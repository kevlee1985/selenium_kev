import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sv_killer
import sv_killer_de
import sv_killer_ie
from string_gen import RandomStringGenerator
import time


@pytest.fixture
def random_string_generator():
    return RandomStringGenerator()


class BrowserActions:
    def __init__(self, driver):
        self.driver = driver

    def verify_title(self):
        time.sleep(3)
        data_file_path = self.get_data_file()
        cookie_button = data_file_path.cookie_button
        try:
            accept_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, cookie_button)))
            if accept_button:
                accept_button.click()
                print("Cookie consent accepted.")
            else:
                print("Cookie consent button not found.")
        except Exception as e:
            print(f"Error handling cookie consent: {e}")
            expected_title = data_file_path.expected_title
            assert self.driver.title == expected_title

    def log_in(self, username, password):
        self.nav_login_page()
        data_file_path = self.get_data_file()
        self.driver.find_element(By.XPATH, data_file_path.email_address).send_keys(username)
        self.driver.find_element(By.XPATH, data_file_path.password).send_keys(password)

    def nav_login_page(self):
        self.verify_title()
        data_file_path = self.get_data_file()
        self.wait_until(data_file_path.login_button, 3)
        self.driver.find_element(By.XPATH, data_file_path.login_button).click()
        self.clear_cookies()
        self.wait_until('//h1[contains(text(),"Customer Login")]', 2)

    def wait_until(self, element, seconds):
        timeout = seconds
        try:
            element_present = EC.presence_of_element_located((By.XPATH, element))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

    def wait_until_disappear(self, element, seconds):
        timeout = seconds
        try:
            element_not_present = EC.invisibility_of_element_located((By.XPATH, element))
            WebDriverWait(self.driver, timeout).until(element_not_present)
        except TimeoutException:
            print("Timed out waiting for element to disappear")

    def nav_create_account(self):
        self.nav_login_page()
        data_file_path = self.get_data_file()
        self.driver.find_element(By.XPATH, data_file_path.create_account_button).click()
        self.wait_until(data_file_path.create_new_customer_account, 3)

    def get_data_file(self):
        data_file = ''
        current_url = self.driver.current_url
        if 'co.uk' in current_url:
            data_file = sv_killer
        elif 'ie' in current_url:
            data_file = sv_killer_ie
        elif 'de' in current_url:
            data_file = sv_killer_de
        return data_file

    def clear_cart(self):
        data_file_path = self.get_data_file()
        self.driver.find_element(By.XPATH, data_file_path.basket_button).click()
        time.sleep(3)
        if self.driver.find_elements(By.XPATH, data_file_path.remove_item):
            self.driver.find_element(By.XPATH, data_file_path.remove_item).click()
            time.sleep(3)
            if self.driver.find_elements(By.XPATH, data_file_path.are_you_sure):
                self.driver.find_element(By.XPATH, data_file_path.are_you_sure).click()
        elif self.driver.find_elements(By.XPATH, data_file_path.remove_all_button):
            self.driver.find_element(By.XPATH, data_file_path.remove_all_button).click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, data_file_path.are_you_sure).click()
        self.wait_until(data_file_path.empty_shopping_cart, 3)

    def clear_cookies(self):
        data_file_path = self.get_data_file()
        cookie_button = data_file_path.cookie_button
        try:
            accept_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, cookie_button)))
            if accept_button:
                accept_button.click()
                print("Cookie consent accepted.")
            else:
                print("Cookie consent button not found.")
        except Exception as e:
            print(f"Error handling cookie consent: {e}")

    def add_product_to_cart(self):
        self.log_in("kev_lee2002@hotmail.com", "22Paignton")
        self.driver.find_element(By.XPATH, sv_killer.submit_login_button).click()
        self.wait_until(sv_killer.account_information, 3)
        self.clear_cart()
        self.driver.find_element(By.XPATH, sv_killer.search_bar).send_keys("xion")
        self.driver.find_element(By.XPATH, sv_killer.search_bar_go_button).click()
        self.wait_until(sv_killer.xion_machine, 3)
        self.driver.find_element(By.XPATH, sv_killer.xion_machine).click()
        self.driver.find_element(By.XPATH, sv_killer.add_to_cart).click()
        time.sleep(5)
        if self.driver.find_elements(By.XPATH, sv_killer.close_icon):
            self.driver.find_element(By.XPATH, sv_killer.close_icon).click()
        else:
            self.wait_until(sv_killer.basket_button, 3)
        time.sleep(5)
        self.driver.find_element(By.XPATH, sv_killer.basket_button).click()
        self.wait_until(sv_killer.basket_item, 3)
