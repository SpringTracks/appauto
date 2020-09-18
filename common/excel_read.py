from xlrd import open_workbook

def getExcelTestData(sheetName):
    openExcelFile = open_workbook("./testcase/testdata_location.xlsx")
    # 打开Excel文件
    getSheet = openExcelFile.sheet_by_name(sheetName)
    # 获取工作表
    rowNumber = getSheet.nrows
    # 获取行数
    dataList = []
    # 数据List
    for i in range(1, rowNumber):
        # 从第二行开始遍历每一行
        dataList.append(getSheet.row_values(i))
        # 把每个单元格的数值存放到dataList中
    return dataList