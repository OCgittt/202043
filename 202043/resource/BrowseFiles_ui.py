# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BrowseFiles.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(367, 262)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(2, 22, 361, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 0, 1, 1, 1)
        self.filename_LineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.filename_LineEdit.setText("")
        self.filename_LineEdit.setObjectName("filename_LineEdit")
        self.gridLayout.addWidget(self.filename_LineEdit, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(129, 112, 108, 143))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.statistics_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.statistics_btn.setObjectName("statistics_btn")
        self.verticalLayout.addWidget(self.statistics_btn)
        self.save_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout.addWidget(self.save_btn)
        self.analyze_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.analyze_btn.setObjectName("analyze_btn")
        self.verticalLayout.addWidget(self.analyze_btn)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.draw_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.draw_btn.setObjectName("draw_btn")
        self.verticalLayout_2.addWidget(self.draw_btn)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(37, 70, 294, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.database_name_LineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.database_name_LineEdit.setObjectName("database_name_LineEdit")
        self.gridLayout_3.addWidget(self.database_name_LineEdit, 0, 1, 1, 1)
        self.creat_database_btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.creat_database_btn.setObjectName("creat_database_btn")
        self.gridLayout_3.addWidget(self.creat_database_btn, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(253, 211, 111, 41))
        self.label_3.setStyleSheet("\n"
"font: 11pt \"楷体\";\n"
"\n"
"text-decoration: underline;")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        self.toolButton.clicked.connect(Form.browse_files)
        self.statistics_btn.clicked.connect(Form.statistics_file)
        self.analyze_btn.clicked.connect(Form.analyze_file)
        self.save_btn.clicked.connect(Form.save_data)
        self.draw_btn.clicked.connect(Form.paint_draw)
        self.creat_database_btn.clicked.connect(Form.create_database)
        self.database_name_LineEdit.textChanged['QString'].connect(Form.get_dbname)
        self.pushButton.clicked.connect(Form.save_cloud)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "浏览文件"))
        self.toolButton.setText(_translate("Form", "..."))
        self.statistics_btn.setText(_translate("Form", "开始统计文件数据"))
        self.save_btn.setText(_translate("Form", "开始导入保存数据"))
        self.analyze_btn.setText(_translate("Form", "开始导出文件数据"))
        self.pushButton.setText(_translate("Form", "导出到云端"))
        self.draw_btn.setText(_translate("Form", "开始作图"))
        self.label_2.setText(_translate("Form", "输入数据库名"))
        self.creat_database_btn.setText(_translate("Form", "创建数据库"))
        self.label_3.setText(_translate("Form", "By Leus DD OC"))
