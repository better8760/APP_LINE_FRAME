import pytest
from appium import webdriver
import time
import allure
import os

@allure.epic("[epic]简单计算器")
@allure.feature("基础计算模块")
@allure.story("加法运算场景")

class Test_add():
    @allure.title("正数和正数相加")
    @allure.severity("blocker")
    def test_add_case_01(self,start_app):
        with open(os.path.dirname(__file__)+'/screen_shot/结果.png',"rb") as file:
            img_file=file.read()
            allure.attach(img_file,'结果图示',allure.attachment_type.PNG)
        driver=start_app
        driver.find_element_by_id("com.sky.jisuanji:id/btn6").click()
        driver.find_element_by_id("com.sky.jisuanji:id/jian").click()
        driver.find_element_by_id("com.sky.jisuanji:id/btn3").click()
        driver.find_element_by_id("com.sky.jisuanji:id/denyu").click()
        result=driver.find_element_by_id("com.sky.jisuanji:id/text").text
        assert float(result)==3.0
        time.sleep(1)

    @allure.title("正数和负数相加")
    @allure.severity("blocker")
    def test_add_case_02(self,start_app):
        driver=start_app
        driver.find_element_by_id("com.sky.jisuanji:id/btn6").click()
        driver.find_element_by_id("com.sky.jisuanji:id/jia").click()
        driver.find_element_by_id("com.sky.jisuanji:id/btn8").click()
        driver.find_element_by_id("com.sky.jisuanji:id/zhenfu").click()
        driver.find_element_by_id("com.sky.jisuanji:id/denyu").click()
        result=driver.find_element_by_id("com.sky.jisuanji:id/text").text
        assert float(result)==-2.0
        time.sleep(1)