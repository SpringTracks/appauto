import HTMLTestRunnerCN
import os
import time

from ddt import ddt, data
from appium import webdriver
from time import sleep
import unittest
from parameterized import parameterized
from common.excel_read import getExcelTestData
from common.iselement import isElement
import configparser


@ddt
class MyTests(unittest.TestCase):
    def setUp(self):#初始化-进入测试app
        #读取配置文件中的参数用于初始化driver
        config = configparser.ConfigParser()
        config.read('./common/configinfo.ini')
        caps = {}
        caps["platformName"] = config['DEFAULT']['platformName']
        caps["appPackage"] = config['DEFAULT']['appPackage']
        caps["appActivity"] = config['DEFAULT']['appActivity']
        caps["platformVersion"] = config['DEFAULT']['platformVersion']
        caps["deviceName"] = config['DEFAULT']['deviceName']
        caps["ensureWebviewsHavePages"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    #测试方法
    def boot(self):
        #同意协议
        el1 = self.driver.find_element_by_id("com.moji.mjweather:id/j1")
        el1.click()
        sleep(10)

        #输入济南并选择济南
        el5=self.driver.find_element_by_id('com.moji.mjweather:id/b5h')
        el5.send_keys("济南")
        sleep(2)
        el6=self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("济南市")')
        el6.click()
        sleep(5)
        #判断是否有弹出提示窗口，如有，关闭掉
        isPop=isElement(self,id,"com.moji.mjweather:id/b3z")
        #print(isPop)
        if isPop:
            self.driver.find_element_by_id("com.moji.mjweather:id/b3z").click()#点击弹窗右上方的×号
        # try:
        #     self.driver.find_element_by_id("com.moji.mjweather:id/b3j").click()
        # except Exception as e:
        #     print(e)

     #校验是否添加济南成功
    @data(*getExcelTestData('Sheet1'))
    def test_Location(self,data):
        self.boot()
        comparedLocation=tuple(data)

        el7=self.driver.find_element_by_id("com.moji.mjweather:id/en")
        locationString=el7.text
        locationString2=locationString[0:2]
        #print(locationString2)
        self.assertEqual(comparedLocation[0],locationString2)


    #测试退出
    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = self.list2reason(result.errors)
        failure = self.list2reason(result.failures)
        ok = not error and not failure
        if not ok:
            timestr = time.strftime("%Y-%m-%d_%H_%M_%S")
            self.driver.get_screenshot_as_file('./errorimages/地点_%s.png' %(timestr))
        self.driver.quit()

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]
        #self.driver.quit()