# -*-coding: utf-8 -*-
import os
import re
from tkinter import *  # 选择文件使用
import tkinter.filedialog  # 选择文件使用
import tkinter.messagebox  # 弹窗
import pandas as pd  # 分析excel使用
import pymysql  # 连接数据库，数据库操作使用
import xlrd  # 获取数据库表名类型使用
import webbrowser  # 通过默认浏览器访问指定网页
from time import strftime, gmtime
import csv
import array  # 获取数据库表名类型使用
import numpy as np


class processing_data(object):
    global filename
    filename = ""
    global db_name
    db_name = ""
    global cursor

    #     选择文件
    def browse_files(self):
        global filename
        print("选择文件")
        root = Tk()  # 创建一个tkinter.Tk()实例
        root.withdraw()  # 将Tkinter.Tk()实例隐藏
        default_dir = r"C:\Users"  # 定义初始位置

        filename = tkinter.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(default_dir)))
        if filename.endswith('.xlsx'):
            self.filename_LineEdit.setText(filename)
            db_name = filename.split('/')[-1]
        else:
            self.filename_LineEdit.setText("只能选择.xlsx文件类型，或您未选择文件")

    #     统计excel数据
    def statistics_file(self):  # 统计
        global filename
        root = Tk()
        root.withdraw()
        print(filename)

        if filename != "":
            print("开始统计")
            print(filename)
            df = pd.read_excel(filename)
            print("完成统计", filename)
            data_count = df.shape
            print("一共有 %s 行 %s 列数据" % (data_count[0], data_count[1]))
            print(df.head(5))
            res_count = '该文件一共有'+str(data_count[0])+'行'+str(data_count[1])+'列数据'
            try:
                tkinter.messagebox.showinfo('提示', res_count)
            except :
                pass
        else:
            print("请选择文件")
            tkinter.messagebox.showwarning('警告', '请先选择文件')

    #     数据库连接
    def db_conn(self):
        try:
            self.conn = pymysql.connect(host='120.24.219.85', port=3309, user='root', password='123456', charset='gbk',
                                        local_infile=1)
            self.cursor = self.conn.cursor()
            return self.conn
        except:
            tkinter.messagebox.showerror('错误', '数据库连接错误')
            print("连接数据库报错！！！")
            return 0

    #     获取库名
    def get_dbname(self):
        global db_name
        print("获取db_name")
        db_name = self.database_name_LineEdit.text()  # 获取输入的字符传到db_name
        print(db_name)

    #     创建数据库
    def create_database(self):
        root = Tk()
        root.withdraw()
        global db_name
        print("创建数据库存储数据")
        if db_name == '':
            print("请输入数据库名")
            tkinter.messagebox.showwarning('警告', '请输入数据库名')
            pass
        else:
            conn_res = processing_data.db_conn(self)
            if conn_res != 0:
                sql_create = "create database " + db_name + " character set gbk;"
                try:
                    self.cursor.execute(sql_create)  # 游标
                    tkinter.messagebox.showinfo('提示', '创建数据库成功')
                except:
                    print("已有该数据库名称或数据库名包含特殊符号")
                    tkinter.messagebox.showwarning('警告', '数据库名已存在或数据库命包含中文等特殊符号,请更换数据库名')
                    pass
                self.cursor.execute("show databases")
                print(self.cursor.fetchall())  # 输出查询结果
                self.cursor.close()  # 关闭光标
                self.conn.close()  # 关闭数据库连接
                # try:
                #     conn = pymysql.connect(host = 'localhost', user = 'root', password = 'root', charset = 'utf8')
                #     cursor = conn.cursor()
                #     sql_create = "create database " + db_name + ";"
                #
                #     cursor.execute(sql_create) #游标
                #     cursor.execute("show databases")
                #     print(cursor.fetchall()) #输出查询结果
                # except:
                #     print("连接数据库报错了！！！")
            else:
                pass

    #     获取数据库表名类型
    def tb_name(self):
        try:
            print("获取表名")
            file = filename
            path = os.path.dirname(file)
            print('path路径为： ' + path)
            # name_csv = file.split('/')[-1].split('.')[0]    #规定csv文件名前缀
            self.sql_create_all = []  # 创建表的语句数据
            data = xlrd.open_workbook(file)  # 打开excel文件
            self.name_sheet = data.sheet_names()  # 返回excel中所有sheet的名字
            for i in self.name_sheet:
                # print('1')
                data_xl = pd.read_excel(data, i, index_col=0, skiprows={0})
                # print(data_xl)
                data_xl.to_csv(path + '/' + i + '.csv', encoding='gbk')  # 转码获得csv文件，方便导入到数据库
                # print('3')
                sql_create = 'create table ' + i + '( name varchar(20), value int(11), date datetime ) engine=innodb default charset=gbk;'
                self.sql_create_all.append(sql_create)
        except:
            pass
        # row = 1  # 选取第几行数据  115
        # file = filename
        # j = 1
        # self.sql_creat_all = []                  # 创建表语句的数组
        # print(file)
        # data = xlrd.open_workbook(file)     # 打开excel文件
        # self.name_sheet = data.sheet_names()     # 返回excel中所有sheet的名字
        # for i in self.name_sheet:
        #     print(i)
        #     sql_creat = 'create table ' + i + ' ( '
        #     table = data.sheet_by_name(i)
        #     len = table.row_len(row)  # 返回该行的有效单元格长度
        #     types = table.row_types(row, start_colx=0, end_colx=None) # 返回由该行中所有单元格的数据类型组成的列表  从零开始
        #     for k in range(len):
        #         type = types[k]
        #         k+=1
        #         col_name = 'column' + str(k)
        #         if type == 1:
        #             type = 'text'
        #         else:
        #             if type == 2:
        #                 type = 'float'
        #             else:
        #                 if type == 3:
        #                     type = 'datetime'
        #         print('类型type为 : '+type)
        #         sql_creat = sql_creat + col_name + ' ' + type + ', '    # 结尾多了个逗号
        #
        #     sql_creat = sql_creat.strip(", ")  # 去掉右边最后的逗号和空格
        #     sql_creat = sql_creat + ') default charset=utf8;'
        #     print(sql_creat)
        #     self.sql_creat_all.append(sql_creat)
        #     j+=1
        #     print(self.sql_creat_all)

    #     将excel导入数据库
    def save_data(self):  # 数据库记录
        global filename
        print("开始记录")
        print("文件路径为" + filename)
        path = os.path.dirname(filename)
        # print(path)
        root = Tk()
        root.withdraw()
        k = 0
        processing_data.tb_name(self)
        conn_res = processing_data.db_conn(self)
        if conn_res != 0:
            try:
                self.cursor.execute('use ' + db_name)
                print(self.sql_create_all)
                for i in self.sql_create_all:
                    self.cursor.execute(i)
                    set_character = "set character_set_client = 'gbk',character_set_connection = 'gbk',character_set_results= 'gbk',character_set_server= 'gbk',character_set_database= 'gbk';"
                    self.cursor.execute(set_character)
                    path_csv = path + '/' + self.name_sheet[k] + '.csv'
                    print(path)
                    sql_save = 'load data local infile "' + path_csv + '" into table ' + self.name_sheet[
                        k] + " fields terminated by ',' lines terminated by '\\n';"  # 编码问题未解决
                    # self.cursor.execute('show tables;')
                    # print(self.cursor.fetchall())
                    print("done")
                    try:
                        self.cursor.execute(sql_save)  # 执行导入数据
                        print("导入成功")
                        tkinter.messagebox.showinfo('提示', '导入成功')
                        print(sql_save)
                    except:
                        info = sys.exc_info()
                        print(info[0], ":", info[1])
                        print("导入失败")
                        tkinter.messagebox.showerror('错误', '导入失败')
                    # try:
                    self.cursor.execute('select*from ' + self.name_sheet[k] + ';')
                    # except:
                    #     info = sys.exc_info()
                    #     print(info[0], ":", info[1])
                    #     print("done2")
                    print('select*from ' + self.name_sheet[k] + ';')
                    k += 1
                    print(self.cursor.fetchall())  # 输出查询结果
                    self.conn.commit()
                    print('2')
            except:
                tkinter.messagebox.showwarning('警告', '请先选择文件或创建数据库')
            self.cursor.close()  # 关闭光标
            self.conn.close()  # 关闭数据库连接


        else:
            pass

    def write_csv(self):
        root = Tk()
        root.withdraw()
        datas = []
        conn_res = processing_data.db_conn(self)
        if conn_res != 0:
            try:
                for i in self.name_sheet:
                    db = db_name
                    tb = i
                    print(db + tb)
                    sql_select = "select name,value,date from " + db + "." + tb + " order by name;"
                    print(sql_select)
                    try:
                        self.cursor.execute(sql_select.encode('gbk'))
                        data = self.cursor.fetchall()
                        print('done')
                    except:
                        info = sys.exc_info()
                        print(info[0], ":", info[1])
                        print("fail")
                    print(data)
                    # try:
                    datas.append(data)
                    # except Exception as e:
                    #     print('repr(e):\t',repr(e))
            except:
                tkinter.messagebox.showwarning('警告', '请先导入文件')
        else:
            print('数据库连接错误')
        self.cursor.close()  # 关闭光标
        self.conn.close()  # 关闭数据库连接
        # print('0')

        # print('1')
        path = os.path.dirname(filename)
        # print('2')
        # print('3')
        z = 1
        try:
            for x in datas:
                print('4')
                now = strftime("%Y%m%d%H%M%S")
                fname = path + "/" + now + str(z) + ".csv"  # r'D:\%s.csv' % now  # 获取当前时间作为文件名
                z += 1
                print('4.1:  ' + fname)
                with open(fname, mode='w', encoding='gbk', newline='') as f:
                    print('5')
                    write = csv.writer(f, dialect='excel')
                    write.writerow(['name', 'value', 'date'])
                    print('6')
                    for item in x:
                        print('7')
                        write.writerow(item)
            # print("文件URL为:" + fname)
            tkinter.messagebox.showinfo('提示', '导出成功,文件名为当前时间'+fname)
        except:
            pass

    def analyze_file(self):  # 分析
        print("开始分析")
        self.write_csv()

    def save_file(self):
        print("保存数据")

    def paint_draw(self):  # 画图
        print("开始画图")
        webbrowser.open("http://www.leus.top:8082/")
        # webbrowser.open("http://show.ocbiu.top:2334/202043/")
        # webbrowser.open("http://show.ocbiu.top:2334/files/")

    def save_cloud(self):  # 保存云端
        print('cloud')
        root = Tk()
        root.withdraw()
        conn_res = processing_data.db_conn(self)
        if conn_res != 0:
            try:
                for i in self.name_sheet:
                    db = db_name
                    tb = i
                    print(db + tb)
                    sql_usedb = "use " + db + ";"
                    # sql_delimiter = r"delimiter $$"
                    sql_dropproc = "DROP PROCEDURE IF EXISTS export;"
                    sql_save_cloud = "create procedure export(IN tb varchar(30))\
                    begin\
                    DECLARE url varchar(300);\
                    select concat(" + "\"select name,value,date into outfile '/var/www/html/files/\",date_format(now(),'%Y%m%d%H%i%s'),\".csv'\",\" character set gbk fields terminated by ',' optionally enclosed by'\",\"\"\"\",\"'escaped by '\",\"\"\"\",\"' lines terminated by '\\r\\n' from (select 'name','value','date' union select name,value,date from \",tb,\")b order by name;\")into url;\
                    set @sql=url;\
                    prepare s1 from @sql;\
                    execute s1;\
                    deallocate prepare s1;\
                    end"

                    # delimiter ;
                    sql_call_export = "call export(" + "\"" + tb + "\"" + ");"

                    try:
                        self.cursor.execute(sql_usedb)
                        # self.cursor.execute(sql_delimiter)
                        self.cursor.execute(sql_dropproc)
                        self.cursor.execute(sql_save_cloud)
                        print(tb)
                        print(type(tb))
                        tb = str(tb)
                        # self.cursor.callproc('export', args=tb)

                        self.cursor.execute(sql_call_export)
                        print("保存成功")
                        tkinter.messagebox.showinfo('提示', '保存成功,文件名为当前时间')
                    except:
                        print("保存到云端失败")
                        tkinter.messagebox.showerror('错误', '保存到云端失败')
                        info = sys.exc_info()
                        print(info[0], ":", info[1])
                        pass
            except:
                tkinter.messagebox.showwarning('警告', '请先导入文件')
        else:
            print("连接数据库失败")
            pass
        self.cursor.close()  # 关闭光标
        self.conn.close()  # 关闭数据库连接

# delimiter $$
# DROP PROCEDURE IF EXISTS export;
# create procedure export(IN tb varchar(30))
# begin
# DECLARE url varchar(300);
# select concat("select * into outfile '/var/www/html/files/",date_format(now(),'%Y%m%d%H%i%s'),".csv'"," character set gbk fields terminated by ',' optionally enclosed by'","""","'escaped by '","""","' lines terminated by '\\r\\n' from (select 'name','value','date' union select name,value,date from ",tb,")b order by name;")into url;
# select url;
# set @sql=url;
# prepare s1 from @sql;
# execute s1;
# deallocate prepare s1;
# end$$
# delimiter ;
