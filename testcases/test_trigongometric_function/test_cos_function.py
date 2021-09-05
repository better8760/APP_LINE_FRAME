from appium import webdriver
import time
import allure

@allure.epic("[epic]简单计算器")
@allure.feature("三角函数计算模块")
@allure.story("cos函数运算场景")
class Test_cos_function():
    @allure.title("cos正数")
    def test_cos_case_01(self,start_app):
        driver=start_app
        driver.find_element_by_id("com.sky.jisuanji:id/btn1").click()
        driver.find_element_by_id("com.sky.jisuanji:id/cos").click()
        result=driver.find_element_by_id("com.sky.jisuanji:id/text").text
        assert float(result)>0.54
        time.sleep(1)