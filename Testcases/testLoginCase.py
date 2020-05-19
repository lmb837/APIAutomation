import pytest
import allure,os
from common.Basic import *

class TestLoginCase():

    @allure.step(title="登录用例1")
    def test_case1(self):
        status=getCaseStatus(os.getcwd()+"/data/testcase.xlsx", "清单测试用例", 1)
        assert status

    @allure.step(title="登录用例2")
    def test_case2(self):
        status=getCaseStatus(os.getcwd()+"/data/testcase.xlsx", "清单测试用例", 2)
        assert status

    @allure.step(title="登录用例3")
    def test_case3(self):
        status=getCaseStatus(os.getcwd()+"/data/testcase.xlsx", "清单测试用例", 3)
        assert status

    @allure.step(title="登录用例4")
    def test_case4(self):
        status=getCaseStatus(os.getcwd()+"/data/testcase.xlsx", "清单测试用例", 4)
        assert status

    @allure.step(title="登录用例5")
    def test_case5(self):
        status=getCaseStatus(os.getcwd()+"/data/testcase.xlsx", "清单测试用例", 5)
        assert False