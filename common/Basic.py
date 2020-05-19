import xlrd
# 获取接口标题
def getApiTitle(file_path, sheet_name, i, titleParm):
    workbook = xlrd.open_workbook(file_path)
    sheetName = workbook.sheet_by_name(sheet_name)
    for row in range(sheetName.nrows):
        for col in range(sheetName.ncols):
            if (i == sheetName.row(row)[col].value):
                titleParm = sheetName.row(row)[getCaseTitle(file_path, sheet_name).index(titleParm)].value
    return titleParm


# 获取请求地址
def getUrl(file_path, case_sheet_name, i, titleParm):
    url = getApiTitle(file_path, case_sheet_name, i, titleParm)
    return url


# 获取请求头
def getHeaders(file_path, case_sheet_name, i, titleParm):
    headers = getApiTitle(file_path, case_sheet_name, i, titleParm)
    return headers


# 获取请求方式
def getReqMethod(file_path, case_sheet_name, i, titleParm):
    reqMethod = getApiTitle(file_path, case_sheet_name, i, titleParm)
    return reqMethod


# 获取用例的编号
def getCaseApiId(file_path, sheet_name, titleParm):
    apiIdList = []
    workbook = xlrd.open_workbook(file_path)
    sheetName = workbook.sheet_by_name(sheet_name)
    for row in range(sheetName.nrows):
        for col in range(sheetName.ncols):
            apiId = sheetName.row(row)[getCaseTitle(file_path, sheet_name).index(titleParm)].value
            if (isinstance(apiId, float)):
                apiIdList.append(apiId)
    # 列表去重
    apiIdList = list(set(apiIdList))
    # print(apiIdList)
    return apiIdList


# 获取用例的标题
def getCaseTitle(file_path, case_sheet_name):
    titleList = []
    workbook = xlrd.open_workbook(file_path)
    sheetName = workbook.sheet_by_name(case_sheet_name)
    for row in range(1):
        for col in range(sheetName.ncols):
            titleList.append(sheetName.row(row)[col].value)
    return titleList

# 获取对应用例的状态值:i：指第几条用例
def getCaseStatus(file_path, case_sheet_name,i):
    workbook = xlrd.open_workbook(file_path)
    sheetName = workbook.sheet_by_name(case_sheet_name)
    for row in range(1,2):
        for col in (7,8):
            return  sheetName.row(i)[7].value

def getVariableKeyList(file_path, variable_sheet_name):
    keyList = []
    workbook = xlrd.open_workbook(file_path)
    sheetName = workbook.sheet_by_name(variable_sheet_name)
    for row in range(1, sheetName.nrows):
        for col in range(1, sheetName.ncols):
            if "$" in str(sheetName.row(row)[col].value):
                keyList.append(sheetName.row(row)[col].value)
    return keyList

def setVariableDict(file_path, variable_sheet_name):
    dataDict = {}
    workbook = xlrd.open_workbook(file_path)
    sheetName = workbook.sheet_by_name(variable_sheet_name)
    for row in range(1, sheetName.nrows):
        for col in range(1, sheetName.ncols):
            if "$" in str(sheetName.row(row)[col].value) and (isinstance(sheetName.row(row)[col + 1].value, float)):
                dataDict[sheetName.row(row)[col].value] = str(int(sheetName.row(row)[col + 1].value))
            elif "$" in str(sheetName.row(row)[col].value):
                dataDict[sheetName.row(row)[col].value] = str(sheetName.row(row)[col + 1].value)
    return dataDict
