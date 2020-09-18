# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
#caps["appPackage"] = "com.baidu.browser.apps_sj"
#caps["appActivity"] = "com.baidu.browser.framework.BdBrowserActivity"
caps["platformVersion"] = "5.1.1"
caps["deviceName"] = "127.0.0.1:62001 device"
caps["ensureWebviewsHavePages"] = True
caps["launchMode"]="standard"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.find_element_by_android_uiautomator("百度浏览器").click()
#el1.click()
# el2 = driver.find_element_by_id("66868fc4-911b-499c-8087-b12eb485f80d")
# el2.send_keys("www.baidu.com")
# el2.click()


driver.find_element_by_xpath('//android.widget.ScrollView/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.LinearLayout[2]/android.view.View[1]').click()
el3=driver.find_element_by_xpath('//android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[5]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]').send_keys("www.hao123.com")
#el3.click()
#el3.send_keys("www.hao123.com")
driver.find_element_by_id('//android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[5]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.view.View[2]').click()


#driver.quit()
