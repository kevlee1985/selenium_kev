from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def verify_title():
    driver.get("https://sdetunicorns.com")
    title = driver.title
    expected_title = "Master Software Testing and Automation | SDET Unicorns"
    assert title == expected_title


if __name__ == '__main__':
    verify_title()


def test_001():
    verify_title()

