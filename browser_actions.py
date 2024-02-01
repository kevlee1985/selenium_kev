from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import static_values

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

    def nav_create_account(self):
        self.nav_login_page()
        self.driver.find_element(By.XPATH, static_values.create_account_button).click()
        self.wait_until(static_values.login_full_name_field)

