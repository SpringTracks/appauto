# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from time import sleep
import unittest

class MyTests(unittest.TestCase):
    def setUp(self):#初始化
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.moji.mjweather"
        caps["appActivity"] = "MainActivity"
        caps["platformVersion"] = "5.1.1"
        caps["deviceName"] = "127.0.0.1:62001 device"
        caps["ensureWebviewsHavePages"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    #测试方法
    def test_calculator(self):
        el1 = self.driver.find_element_by_id("com.moji.mjweather:id/bws")
        el1.click()
        #同意协议
        sleep(5)
        el3=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.TextView[3]")
        el3.click()
        sleep(8)

        #选择北京
        #el4=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout[2]").click()

        #输入济南并选择济南
        el5=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText")
        el5.send_keys("济南")
        sleep(2)
        el6=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.view.View[1]")
        el6.click()
        sleep(5)
        #校验是否添加济南成功
        el7=self.driver.find_element_by_id("com.moji.mjweather:id/ek")
        locationString=el7.text
        locationString2=locationString[0:2]
        print(locationString2)

    #测试退出
    def tearDown(self):
        self.driver.quit()