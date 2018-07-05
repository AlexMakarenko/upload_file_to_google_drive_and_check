import pytest
from selenium import webdriver

from config import CHROMEDRIVER


@pytest.fixture()
def driver(request):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=CHROMEDRIVER)
    request.addfinalizer(driver.quit)
    return driver
