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
    def test_user_navigates_to_login_screen(self, setup_teardown):
        driver = setup_teardown
        browser_actions = BrowserActions(driver)
        browser_actions.verify_title()
        driver.find_element(By.XPATH, static_values.login_button).click()
        timeout = 1
        try:
            element_present = EC.presence_of_element_located((By.XPATH, static_values.email_address))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        finally:
            print("Page loaded")

    def test_verify_page_title(self, setup_teardown):
        driver = setup_teardown
        browser_actions = BrowserActions(driver)
        browser_actions.verify_title()

    def test_login(self, setup_teardown):
        driver = setup_teardown
        browser_actions = BrowserActions(driver)
        browser_actions.log_in("kev_lee2002@hotmail.com", "22Paignton")
        driver.find_element(By.XPATH, static_values.submit_login_button).click()
        timeout = 5
        try:
            element_present = EC.presence_of_element_located((By.XPATH, "//a[@id='profileDropdown']"))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        expected_title = "SDET Unicorns"
        assert driver.title == expected_title

    def test_unsuccessful_login(self, setup_teardown):
        driver = setup_teardown
        browser_actions = BrowserActions(driver)
        browser_actions.log_in("HGDNN@gmail.com", "jhskjsh")
        driver.find_element(By.XPATH, static_values.submit_login_button).click()
        timeout = 5
        try:
            element_present = EC.presence_of_element_located((By.XPATH, "//h2[@id='swal2-title']"))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
