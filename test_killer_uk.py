import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from killer_methods import BrowserActions
import sv_killer
from string_gen import RandomStringGenerator
from selenium.webdriver.support import expected_conditions as EC
import time

url = sv_killer.base_url_uk


@pytest.fixture
def random_string_generator():
    return RandomStringGenerator()


@pytest.fixture
def setup_teardown():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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
        killer_methods.wait_until(sv_killer.account_information, 3)

    def test_logout(self, setup_teardown):
        driver = setup_teardown
        killer_methods = BrowserActions(driver)
        killer_methods.log_in("kev_lee2002@hotmail.com", "22Paignton")
        driver.find_element(By.XPATH, sv_killer.submit_login_button).click()
        killer_methods.wait_until(sv_killer.account_information, 3)
        killer_methods.wait_until(sv_killer.logout_button, 3)
        driver.find_element(By.XPATH, sv_killer.logout_button).click()
        killer_methods.wait_until(sv_killer.login_button, 3)

    def test_unsuccessful_login(self, setup_teardown):
        driver = setup_teardown
        killer_methods = BrowserActions(driver)
        killer_methods.log_in("HGDNN@gmail.com", "jhskjsh")
        driver.find_element(By.XPATH, sv_killer.submit_login_button).click()
        time.sleep(2)
        killer_methods.wait_until(sv_killer.login_error_popup, 3)

    def test_nav_to_create_account(self, setup_teardown):
        driver = setup_teardown
        killer_methods = BrowserActions(driver)
        killer_methods.nav_create_account()

    def test_add_product_to_cart(self, setup_teardown):
        driver = setup_teardown
        killer_methods = BrowserActions(driver)
        killer_methods.add_product_to_cart()

    def test_remove_product_from_cart(self, setup_teardown):
        driver = setup_teardown
        killer_methods = BrowserActions(driver)
        killer_methods.add_product_to_cart()
        killer_methods.wait_until(sv_killer.basket_item, 3)
        time.sleep(2)
        driver.find_element(By.XPATH, sv_killer.remove_item).click()
        killer_methods.wait_until(sv_killer.empty_shopping_cart, 3)

    def test_checkout_total(self, setup_teardown):
        driver = setup_teardown
        killer_methods = BrowserActions(driver)
        killer_methods.add_product_to_cart()
        killer_methods.wait_until(sv_killer.proceed_to_checkout_button, 3)
        time.sleep(5)
        driver.find_element(By.XPATH, sv_killer.proceed_to_checkout_button).click()
        killer_methods.wait_until(sv_killer.order_review_page, 10)
        expected_title = "Checkout"
        total_price = 562.74
        time.sleep(5)
        price_element = driver.find_element(By.XPATH, sv_killer.price_element).text
        cart_subtotal = driver.find_element(By.XPATH, sv_killer.cart_subtotal).text
        tax = driver.find_element(By.XPATH, sv_killer.Tax).text
        price_text = float(price_element[1:])
        subtotal_text = float(cart_subtotal[1:])
        tax_text = float(tax[1:])
        assert expected_title == driver.title
        assert total_price == price_text
        assert price_text == subtotal_text + tax_text

    def test_adding_elements_to_basket(self, setup_teardown):
        driver = setup_teardown
        killer_methods = BrowserActions(driver)
        killer_methods.add_product_to_cart()
        killer_methods.wait_until(sv_killer.proceed_to_checkout_button, 3)
        time.sleep(5)
        price_element = driver.find_element(By.XPATH, sv_killer.basket_screen_price).text
        price_text = float(price_element[1:])
        print(price_text)
        driver.find_element(By.XPATH, sv_killer.add_item_icon).click()
        time.sleep(5)
        item_count = driver.find_element(By.XPATH, sv_killer.item_count)
        value_attribute = int(item_count.get_attribute("value"))
        total_price = 1125.48
        assert value_attribute == 2
        assert total_price == price_text * value_attribute

    def test_hover_over(self, setup_teardown):
        driver = setup_teardown
        killer_methods = BrowserActions(driver)
        killer_methods.log_in("kev_lee2002@hotmail.com", "22Paignton")
        driver.find_element(By.XPATH, sv_killer.submit_login_button).click()
        killer_methods.wait_until(sv_killer.account_information, 3)
        killer_methods.hover_over_element(sv_killer.basket_button)
        time.sleep(5)
        sub_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, sv_killer.bin_button))
        )
        sub_element.click()
        killer_methods.wait_until(sv_killer.empty_basket, 3)
        time.sleep(5)
        alert = driver.switch_to.alert
        alert.driver.find_element(By.XPATH, sv_killer.are_you_sure_overlay).click()
        driver.find_element(By.XPATH, sv_killer.basket_button)
        killer_methods.wait_until(sv_killer.empty_shopping_cart, 3)

