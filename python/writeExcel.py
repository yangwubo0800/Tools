import xlwt
import os
import xlrd

# excel的存放路径
excel_path = r'C:\Users\DELL\Desktop\teenager.xls'


class ExcelWrite(object):
    def __init__(self):
        self.excel = xlwt.Workbook()  # 创建一个工作簿
        self.sheet = self.excel.add_sheet('Sheet1')  # 创建一个工作表

    # 写入单个值
    def write_value(self, cell, value):
        '''
            - cell: 传入一个单元格坐标参数，例如：cell=(0,0),表示修改第一行第一列
        '''
        self.sheet.write(*cell, value)
        # （覆盖写入）要先用remove(),移动到指定路径，不然第二次在同一个路径保存会报错
        os.remove(excel_path)
        self.excel.save(excel_path)

    # 写入多个值
    def write_values(self, cells, values):
        '''
            - cells: 传入一个单元格坐标参数的list，
            - values: 传入一个修改值的list，
            例如：cells = [(0, 0), (0, 1)],values = ('a', 'b')
            表示将列表第一行第一列和第一行第二列，分别修改为 a 和 b
        '''
        # 判断坐标参数和写入值的数量是否相等
        if len(cells) == len(values):
            for i in range(len(values)):
                self.write_value(cells[i], values[i])
        else:
            print("传参错误,单元格：%i个,写入值：%i个" % (len(cells), len(values)))


if __name__ == '__main__':
    # 打开Excel表格
    data = xlrd.open_workbook("students.xlsx")
    # 获取目标EXCEL文件sheet名
    print(data.sheet_names())
    # 取出青少表
    teenager = data.sheet_by_index(2)


    # 名字
    names = teenager.col_values(0, 1)
    print(names)
    # names = list(filter(None, names))
    # print(names)

    # 班号
    classNo = teenager.col_values(2, 1)
    # print(classNo)
    # classNo = list(filter(None, classNo))

    # 电话号码
    phoneNo = teenager.col_values(12, 1)
    print(phoneNo)
    # phoneNo = list(filter(None, phoneNo))

    # 主课
    mainCourse = teenager.col_values(4, 1)
    print(mainCourse)
    mainCourseConvert = []
    for course in mainCourse:
        index = course.find('上')
        mainCourseConvert.append(course[index+1:])
    print(mainCourseConvert)

    # 特色课
    CharacterCourse = teenager.col_values(19, 1)
    print(CharacterCourse)

    #授课老师
    teacher = teenager.col_values(5, 1)
    print(teacher)

    #班级名称
    className = teenager.col_values(2, 1)
    print(className)

    #主课课时
    mainCourseHour =teenager.col_values(15, 1)
    print(mainCourseHour)

    #特色课课时
    characterCourseHour =teenager.col_values(16, 1)
    print(characterCourseHour)

    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('teenager')
    #插入第一行标题
    worksheet.write(0, 0, '序号')
    worksheet.write(0, 1, '校区')
    worksheet.write(0, 2, '学生姓名')
    worksheet.write(0, 3, '电话号码')
    worksheet.write(0, 4, '课程类型')
    worksheet.write(0, 5, '目前所读课程名称')
    worksheet.write(0, 6, '授课老师')
    worksheet.write(0, 7, '目前所读班级名称')
    worksheet.write(0, 8, '总课时')

    count = len(names);
    print(count)
    for i in range(count):
        #print(names[i])
        if len(names[i]) != 0:
            worksheet.write(2 * i + 1, 0, i+1)
            worksheet.write(2 * i + 1, 1, 'XX校区')
            worksheet.write(2 * i + 2, 1, 'XX校区')
            worksheet.write(2*i+1, 2, names[i])
            worksheet.write(2*i+1, 3, phoneNo[i])
            worksheet.write(2*i+1, 4, '主课')
            worksheet.write(2*i+2, 4, '特色课')
            worksheet.write(2*i+1, 5, mainCourseConvert[i])
            worksheet.write(2*i+2, 5, CharacterCourse[i])
            worksheet.write(2*i+1, 6, teacher[i])
            worksheet.write(2*i+1, 7, className[i])
            worksheet.write(2*i+1, 8, mainCourseHour[i])
            worksheet.write(2*i+2, 8, characterCourseHour[i])

    workbook.save(excel_path)

    # start = ExcelWrite()
    # cells1 = [(0, 0), (0, 1)]
    # values1 = ('飞猪', '哈哈')
    # start.write_values(cells1, values1)