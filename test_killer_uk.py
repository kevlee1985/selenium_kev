import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from killer_methods import BrowserActions
import sv_killer
from string_gen import RandomStringGenerator
import time

url = sv_killer.base_url_uk


@pytest.fixture
def random_string_generator():
    return RandomStringGenerator()


@pytest.fixture
def setup_teardown():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()


class TestClass:

    def test_verify_page_title(self, setup_teardown):
        driver = setup_teardown
        killer_methods = BrowserActions(driver)
        killer_methods.verify_title()

    def test_user_navigates_to_login_screen(self, setup_teardown):
        driver = setup_teardown
        killer_methods = BrowserActions(driver)
        killer_methods.verify_title()
        killer_methods.nav_login_page()

    def test_login(self, setup_teardown):
        driver = setup_teardown
        killer_methods = BrowserActions(driver)
        killer_methods.log_in("kev_lee2002@hotmail.com", "22Paignton")
        driver.find_element(By.XPATH, sv_killer.submit_login_button).click()
        killer_methods.wait_until(sv_killer.account_information)

    def test_unsuccessful_login(self, setup_teardown):
        driver = setup_teardown
        killer_methods = BrowserActions(driver)
        killer_methods.log_in("HGDNN@gmail.com", "jhskjsh")
        driver.find_element(By.XPATH, sv_killer.submit_login_button).click()
        time.sleep(2)
        killer_methods.wait_until(sv_killer.login_error_popup)

    def test_nav_to_create_account(self, setup_teardown):
        driver = setup_teardown
        killer_methods = BrowserActions(driver)
        killer_methods.nav_create_account()

    def test_add_product_to_cart(self, setup_teardown):
        driver = setup_teardown
        killer_methods = BrowserActions(driver)
        killer_methods.log_in("kev_lee2002@hotmail.com", "22Paignton")
        driver.find_element(By.XPATH, sv_killer.submit_login_button).click()
        killer_methods.wait_until(sv_killer.account_information)
        killer_methods.clear_cart()
        driver.find_element(By.XPATH, sv_killer.search_bar).send_keys("xion")
        driver.find_element(By.XPATH, sv_killer.search_bar_go_button).click()
        killer_methods.wait_until(sv_killer.xion_machine)
        driver.find_element(By.XPATH, sv_killer.xion_machine).click()
        driver.find_element(By.XPATH, sv_killer.add_to_cart).click()
        killer_methods.wait_until(sv_killer.basket_button)
        driver.find_element(By.XPATH, sv_killer.basket_button).click()
        killer_methods.wait_until(sv_killer.basket_item)

    def test_remove_product_from_cart(self, setup_teardown):
        driver = setup_teardown
        killer_methods = BrowserActions(driver)
        killer_methods.log_in("kev_lee2002@hotmail.com", "22Paignton")
        driver.find_element(By.XPATH, sv_killer.submit_login_button).click()
        killer_methods.wait_until(sv_killer.account_information)
        killer_methods.clear_cart()
        driver.find_element(By.XPATH, sv_killer.search_bar).send_keys("xion")
        driver.find_element(By.XPATH, sv_killer.search_bar_go_button).click()
        killer_methods.wait_until(sv_killer.xion_machine)
        driver.find_element(By.XPATH, sv_killer.xion_machine).click()
        driver.find_element(By.XPATH, sv_killer.add_to_cart).click()
        if driver.find_elements(By.XPATH, sv_killer.close_icon):
            time.sleep(5)
            driver.find_element(By.XPATH, sv_killer.close_icon).click()
            print("Clicked the close button.")
        else:
            print("Close button not found. Doing nothing.")
        time.sleep(5)
        killer_methods.wait_until(sv_killer.basket_button)
        driver.find_element(By.XPATH, sv_killer.basket_button).click()
        killer_methods.wait_until(sv_killer.basket_item)
        time.sleep(2)
        driver.find_element(By.XPATH, sv_killer.remove_item).click()
        killer_methods.wait_until(sv_killer.empty_shopping_cart)
