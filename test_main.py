from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def verify_title():
    driver.get("https://sdetunicorns.com")
    title = driver.title
    print(title)
    expected_title = "Master Software Tsting and Automation | SDET Unicorns"
    if title == expected_title:
        print("get in")
    else:
        print("oh no")
    driver.quit()


if __name__ == '__main__':
    verify_title()


def test_001():
    verify_title()
