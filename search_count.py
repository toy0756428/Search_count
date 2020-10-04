#!/usr/bin/env python
#encoding:UTF-8
#version2.0

import os
import sys
import time
import ipaddress
from itertools import chain
from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
chrome_options = Options()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chromedriver, chrome_options=chrome_options)

pd.set_option("display.max_rows", 1000)
pd.set_option("display.max_columns", 1000)
df = pd.read_csv(r"C:\Users\Toy\Desktop\Python\aoi\search_count\csuser__csuser__eam2__search3_1601343261_38661.csv")
filters = []
net_10 = ipaddress.ip_network('10.0.0.0/8').hosts()
net_172 = ipaddress.ip_network('172.16.0.0/12').hosts()
net_192 = ipaddress.ip_network('192.168.0.0/16').hosts()
net_127 = ipaddress.ip_network('127.0.0.0/8').hosts()
net_total = chain(net_10, net_127, net_172, net_192)
for x in net_total:
    filters.append(str(x))

#df = pd.read_csv("csuser__csuser__eam2__search2_1594859881_9778.csv")
#df = df.drop(columns=["UserSid_readable", "fEnd", "fStart"])

def expand_shadow_element(element):
    shadow_root = browser.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root

def user(username):
    cg = df.User_Name.values
    num_genres = pd.DataFrame(np.array(cg).reshape(username, 1))
    a = str(pd.value_counts(num_genres[0]))
    f = open(r"C:\Users\Toy\Desktop\Python\aoi\search_count\user_" + time.strftime('%Y_%m_%d') + ".txt", "w", encoding="utf-8")
    f.write(a)
    f.close()

def host(hostname):
    cg = df.Host_Name.values
    num_genres = pd.DataFrame(np.array(cg).reshape(hostname, 1))
    a = str(pd.value_counts(num_genres[0]))
    f = open(r"C:\Users\Toy\Desktop\Python\aoi\search_count\host_" + time.strftime('%Y_%m_%d') + ".txt", "w", encoding="utf-8")
    f.write(a)
    f.close()

def remote_ip():
    df_new = df[df['Remote_Source_IP'].notnull()]
    mydata = list(df_new.iloc[:, 5])
    f = open(r"C:\Users\Toy\Desktop\Python\aoi\search_count\ip.txt", "w", encoding="utf-8")
    for ip in mydata:
        t = ip.split()
        #s = t.split("[")[1].split("]")[0]
        f.write(str(t))
        f.write("\n")
        for i in range(0, len(t),1):
            if t[i] not in filters:
                url = "https://www.virustotal.com/gui/ip-address/"
                test_ip = url + t[i]
                sleep(3)
                browser.get(test_ip)
                root1 = browser.find_elements_by_tag_name('ip-address-view')
                for root1_kid in root1:
                    sleep(3)
                    shadow_root1 = expand_shadow_element(root1_kid)
                    message = shadow_root1.find_element_by_tag_name('vt-ui-main-generic-report')
                    text = message.get_attribute('detections-string')
                    if text != "No interesting sightings for this IP address":
                        print(t[i])
                        l = open("C:\\Users\\Toy\\Desktop\\Python\\aoi\\search_count\\remoteip_" + time.strftime('%Y_%m_%d') + ".txt", "a", encoding="utf-8")
                        l.write(t[i] + "：trouble\n")
                        l.close()
                    else:
                        print("YA~")
                        l = open("C:\\Users\\Toy\\Desktop\\Python\\aoi\\search_count\\remoteip_" + time.strftime('%Y_%m_%d') + ".txt", "a", encoding="utf-8")
                        l.write(t[i] + "：No problem\n")
                        l.close()
    f.close()
    browser.close()
    browser.quit()

if __name__ == '__main__':
    column = int(input("columns："))
    if type(column) is int:
        user(column)
        host(column)
        remote_ip()
        print(time.strftime('%Y_%m_%d_%H_%M_%S'))
    else:
        print("please input number.")
