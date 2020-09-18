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
        #self.imgs = []
        #self.addCleanup(self.cleanup)

    # def add_img(self):
    #     # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
    #     #self.imgs.append(self.driver.get_screenshot_as_base64())
    #     return True

    #测试方法
    def boot(self):
        #同意协议
        el1 = self.driver.find_element_by_id("com.moji.mjweather:id/iw")
        el1.click()
        # el3=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.TextView[3]")
        # el3.click()
        sleep(10)

        #输入济南并选择济南
        el5=self.driver.find_element_by_id('com.moji.mjweather:id/b52')
        #el5=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText")
        el5.send_keys("济南")
        sleep(2)
        el6=self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("济南市")')
        #el6=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.view.View[1]")
        el6.click()
        sleep(5)
        #判断是否有弹出提示窗口，如有，关闭掉
        isPop=isElement(self,id,"com.moji.mjweather:id/b3j")
        #print(isPop)
        if isPop:
            self.driver.find_element_by_id("com.moji.mjweather:id/b3j").click()#点击弹窗右上方的×号

     #校验是否添加济南成功
    @data(*getExcelTestData('Sheet1'))
    def test_Location(self,data):
        self.boot()
        comparedLocation=tuple(data)

        el7=self.driver.find_element_by_id("com.moji.mjweather:id/ek")
        locationString=el7.text
        locationString2=locationString[0:2]
        #print(locationString2)
        self.assertEqual(comparedLocation[0],locationString2)

    #检验当前温度，parameterized参数化
    # @parameterized.expand([
    #     (26,),
    #     (28,),
    #     # (29,),
    #     # (23,),
    # ])
    # def test_Temperature(self,tem):
    #     self.boot()
    #     sleep(15)
    #     el8=self.driver.find_element_by_id("com.moji.mjweather:id/dt3")
    #     temperature=el8.text
    #     temperatureNum=int(temperature[0:2])
    #     print(temperatureNum)
    #     self.assertEqual(tem,temperatureNum)

    #测试退出
    def tearDown(self):
    #     result = self.defaultTestResult()
    #     self._feedErrorsToResult(result, self._outcome.errors)
    #     error = self.list2reason(result.errors)
    #     failure = self.list2reason(result.failures)
    #     ok = not error and not failure
    #     if not ok:
    #         timestr = time.strftime("%Y-%m-%d_%H_%M_%S")
    #         self.driver.get_screenshot_as_file('./errorimages/%s.png' %(timestr))
    #     self.driver.quit()
    #
    # def list2reason(self, exc_list):
    #     if exc_list and exc_list[-1][0] is self:
    #         return exc_list[-1][1]
        self.driver.quit()