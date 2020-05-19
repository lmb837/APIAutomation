import xlrd, xlwt
from common.SendMethod import SendMethod
from common.WriteExcel import WriteExcel
from common.isJson import is_json
from common.Basic import *
from common.ReplaceParams import *
from openpyxl.styles import Font, colors
import json


def baseCase(file_path, case_sheet_name, inter_sheet_name, variable_sheet_name):
    workbook = xlrd.open_workbook(file_path)
    sheetName = workbook.sheet_by_name(case_sheet_name)
    apiIdList = getCaseApiId(file_path, case_sheet_name, "ApiId")
    newHeaders = {}
    Cookie = {}
    orrelationDict = {}
    for i in apiIdList:
        for row in range(sheetName.nrows):
            for col in range(sheetName.ncols):
                if (sheetName.row(row)[col].value == i):
                    url = getUrl(file_path, inter_sheet_name, sheetName.row(row)[col].value, "Url")
                    headers = getHeaders(file_path, inter_sheet_name, sheetName.row(row)[col].value,
                                         "Headers")
                    headers = eval(headers)
                    reqMethod = getReqMethod(file_path, inter_sheet_name, sheetName.row(row)[col].value,
                                             "ReqMethod")
                    params = sheetName.row(row)[
                        getCaseTitle(file_path, case_sheet_name).index("Data")].value
                    orrelation = sheetName.row(row)[
                        getCaseTitle(file_path, case_sheet_name).index("Orrelation")].value
                    data = ReplaceParams.replaceParams(params, getVariableKeyList(file_path,
                                                                                  variable_sheet_name),
                                                       setVariableDict(file_path, variable_sheet_name))
                    exceptResult = sheetName.row(row)[
                        getCaseTitle(file_path, case_sheet_name).index("ExpectResult")].value

                    for key in orrelationDict.keys():
                        if key in url:
                            url = url.replace(key + '&', str(orrelationDict[key]) + '&')
                    if "post" == reqMethod:
                        if newHeaders:
                            res = SendMethod.postByJson(url, data.encode(), newHeaders)
                        else:
                            res = SendMethod.postByJson(url, data.encode(), headers)
                            newHeaders.update(headers)
                        print(res.text)
                        cookies = str(res.cookies).split(" ")
                        for cookie in cookies:
                            if "JSESSIONID" in cookie:
                                Cookie['Cookie'] = cookie
                                newHeaders.update(Cookie)
                        WriteExcel.writeExcel(file_path, case_sheet_name, row,
                                              getCaseTitle(file_path, case_sheet_name).index(
                                                  "ActualResult"), res.text,
                                              xlwt.easyxf('font: colour_index black;'))
                        actualResult = res.text
                        if is_json(actualResult):
                            actualResultDict = json.loads(actualResult)
                            if orrelation and orrelation in actualResult:
                                try:
                                    orrelationDict[orrelation] = actualResultDict[orrelation]
                                except:
                                    print("返回值不存在" + orrelation + "该字段")
                            if (isinstance(exceptResult, float)):
                                exceptResult = str(int(exceptResult))
                            if (res.status_code == 200):
                                WriteExcel.writeExcel(file_path, case_sheet_name, row,
                                                      getCaseTitle(file_path, case_sheet_name).index(
                                                          "Status"),
                                                      "True", xlwt.easyxf('font: colour_index green;'))
                            elif (exceptResult.strip() != "" and exceptResult in actualResult):
                                WriteExcel.writeExcel(file_path, case_sheet_name, row,
                                                      getCaseTitle(file_path, case_sheet_name).index(
                                                          "Status"),
                                                      "True", xlwt.easyxf('font: colour_index green;'))
                            else:
                                WriteExcel.writeExcel(file_path, case_sheet_name, row,
                                                      getCaseTitle(file_path, case_sheet_name).index(
                                                          "Status"),
                                                      "False", xlwt.easyxf('font: colour_index red;'))
                    elif "get" == reqMethod:
                        for key in orrelationDict.keys():
                            if key in url:
                                url = url.replace(key + '&', str(orrelationDict[key]) + '&')
                        if newHeaders:
                            res = SendMethod.get(url, data, newHeaders)
                            print(res.text)
                        else:
                            res = SendMethod.get(url, data, newHeaders)
                        cookies = str(res.cookies).split(" ")
                        for cookie in cookies:
                            if "JSESSIONID" in cookie:
                                Cookie['Cookie'] = cookie
                                newHeaders.update(Cookie)
                        WriteExcel.writeExcel(file_path, case_sheet_name, row,
                                              getCaseTitle(file_path, case_sheet_name).index(
                                                  "ActualResult"), res.text,
                                              xlwt.easyxf('font: colour_index black;'))
                        actualResult = res.text
                        if is_json(actualResult):
                            actualResultDict = json.loads(actualResult)
                            if orrelation and orrelation in actualResult:
                                try:
                                    orrelationDict[orrelation] = actualResultDict[orrelation]
                                except:
                                    try:
                                        orrelationDict[orrelation] = actualResultDict['data'][orrelation]
                                    except:
                                        print("返回值不存在" + orrelation + "该字段")
                            if (isinstance(exceptResult, float)):
                                exceptResult = str(int(exceptResult))
                            if (res.status_code == 200):
                                WriteExcel.writeExcel(file_path, case_sheet_name, row,
                                                      getCaseTitle(file_path, case_sheet_name).index(
                                                          "Status"),
                                                      "True", xlwt.easyxf('font: colour_index green;'))
                            elif (exceptResult.strip() != "" and exceptResult in actualResult):
                                WriteExcel.writeExcel(file_path, case_sheet_name, row,
                                                      getCaseTitle(file_path, case_sheet_name).index(
                                                          "Status"),
                                                      "True", xlwt.easyxf('font: colour_index green;'))
                            else:
                                WriteExcel.writeExcel(file_path, case_sheet_name, row,
                                                      getCaseTitle(file_path, case_sheet_name).index(
                                                          "Status"),
                                                      "False", xlwt.easyxf('font: colour_index red;'))
