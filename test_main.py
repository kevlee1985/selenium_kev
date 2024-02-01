import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser_actions import BrowserActions
import static_values
from string_gen import RandomStringGenerator


@pytest.fixture
def random_string_generator():
    return RandomStringGenerator()


@pytest.fixture
def setup_teardown():
    # Setup: Open the browser
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    # Provide the driver instance to the test function
    yield driver
    # Teardown: Close the browser
    driver.quit()


class TestClass:

    def test_verify_page_title(self, setup_teardown):
        driver = setup_teardown
        browser_actions = BrowserActions(driver)
        browser_actions.verify_title()

    def test_user_navigates_to_login_screen(self, setup_teardown):
        driver = setup_teardown
        browser_actions = BrowserActions(driver)
        browser_actions.verify_title()
        browser_actions.nav_login_page()

    def test_login(self, setup_teardown):
        driver = setup_teardown
        browser_actions = BrowserActions(driver)
        browser_actions.log_in("kev_lee2002@hotmail.com", "22Paignton")
        driver.find_element(By.XPATH, static_values.submit_login_button).click()
        browser_actions.wait_until(static_values.account_dropdown)
        expected_title = "SDET Unicorns"
        assert driver.title == expected_title

    def test_unsuccessful_login(self, setup_teardown):
        driver = setup_teardown
        browser_actions = BrowserActions(driver)
        browser_actions.log_in("HGDNN@gmail.com", "jhskjsh")
        driver.find_element(By.XPATH, static_values.submit_login_button).click()
        browser_actions.wait_until(static_values.login_error_popup)
        expected_title = "SDET Unicorns"
        assert driver.title == expected_title

    def test_nav_to_create_account(self, setup_teardown):
        driver = setup_teardown
        browser_actions = BrowserActions(driver)
        browser_actions.nav_login_page()
        driver.find_element(By.XPATH, static_values.create_account_button).click()
        browser_actions.wait_until(static_values.login_full_name_field)
        expected_title = "SDET Unicorns"
        assert driver.title == expected_title

    def test_create_new_account1(self, setup_teardown, random_string_generator):
        driver = setup_teardown
        browser_actions = BrowserActions(driver)
        browser_actions.create_new_account(random_string_generator)
