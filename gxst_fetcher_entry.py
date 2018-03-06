#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
from selenium import webdriver

if __name__ == '__main__':

    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(120)
    driver.get('http://www.gsxt.gov.cn/index.html')

    input_ele = driver.find_element_by_id('keyword')
    input_ele.clear()
    input_ele.send_keys(u'浙江久立特材科技股份有限公司')

    time.sleep(2)

    btn_ele = driver.find_element_by_id('btn_query')
    btn_ele.click()

    line_item = driver.find_element_by_css_selector('.search_list_item .db')

    print line_item[0]