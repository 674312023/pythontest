# coding:utf-8
import xlrd

# data = xlrd.open_workbook('testdata.xlsx')
# table = data.sheet_by_name('Sheet1')
# nrows = table.nrows
# ncols = table.ncols
# print(table.row_values(0))
# print(table.col_values(0))

class Xlsxtest():
    def __init__(self, excelpath, sheetname):
        self.data = xlrd.open_workbook(excelpath)
        self.table = self.data.sheet_by_name(sheetname)
        # 获取第一行作为 key 值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        #获取总列数
        self.colNum = self.table.ncols
        print(self.keys)

    def dict_data(self):
        if self.rowNum <=1:
            print('总行数小于等于1行')
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                # 从第二行开始取对应 values 值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]]=values[x]
                r.append(s)
                j+=1

            return r

if __name__ == '__main__':
    filepath = r'D:\pythontest\jiekou\6-1\testdata.xlsx'
    sheetname = 'Sheet1'
    data = Xlsxtest(filepath,sheetname)
    print(data.dict_data())
