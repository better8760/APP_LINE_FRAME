import pytest
from appium import webdriver
import time


driver=None
@pytest.fixture()
def start_app(driverenv):
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',driverenv)
    return driver

@pytest.fixture(autouse=True)
def close_app():
    yield driver
    time.sleep(2)
    driver.close_app()
