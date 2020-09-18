# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from time import sleep

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "10"
caps["deviceName"] = "dd1b2e2d"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_xpath("//android.widget.ImageView[@content-desc=\"天气\"]")
el1.click()
el2 = driver.find_element_by_id("com.miui.weather2:id/activity_main_city_name")
el2.click()
el3 = driver.find_element_by_accessibility_id("城市管理")
el3.click()
el4 = driver.find_element_by_id("com.miui.weather2:id/act_find_city_key")
el4.click()
sleep(3)
el5 = driver.find_element_by_id("com.miui.weather2:id/act_find_city_key")
el5.send_keys("北京")

driver.quit()