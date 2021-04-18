#coding=utf-8
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get('http://192.168.0.8:8080/oa/login')