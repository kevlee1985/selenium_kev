import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import static_values
from string_gen import RandomStringGenerator


@pytest.fixture
def random_string_generator():
    return RandomStringGenerator()


url = static_values.base_url


class BrowserActions:
    def __init__(self, driver):
        self.driver = driver

    def verify_title(self):
        self.driver.get(url)
        expected_title = "Master Software Testing and Automation | SDET Unicorns"
        assert self.driver.title == expected_title

    def log_in(self, username, password):
        self.nav_login_page()
        self.driver.find_element(By.XPATH, static_values.email_address).send_keys(username)
        self.driver.find_element(By.ID, static_values.password).send_keys(password)

    def nav_login_page(self):
        self.verify_title()
        self.driver.find_element(By.XPATH, static_values.login_button).click()
        timeout = 5
        try:
            element_present = EC.presence_of_element_located((By.ID, 'MLemail'))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])

    def wait_until(self, element):
        timeout = 5
        try:
            element_present = EC.presence_of_element_located((By.XPATH, element))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

    def wait_until_disappear(self, element):
        timeout = 10
        try:
            element_not_present = EC.invisibility_of_element_located((By.XPATH, element))
            WebDriverWait(self.driver, timeout).until(element_not_present)
        except TimeoutException:
            print("Timed out waiting for element to disappear")

    def nav_create_account(self):
        self.nav_login_page()
        self.driver.find_element(By.XPATH, static_values.create_account_button).click()
        self.wait_until(static_values.login_full_name_field)

    def create_new_account(self, random_string_generator):
        self.nav_create_account()
        string_1 = random_string_generator.generate_random_string(length=8)
        self.driver.find_element(By.XPATH, static_values.login_full_name_field).send_keys(string_1)
        self.driver.find_element(By.XPATH, static_values.create_account_email).send_keys(string_1 + "@hotmail.com")
        self.driver.find_element(By.XPATH, static_values.create_account_password).send_keys(string_1 + "111")
        self.driver.find_element(By.XPATH, static_values.sign_up_button).click()
        self.wait_until(static_values.email_address)
        self.driver.find_element(By.XPATH, static_values.email_address).send_keys(string_1 + "@hotmail.com")
        self.driver.find_element(By.ID, static_values.password).send_keys(string_1 + "111")
        self.driver.find_element(By.XPATH, static_values.submit_login_button).click()
        self.wait_until(static_values.account_dropdown)
