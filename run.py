from common.Basic import *
from Testcases.BaseCase import *
from config.Config import *
from common.SendEmail import *
import os
from common.zipDir import *
if __name__ == "__main__":
    caseConfig = getConfig()
    caseFile = getFile()
    caseApi = getApi()
    caseSheets = getCaseSheets()
    variableSheetName = getVariableSheetName()
    for caseSheet in caseSheets:
        baseCase(caseFile, caseSheet, caseApi, variableSheetName);
    print(os.getcwd())

    os.system("pytest ./Testcases/testLoginCase.py   --alluredir ./report")
    os.system("allure generate ./report/ -o ./report/html --clean")
    zipDir(os.getcwd()+"/report/",os.getcwd()+"/report/html.zip")
    sendEmail()

