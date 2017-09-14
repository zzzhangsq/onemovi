# coding=utf-8
import os
import unittest
from appium import webdriver
from time import sleep


class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = 'accf8547bbd6'
        desired_caps['appPackage'] = 'com.onemovi.app'
        desired_caps['appActivity'] = '.modules.activity.StartupActivity'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def tearDown(self):
        self.driver.quit()
    def test_create_album(self):
        sleep(5)
        self.driver.find_element_by_id("com.onemovi.app:id/btn_create").click()
        sleep(5)
        self.driver.find_element_by_id("com.onemovi.app:id/tv_album_scene").click()

        # 获取当前手机屏幕大小X,Y
        X = self.driver.get_window_size()['width']
        Y = self.driver.get_window_size()['height']
        print (X,Y)
        a = 98.8 / 1280
        b = 138.8 / 720.0
        self.driver.tap([(a * X, b * Y)])
        sleep(2)

        a = 269.7 / 1280
        b = 138.8 / 720.0
        self.driver.tap([(a * X, b * Y)])
        sleep(2)

        a = 440.7 / 1280
        b = 138.8 / 720
        self.driver.tap([(a * X, b * Y)])

        self.driver.find_element_by_id("com.onemovi.app:id/tv_done").click()
        self.driver.tap([(a * X, b * Y)])
        self.driver.tap([(a * X, b * Y)])
        self.driver.tap([(a * X, b * Y)])

        self.driver.find_element_by_id("com.onemovi.app:id/iv_back").click()

        self.driver.find_element_by_id("com.onemovi.app:id/lly_bg").click()
        self.driver.find_element_by_id("com.onemovi.app:id/et_author").send_keys("zhangsuqin")
        self.driver.find_element_by_id("com.onemovi.app:id/tv_done").click()
        self.driver.find_element_by_id("com.onemovi.app:id/iv_save").click()
    def test_swipe(self):
        for i in range(0,9):
            self.test_create_album()
            self.driver.find_element_by_id("com.onemovi.app:id/iv_back").click()



if __name__ == '__main__':
    unittest.main()
