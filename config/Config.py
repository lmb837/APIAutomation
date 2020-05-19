import os, sys
import configparser


def getConfig():
    config = configparser.ConfigParser()

    configFile = config.read('./config/caseConfig.ini', encoding="utf-8-sig")
    sections = config.sections()
    dictConfig = {}
    for section in sections:
        options = config.options(section)
        for option in options:
            value = config.get(section, option)
            dictConfig[option] = value
    print(dictConfig)
    return dictConfig

def getFile():
    print(os.getcwd())

    dictConfig = getConfig();
    caseFile = dictConfig['casefile']
    return caseFile

def getApi():
    dictConfig = getConfig();
    caseApi = dictConfig['interfaceapi']
    return caseApi
def getVariableSheetName():
    dictConfig = getConfig();
    variableSheetName = dictConfig['variablesheetname']
    return variableSheetName
def getCaseSheets():
    caseSheets = []
    dictConfig = getConfig();
    del [dictConfig['casefile']]
    del [dictConfig['interfaceapi']]
    del [dictConfig['variablesheetname']]
    for caseSheet in dictConfig.values():
        caseSheets.append(caseSheet)
    return caseSheets



if __name__ == '__main__':
    a=getConfig()
    print(a)
    # CaseConfig().getCaseConfig2();
    # CaseConfig().getFile();
    # CaseConfig().getApi();
    # CaseConfig().getCaseSheets();
