import pytest
from appium import webdriver
import time
import allure

@allure.epic("[epic]简单计算器")
@allure.feature("基础计算模块")
@allure.story("减法运算场景")
class Test_sub():
    @allure.title("正数减正数")
    def test_sub_case_01(self,start_app):
        driver = start_app
        driver.find_element_by_id("com.sky.jisuanji:id/btn9").click()
        driver.find_element_by_id("com.sky.jisuanji:id/jia").click()
        driver.find_element_by_id("com.sky.jisuanji:id/btn8").click()
        driver.find_element_by_id("com.sky.jisuanji:id/denyu").click()
        result = driver.find_element_by_id("com.sky.jisuanji:id/text").text
        assert float(result) == 17.0
        time.sleep(1)

