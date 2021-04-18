import xlrd
import unittest,ddt
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def read_username(row):
    """读取用户名"""
    book = xlrd.open_workbook('data_info.xlsx', 'r')
    table = book.sheet_by_index(0)
    return table.row_values(row)[0]

def read_password(row):  # row表示行号
    """读取登录密码"""
    book = xlrd.open_workbook('data_info.xlsx', 'r')
    table = book.sheet_by_index(0)
    return table.row_values(row)[1]

def read_assertText(row):
    """读取验证信息"""
    book = xlrd.open_workbook('data_info.xlsx', 'r')
    table = book.sheet_by_index(0)
    return table.row_values(row)[2]



