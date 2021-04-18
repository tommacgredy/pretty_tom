# 运行所有测试用例的主程序文件
import os,unittest,time
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner


def get_all_cases():
    """
    获取Login_Testcases下的所有测试模块
    """
    start_dir = os.path.dirname(__file__)
    print(start_dir)
    pattern = 'oa*.py'
    TestSuite = unittest.defaultTestLoader.discover(start_dir, pattern)
    return TestSuite

def run_main():
    """
    1.运行测试用例
    2.生成测试报告
    3.将测试报告写入指定的目录下
    """
    fp = open(os.path.join(os.path.dirname(__file__), 'Reports',time.strftime('%Y_%m_%d_%H_%M_%S') +'report.html'), 'w', encoding='utf-8')
    runner = HTMLTestRunner(stream=fp, title='自动化测试', description='python自动化')
    runner.run(get_all_cases())


if __name__ == '__main__':
    run_main()