
from time import sleep

from selenium.common.exceptions import NoSuchElementException


def isElement(self,identifyBy,c):
    '''
    Determine whether elements exist
    Usage:
    isElement(By.XPATH,"//a")
    '''
    sleep(1)
    flag=None
    try:
        if identifyBy == "id":
            #self.driver.implicitly_wait(60)
            self.driver.find_element_by_id(c)
            flag = True
        elif identifyBy == "xpath":
            #self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath(c)
            flag = True
        elif identifyBy == "class":
            self.driver.find_element_by_class_name(c)
            flag = True
        elif identifyBy == "link text":
            self.driver.find_element_by_link_text(c)
            flag = True
        elif identifyBy == "partial link text":
            self.driver.find_element_by_partial_link_text(c)
            flag = True
        elif identifyBy == "name":
            self.driver.find_element_by_name(c)
            flag = True
        elif identifyBy == "tag name":
            self.driver.find_element_by_tag_name(c)
            flag = True
        elif identifyBy == "css selector":
            self.driver.find_element_by_css_selector(c)
            flag = True
    except NoSuchElementException as e:
        flag = False
    finally:
        return flag