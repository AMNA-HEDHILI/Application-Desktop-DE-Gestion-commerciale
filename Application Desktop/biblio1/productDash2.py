# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productDash2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pymongo import collection
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QTableWidgetItem
import pandas as pd

from typing import Collection, Text
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from pymongo import collection
from pymongo.errors import NotMasterError
import numpy
import pandas as pd
import  pymongo
from pymongo import MongoClient
import sys
#création bd
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["DesktopApp"]
#collection categorie
collectionCategory=db.category


class Ui_MainWindow(object):
    

    def SearchNamecat(self):
                collectionCategory=db.category
                Name=self.catname.text()
                df = pd.DataFrame(list(collectionCategory.find({"Name":Name})))
                if (not(df.empty)):        
                        print (df)
    # Add data from Database
                        self.Category.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                        self.Category.setColumnCount(len(df.columns))
                        self.Category.setRowCount(len(df.index))
                        for i in range(len(df.index)):
                                for j in range(len(df.columns)):
                                                self.Category.setItem(i,j,QTableWidgetItem(str(df.iloc[i, j])))
                else:
                        self.catname.setStyleSheet("background-color: rgb(255, 0, 0);color: rgb(255,255,255);font-size: 9pt")



    def SearchNamesouscat(self):
        collectionSousCategory=db.SubCategory
        Name=self.subid.text()
        dp = pd.DataFrame(list(collectionSousCategory.find({"Name":Name})))
        if (not (dp.empty)):
    # Add data from Database
                self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                self.tableWidget.setColumnCount(len(dp.columns))
                self.tableWidget.setRowCount(len(dp.index))
                for i in range(len(dp.index)):
                        for j in range(len(dp.columns)):
                                self.tableWidget.setItem(i,j,QTableWidgetItem(str(dp.iloc[i, j])))
        else:
                self.subid.setStyleSheet("background-color: rgb(255, 0, 0);color: rgb(255,255,255);font-size: 9pt")

    def SearchNameproduct(self):
        Name=self.proname.text()
        dn = pd.DataFrame(list(db.Product.find({"Name":Name})))
        print(dn)
        if(not(dn.empty)):
    # Add data from Database
                self.tableWidget_2.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                self.tableWidget_2.setColumnCount(len(dn.columns))
                self.tableWidget_2.setRowCount(len(dn.index))
                print(len(dn.index))
                for i in range(len(dn.index)):
                        for j in range(len(dn.columns)):
                              self.tableWidget_2.setItem(i,j,QTableWidgetItem(str(dn.iloc[i, j])))
        else:
                self.proname.setStyleSheet("background-color: rgb(255, 0, 0);color: rgb(255,255,255);font-size: 9pt")

    def ShowAll(self):
                collectionCategory=db.category

                df = pd.DataFrame(list(collectionCategory.find()))
        # Add data from Database
                self.Category.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                self.Category.setColumnCount(len(df.columns))
                self.Category.setRowCount(len(df.index))
                for i in range(len(df.index)):
                        for j in range(len(df.columns)):
                                self.Category.setItem(i,j,QTableWidgetItem(str(df.iloc[i, j])))

                collectionSousCategory=db.SubCategory

                dp = pd.DataFrame(list(collectionSousCategory.find()))
        # Add data from Database
                self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                self.tableWidget.setColumnCount(len(dp.columns))
                self.tableWidget.setRowCount(len(dp.index))
                for i in range(len(dp.index)):
                        for j in range(len(dp.columns)):
                                self.tableWidget.setItem(i,j,QTableWidgetItem(str(dp.iloc[i, j])))

                collectionProduct=db.Product

                dn = pd.DataFrame(list(collectionProduct.find()))
                print(dn)
        # Add data from Database
                self.tableWidget_2.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
                self.tableWidget_2.setColumnCount(len(dn.columns))
                self.tableWidget_2.setRowCount(len(dn.index))
                print(len(dn.index))
                for i in range(len(dn.index)):
                        for j in range(len(dn.columns)):
                                self.tableWidget_2.setItem(i,j,QTableWidgetItem(str(dn.iloc[i, j])))
    def showAllcat(self):
           self.catname.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(0,0,0);font-size: 9pt")

           if (self.catname.text()==""):
                   self.ShowAll()

    def showAllsouscat(self):
           self.subid.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(0,0,0);font-size: 9pt")

           if (self.subid.text()==""):
                   self.ShowAll()



    def showAllpro(self):
           self.proname.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(0,0,0);font-size: 9pt")
           if (self.proname.text()==""):
                   

                   self.ShowAll()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet("    background-color: rgb(34, 76, 132);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(11, 11, 1258, 113))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setSizeIncrement(QtCore.QSize(15, 0))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(3)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Header = QtWidgets.QWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.Header.sizePolicy().hasHeightForWidth())
        self.Header.setSizePolicy(sizePolicy)
        self.Header.setStyleSheet("#Header{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.Header.setObjectName("Header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Header)
        self.horizontalLayout.setContentsMargins(0, 0, 20, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.Header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout.addWidget(self.widget_2)
        self.ShopIcon = QtWidgets.QLabel(self.Header)
        self.ShopIcon.setMinimumSize(QtCore.QSize(50, 50))
        self.ShopIcon.setMaximumSize(QtCore.QSize(50, 50))
        self.ShopIcon.setText("")
        self.ShopIcon.setPixmap(QtGui.QPixmap("../assets/shop.png"))
        self.ShopIcon.setScaledContents(True)
        self.ShopIcon.setObjectName("ShopIcon")
        self.horizontalLayout.addWidget(self.ShopIcon)
        self.Product = QtWidgets.QLabel(self.Header)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Product.setFont(font)
        self.Product.setStyleSheet("#Title{\n"
"    \n"
"    color: rgb(0, 0, 127);\n"
"}")
        self.Product.setObjectName("Product")
        self.horizontalLayout.addWidget(self.Product)
        self.widget_3 = QtWidgets.QWidget(self.Header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout.addWidget(self.widget_3)
        self.Clock = QtWidgets.QLabel(self.Header)
        self.Clock.setMinimumSize(QtCore.QSize(50, 50))
        self.Clock.setMaximumSize(QtCore.QSize(50, 50))
        self.Clock.setText("")
        self.Clock.setPixmap(QtGui.QPixmap("../assets/clock.png"))
        self.Clock.setScaledContents(True)
        self.Clock.setObjectName("Clock")
        self.horizontalLayout.addWidget(self.Clock)
        self.verticalLayout_2.addWidget(self.Header)
        self.AddCategory = QtWidgets.QGroupBox(self.centralwidget)
        self.AddCategory.setGeometry(QtCore.QRect(30, 140, 521, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.AddCategory.sizePolicy().hasHeightForWidth())
        self.AddCategory.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.AddCategory.setFont(font)
        self.AddCategory.setStyleSheet("color: rgb(255, 255, 255);")
        self.AddCategory.setObjectName("AddCategory")
        self.Category = QtWidgets.QTableWidget(self.AddCategory)
        self.Category.setGeometry(QtCore.QRect(40, 110, 381, 121))
        self.Category.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);selection-background-color:rgb(75, 226, 156)")
        self.Category.setObjectName("Category")
        self.Category.setColumnCount(2)
        self.Category.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Category.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Category.setHorizontalHeaderItem(1, item)
        self.layoutWidget = QtWidgets.QWidget(self.AddCategory)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 30, 461, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_4 = QtWidgets.QWidget(self.layoutWidget)
        self.widget_4.setObjectName("widget_4")
        self.layoutWidget1 = QtWidgets.QWidget(self.widget_4)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 11, 277, 24))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.categoryname = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.categoryname.setFont(font)
        self.categoryname.setStyleSheet("    color: rgb(75, 226, 156);\n"
"")
        self.categoryname.setObjectName("categoryname")
        self.horizontalLayout_3.addWidget(self.categoryname)
        self.catname = QtWidgets.QLineEdit(self.layoutWidget1)
        self.catname.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(0,0,0);font-size: 9pt")
        self.catname.setObjectName("catname")
        self.horizontalLayout_3.addWidget(self.catname)
        self.horizontalLayout_5.addWidget(self.widget_4)
        self.searchcat = QtWidgets.QPushButton(self.layoutWidget)
        self.searchcat.setMinimumSize(QtCore.QSize(120, 35))
        self.searchcat.setMaximumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.searchcat.setFont(font)
        self.searchcat.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"color: rgb(0, 0, 0);")
        self.searchcat.setObjectName("searchcat")
        self.horizontalLayout_5.addWidget(self.searchcat)
        self.Addsubcategory = QtWidgets.QGroupBox(self.centralwidget)
        self.Addsubcategory.setGeometry(QtCore.QRect(30, 390, 521, 301))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.Addsubcategory.sizePolicy().hasHeightForWidth())
        self.Addsubcategory.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Addsubcategory.setFont(font)
        self.Addsubcategory.setStyleSheet("    color: rgb(255, 255, 255);\n"
"")
        self.Addsubcategory.setObjectName("Addsubcategory")
        self.widget_7 = QtWidgets.QWidget(self.Addsubcategory)
        self.widget_7.setGeometry(QtCore.QRect(20, 20, 491, 81))
        self.widget_7.setStyleSheet("    color: rgb(75, 226, 156);\n"
"")
        self.widget_7.setObjectName("widget_7")
        self.layoutWidget2 = QtWidgets.QWidget(self.widget_7)
        self.layoutWidget2.setGeometry(QtCore.QRect(12, 12, 471, 71))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.subcatname = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.subcatname.setFont(font)
        self.subcatname.setStyleSheet("#SubCategoryLabel{\n"
"    color: rgb(75, 226, 156);\n"
"}")
        self.subcatname.setObjectName("subcatname")
        self.horizontalLayout_2.addWidget(self.subcatname)
        self.subid = QtWidgets.QLineEdit(self.layoutWidget2)
        self.subid.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(0,0,0);font-size: 9pt")
        self.subid.setObjectName("subid")
        self.horizontalLayout_2.addWidget(self.subid)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.searchsub = QtWidgets.QPushButton(self.layoutWidget2)
        self.searchsub.setMinimumSize(QtCore.QSize(120, 35))
        self.searchsub.setMaximumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.searchsub.setFont(font)
        self.searchsub.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"color: rgb(0, 0, 0);")
        self.searchsub.setObjectName("searchsub")
        self.horizontalLayout_6.addWidget(self.searchsub)
        self.tableWidget = QtWidgets.QTableWidget(self.Addsubcategory)
        self.tableWidget.setGeometry(QtCore.QRect(30, 120, 391, 161))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);selection-background-color:rgb(75, 226, 156)")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.ProductManage = QtWidgets.QGroupBox(self.centralwidget)
        self.ProductManage.setGeometry(QtCore.QRect(570, 140, 681, 551))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.ProductManage.sizePolicy().hasHeightForWidth())
        self.ProductManage.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ProductManage.setFont(font)
        self.ProductManage.setStyleSheet("    color: rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"")
        self.ProductManage.setFlat(False)
        self.ProductManage.setCheckable(False)
        self.ProductManage.setObjectName("ProductManage")
        self.searchpro = QtWidgets.QPushButton(self.ProductManage)
        self.searchpro.setGeometry(QtCore.QRect(360, 70, 120, 35))
        self.searchpro.setMinimumSize(QtCore.QSize(120, 35))
        self.searchpro.setMaximumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.searchpro.setFont(font)
        self.searchpro.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"color: rgb(0, 0, 0);")
        self.searchpro.setObjectName("searchpro")
        self.widget_9 = QtWidgets.QWidget(self.ProductManage)
        self.widget_9.setGeometry(QtCore.QRect(20, 40, 331, 101))
        self.widget_9.setStyleSheet("    color: rgb(75, 226, 156);\n"
"")
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.productname = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.productname.setFont(font)
        self.productname.setStyleSheet("#SubCategoryLabel{\n"
"    color: rgb(75, 226, 156);\n"
"}")
        self.productname.setObjectName("productname")
        self.horizontalLayout_4.addWidget(self.productname)
        self.proname = QtWidgets.QLineEdit(self.widget_9)
        self.proname.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(0,0,0);font-size: 9pt")
        self.proname.setObjectName("proname")
        self.horizontalLayout_4.addWidget(self.proname)
        self.searchpro_2 = QtWidgets.QPushButton(self.ProductManage)
        self.searchpro_2.setGeometry(QtCore.QRect(490, 70, 120, 35))
        self.searchpro_2.setMinimumSize(QtCore.QSize(120, 35))
        self.searchpro_2.setMaximumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.searchpro_2.setFont(font)
        self.searchpro_2.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"color: rgb(0, 0, 0);")
        self.searchpro_2.setObjectName("searchpro_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.ProductManage)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 150, 621, 341))
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);selection-background-color:rgb(75, 226, 156)")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    """def SearchCategory(self):
        # get text
        collectionCategory=connexion.db.Category
            
        texte=self.catname.text()
        print(texte)
            # search
        result = collectionCategory.find_one({"Name" :texte})
        if( result == None):
                QMessageBox.about(self, "ERROR", "No Result Found")
        else:
                print(result) 
                
        
        df = pd.DataFrame(list(collectionCategory.find()))
        rslt=df.loc[df['Name'] == texte]
        self.Category.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.Category.setColumnCount(len(rslt.columns))
        self.Category.setRowCount(len(rslt.index))
        for i in range(len(rslt.index)):
            for j in range(len(rslt.columns)):
                self.Category.setItem(i,j,QTableWidgetItem(str(rslt.iloc[i, j])))
        """

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Product.setText(_translate("MainWindow", "Product Management"))
        self.AddCategory.setTitle(_translate("MainWindow", " Category"))
        item = self.Category.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Category_ID"))
        item = self.Category.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        self.categoryname.setText(_translate("MainWindow", "Category Name"))
        self.searchcat.setText(_translate("MainWindow", "Search"))
        self.Addsubcategory.setTitle(_translate("MainWindow", "Add Sub Category"))
        self.subcatname.setText(_translate("MainWindow", "Sub Category Name"))
        self.searchsub.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sub Category ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Category iD"))
        self.ProductManage.setTitle(_translate("MainWindow", "Product Manage"))
        self.searchpro.setText(_translate("MainWindow", "Search"))
        self.productname.setText(_translate("MainWindow", "Product Name"))
        self.searchpro_2.setText(_translate("MainWindow", "Show All"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product_ID"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Category_ID"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Sub_Category_ID"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cost_Price"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Selling_Price"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Quantity"))
        self.ShowAll()
        self.catname.textChanged.connect(self.showAllcat)
        self.subid.textChanged.connect(self.showAllsouscat)
        self.proname.textChanged.connect(self.showAllpro)
        self.searchcat.clicked.connect(self.SearchNamecat)
        self.searchsub.clicked.connect(self.SearchNamesouscat)
        self.searchpro.clicked.connect(self.SearchNameproduct)
        self.searchpro_2.clicked.connect(self.ShowAll)
 

if __name__ == "__main__":
    import sys        

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
