import xlwt, xlrd
from openpyxl import load_workbook
from xlutils.copy import copy


class WriteExcel:
    def writeExcel(file_path, sheetName, rowId, colId, content, fontColor):
        workbook = xlrd.open_workbook(file_path, formatting_info=True)
        wt = copy(workbook)
        wt.get_sheet(sheetName).write(rowId, colId, content, fontColor)
        wt.save(file_path)

    def test(self):
        list1 = ["abc", "d", "ef"]
        print(list1.index("ef"))


if __name__ == "__main__":
    # WriteExcel().writeExcel("../excelData/test_case.xlsx","登录用例",1,5,"test")
    WriteExcel().test()
