import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.set_window_size(1024, 600)
driver.maximize_window()


@pytest.mark.order1
def test_user_navigates_to_login_screen():
    verify_title()
    driver.find_element(By.XPATH, "//*[@id='menu-item-39']/a").click()
    timeout = 1
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//*[@id='MLemail']"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")


@pytest.mark.order2
def test_verify_page_title():
    verify_title()


@pytest.mark.order3
def test_login():
    log_in()
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[1])
    driver.find_element(By.XPATH, "//input[@id='MLemail']").send_keys("kev_lee2002@hotmail.com")
    driver.find_element(By.ID, "MLpassword").send_keys("22Paignton")
    driver.find_element(By.XPATH,
                        '//body/app-root[1]/app-member-login[1]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]').click()
    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//a[@id='profileDropdown']"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    expected_title = "SDET Unicorns"
    assert driver.title == expected_title


@pytest.mark.order4
def test_unsuccessful_login():
    log_in()
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[2])
    driver.find_element(By.XPATH, "//input[@id='MLemail']").send_keys("HGDNN@gmail.com")
    driver.find_element(By.ID, "MLpassword").send_keys("jhskjsh")
    driver.find_element(By.XPATH,
                        '//body/app-root[1]/app-member-login[1]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]').click()
    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//h2[@id='swal2-title']"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")


def verify_title():
    driver.get("https://sdetunicorns.com")
    expected_title = "Master Software Testing and Automation | SDET Unicorns"
    assert driver.title == expected_title


def log_in():
    verify_title()
    driver.find_element(By.XPATH, "//*[@id='menu-item-39']/a").click()

    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.ID, 'MLemail'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")


if __name__ == '__main__':
    log_in()
