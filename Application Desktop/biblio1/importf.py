# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
import pandas as pd
import pymongo
from PyQt5 import QtWidgets


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["Employee"]
#collection 
importation =db["Importation"] 
collection_list = db.collection_names()

class Ui_Form(object):

    def loadExcelData(self, excel_file_dir, worksheet_name):
        if ("Importation" in collection_list) :
            print(" collection  existe")
            msg = QMessageBox()
            msg.setWindowTitle("IMPORT")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Already Exist")
            retval = msg.exec_() 
        else:
            print("The collection doesn't exist.")
            df = pd.read_excel(excel_file_dir, worksheet_name, engine='openpyxl')
            df_dict = df.to_dict("records")
            # Insert collection
            importation.insert_many(df_dict)
            msg = QMessageBox()
            msg.setWindowTitle("IMPORT")
            msg.setIcon(QMessageBox.Information)
            msg.setText("Data Import Successfully")
            retval = msg.exec_() 

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 120, 151, 51))
        self.pushButton.setStyleSheet("font: 11pt \"Rockwell\";\n"
"background-color: rgb(170, 85, 255);")
        self.pushButton.setObjectName("pushButton")

        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.pushButton.setText(_translate("Form", "I M P O R T"))
        self.pushButton.clicked.connect(lambda _, xl_path='C:\\Users\\LENOVO\\Desktop\\atelier\\biblio1\\DataBase.xlsx', sheet_name='Sheet1': self.loadExcelData(xl_path, sheet_name))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
