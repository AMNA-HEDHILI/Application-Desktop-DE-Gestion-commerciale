# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Employee_management.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import pymongo
from pymongo import MongoClient
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QMessageBox
from itertools import product
from typing import Collection, Text
from PyQt5 import QtCore, QtGui, QtWidgets
from pymongo import collection
from pymongo.errors import NotMasterError


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["Employee"]
#collection 
collection_Employee=db["Employee"]
class Ui_Dialog(object):




    def Ajout_Employee(self):
        id =self.idemployee.text()
        nom = self.name.text()
        adresse = self.adresse.text()
        contactNo = self.contact.text()
        email = self.email.text()
        password = self.password.text()
        Proof_ID = self.proofid.currentText()
        Gender = self.gender.currentText()
        Designation =self.designation.currentText()       
        collection_Employee=db.Employee
        Employee_1 ={ "_id": id,"Name":nom,"Contact No":contactNo,"Adresse": adresse,"Email":email,"Password":password,"Designation":Designation,"Gender":Gender,"Proof of ID":Proof_ID}
        collection_Employee.insert_one(Employee_1)
        msg = QMessageBox()
        msg.setWindowTitle("Employee")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Record save successfully")
        retval = msg.exec_()  
                
   
    def Update(self):
        id =self.idemployee.text()
        nom = self.name.text()
        adresse = self.adresse.text()
        contactNo = self.contact.text()
        email = self.email.text()
        password = self.password.text()
        Proof_ID = self.proofid.currentText()
        Gender = self.gender.currentText()
        Designation =self.designation.currentText()
        collection_Employee=db.Employee
        collection_Employee.find_one({"_id":str(id)})
        if( (id != "") and (nom != "") and (adresse != "") and (contactNo != "") and (email != ""))and (password != "") :
            
            newvalues = { "$set":  { "_id":id,"Name": nom,"Adresse":adresse ,"Cantact No": contactNo,"Email": email,"Password":password} }
            collection_Employee.update_one( {'_id':id},newvalues)
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setIcon(QMessageBox.Information)
            msg.setText("Recoed update succefully")
            retval = msg.exec_()

        else:
                msg = QMessageBox()
                msg.setWindowTitle("ERROR")
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Please fill the required fields")
                retval = msg.exec_()  

            
  
    def Delete_Employee(self):
        id =self.idemployee.text()
        nom = self.name.text()
        adresse = self.adresse.text()
        contactNo = self.contact.text()
        email = self.email.text()
        password = self.password.text()
        Proof_ID = self.proofid.currentText()
        proof = self.drivelic.Text()
        Gender = self.gender.currentText()
        Designation =self.designation.currentText()
        collection_Employee=db.Employee
        if( (id != "") and (nom != "") and (adresse != "") and (contactNo != "")  and (email != ""))and (password != ""):
            # delete
            collection_Employee.delete_one({
                                "_id": id,
                                "Name":nom,
                                "Contact No":contactNo,
                                "Adresse": adresse,
                                "Email":email,
                                "Password":password,
                                "Designation":Designation,
                                "Gender":Gender,
                                "Proof of ID":Proof_ID,
                                "proof": proof

                        })
            msg = QMessageBox()
            msg.setWindowTitle("Employee")
            msg.setIcon(QMessageBox.Information)
            msg.setText("Recoed delete succefully")
            retval = msg.exec_()
               
             
        else:
           msg = QMessageBox()
           msg.setWindowTitle("ERROR")
           msg.setIcon(QMessageBox.Critical)
           msg.setText("Please fill the required fields")
           retval = msg.exec_()
   
    def Search(self):
            
           
            collection_Employee=db.Employee
            
            
            if ( self.searchid.text() != ""):
                    Employee_id =self.searchid.text()
                    result = collection_Employee.find_one({"_id":str(Employee_id)})
                    if(result==None):
                            msg = QMessageBox()
                            msg.setWindowTitle("ERROR")
                            msg.setIcon(QMessageBox.Critical)
                            msg.setText(" No result found")
                            retval = msg.exec_()
                    else:
                        
                            msg = QMessageBox()
                            msg.setWindowTitle("Search")
                            msg.setIcon(QMessageBox.Information)
                            msg.setText("Record Found : \n\n"+str((result)))
                            retval = msg.exec_()
                            listeEmp =list(collection_Employee.find({"_id":str(Employee_id)}))
                            self.name.setText(listeEmp[0]['Name'])
                            self.idemployee.setText(listeEmp[0]['_id'])
                            self.adresse.setText(listeEmp[0]['Adresse'])
                            self.contact.setText(listeEmp[0]['Contact No'])
                            self.email.setText(listeEmp[0]['Email'])
                            self.password.setText(listeEmp[0]['Password'])
                            self.gender.setCurrentText(listeEmp[0]['Gender'])
                            self.designation.setCurrentText(listeEmp[0]['Designation'])
                            self.proofid.setCurrentText(listeEmp[0]['Proof of ID'])
                            
                            
            else:
                    msg = QMessageBox()
                    msg.setWindowTitle("ERROR")
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Please fill the required fields")
                    retval = msg.exec_()

   
    def Clear_Employee(self):
        self.idemployee.clear()
        self.contact.clear()
        self.email.clear()
        self.password.clear()
        self.gender.setCurrentIndex(0)
        self.proofid.setCurrentIndex(0)
        self.designation.setCurrentIndex(0)
        self.name.clear()
        self.adresse.clear()
        self.searchid.clear()
    def selectionchange(self):
            choix = self.proofid.currentText()
            if (choix == "PAN Card"):
                    self.stackedWidget.setCurrentWidget(self.PAN)
            elif (choix == "DrivelicenceNo"):
                    self.stackedWidget.setCurrentWidget(self.DriveLic)
            elif (choix == "Adhar Card"):
                    self.stackedWidget.setCurrentWidget(self.Adhar)



                    
        

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.setEnabled(True)
        Dialog.resize(1300, 720)
        Dialog.setMinimumSize(QtCore.QSize(1300, 0))
        Dialog.setMaximumSize(QtCore.QSize(1280, 720))
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setStyleSheet("\n"
"background-color:rgb(32, 74, 135);\n"
"")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 20, 821, 51))
        self.label.setMinimumSize(QtCore.QSize(821, 51))
        self.label.setMaximumSize(QtCore.QSize(821, 16777215))
        self.label.setStyleSheet("background:rgb(52, 101, 164);\n"
"font: 75 24pt \"URW Bookman L\";color:rgb(237, 212, 0);")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(260, 90, 711, 121))
        self.groupBox.setStyleSheet("color:black;\n"
"font: 57 11pt \"Ubuntu\";")
        self.groupBox.setObjectName("groupBox")
        self.search = QtWidgets.QPushButton(self.groupBox)
        self.search.setGeometry(QtCore.QRect(520, 50, 181, 31))
        self.search.setStyleSheet("background:rgb(211, 215, 207);\n"
"color:black;")
        self.search.setObjectName("search")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(33, 127, 148);\n"
"font: 13pt \"URW Bookman L\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.searchid = QtWidgets.QLineEdit(self.groupBox)
        self.searchid.setGeometry(QtCore.QRect(200, 50, 261, 31))
        self.searchid.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.searchid.setObjectName("searchid")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(190, 230, 501, 381))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setMouseTracking(True)
        self.label_4.setStyleSheet("color:rgb(103, 155, 99);\n"
"\n"
"font: 13pt \"URW Bookman L\";\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setMouseTracking(True)
        self.label_5.setStyleSheet("color:rgb(103, 155, 99);\n"
"\n"
"font: 13pt \"URW Bookman L\";\n"
"\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 171, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setMouseTracking(True)
        self.label_6.setStyleSheet("color:rgb(103, 155, 99);\n"
"\n"
"font: 13pt \"URW Bookman L\";\n"
"\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(20, 120, 151, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setMouseTracking(True)
        self.label_7.setStyleSheet("color:rgb(103, 155, 99);\n"
"\n"
"font: 13pt \"URW Bookman L\";\n"
"\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(20, 220, 151, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setMouseTracking(True)
        self.label_8.setStyleSheet("color:rgb(103, 155, 99);\n"
"\n"
"font: 13pt \"URW Bookman L\";\n"
"\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(20, 270, 151, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setMouseTracking(True)
        self.label_9.setStyleSheet("color:rgb(103, 155, 99);\n"
"\n"
"font: 13pt \"URW Bookman L\";\n"
"\n"
"")
        self.label_9.setObjectName("label_9")
        self.gender = QtWidgets.QComboBox(self.frame_2)
        self.gender.setGeometry(QtCore.QRect(210, 170, 261, 31))
        self.gender.setStyleSheet("background:rgb(211, 215, 207);")
        self.gender.setObjectName("gender")
        self.gender.addItem("")
        self.gender.addItem("")
        self.proofid = QtWidgets.QComboBox(self.frame_2)
        self.proofid.setGeometry(QtCore.QRect(210, 270, 261, 31))
        self.proofid.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.proofid.setObjectName("proofid")
        self.proofid.addItem("")
        self.proofid.addItem("")
        self.proofid.addItem("")
        self.contact = QtWidgets.QLineEdit(self.frame_2)
        self.contact.setGeometry(QtCore.QRect(210, 121, 261, 31))
        self.contact.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contact.setObjectName("contact")
        self.name = QtWidgets.QLineEdit(self.frame_2)
        self.name.setGeometry(QtCore.QRect(210, 70, 261, 31))
        self.name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name.setObjectName("name")
        self.idemployee = QtWidgets.QLineEdit(self.frame_2)
        self.idemployee.setGeometry(QtCore.QRect(210, 20, 261, 31))
        self.idemployee.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.idemployee.setObjectName("idemployee")
        self.adresse = QtWidgets.QLineEdit(self.frame_2)
        self.adresse.setGeometry(QtCore.QRect(210, 220, 261, 31))
        self.adresse.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.adresse.setObjectName("adresse")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 300, 501, 80))
        self.stackedWidget.setObjectName("stackedWidget")
        self.vide = QtWidgets.QWidget()
        self.vide.setObjectName("vide")
        self.stackedWidget.addWidget(self.vide)
        self.PAN = QtWidgets.QWidget()
        self.PAN.setObjectName("PAN")
        self.pan = QtWidgets.QLineEdit(self.PAN)
        self.pan.setGeometry(QtCore.QRect(210, 20, 261, 31))
        self.pan.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pan.setObjectName("pan")
        self.label_10 = QtWidgets.QLabel(self.PAN)
        self.label_10.setGeometry(QtCore.QRect(20, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setMouseTracking(True)
        self.label_10.setStyleSheet("color:rgb(103, 155, 99);\n"
"\n"
"font: 13pt \"URW Bookman L\";\n"
"\n"
"")
        self.label_10.setObjectName("label_10")
        self.stackedWidget.addWidget(self.PAN)
        self.DriveLic = QtWidgets.QWidget()
        self.DriveLic.setObjectName("DriveLic")
        self.label_14 = QtWidgets.QLabel(self.DriveLic)
        self.label_14.setGeometry(QtCore.QRect(20, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setMouseTracking(True)
        self.label_14.setStyleSheet("color:rgb(103, 155, 99);\n"
"\n"
"font: 13pt \"URW Bookman L\";\n"
"\n"
"")
        self.label_14.setObjectName("label_14")
        self.drivelic = QtWidgets.QLineEdit(self.DriveLic)
        self.drivelic.setGeometry(QtCore.QRect(210, 20, 261, 31))
        self.drivelic.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.drivelic.setObjectName("drivelic")
        self.stackedWidget.addWidget(self.DriveLic)
        self.Adhar = QtWidgets.QWidget()
        self.Adhar.setObjectName("Adhar")
        self.adhar = QtWidgets.QLineEdit(self.Adhar)
        self.adhar.setGeometry(QtCore.QRect(210, 20, 261, 31))
        self.adhar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.adhar.setObjectName("adhar")
        self.label_15 = QtWidgets.QLabel(self.Adhar)
        self.label_15.setGeometry(QtCore.QRect(20, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setMouseTracking(True)
        self.label_15.setStyleSheet("color:rgb(103, 155, 99);\n"
"\n"
"font: 13pt \"URW Bookman L\";\n"
"\n"
"")
        self.label_15.setObjectName("label_15")
        self.stackedWidget.addWidget(self.Adhar)
        self.frame_6 = QtWidgets.QFrame(Dialog)
        self.frame_6.setGeometry(QtCore.QRect(720, 230, 441, 381))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_11 = QtWidgets.QLabel(self.frame_6)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setMouseTracking(True)
        self.label_11.setStyleSheet("color:rgb(103, 155, 99);\n"
"\n"
"font: 13pt \"URW Bookman L\";\n"
"\n"
"")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_6)
        self.label_12.setGeometry(QtCore.QRect(10, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setMouseTracking(True)
        self.label_12.setStyleSheet("color:rgb(103, 155, 99);\n"
"\n"
"font: 13pt \"URW Bookman L\";\n"
"\n"
"")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        self.label_13.setGeometry(QtCore.QRect(10, 120, 151, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setMouseTracking(True)
        self.label_13.setStyleSheet("color:rgb(103, 155, 99);\n"
"\n"
"font: 13pt \"URW Bookman L\";\n"
"\n"
"")
        self.label_13.setObjectName("label_13")
        self.designation = QtWidgets.QComboBox(self.frame_6)
        self.designation.setGeometry(QtCore.QRect(160, 120, 261, 31))
        self.designation.setStyleSheet("background:rgb(211, 215, 207);")
        self.designation.setObjectName("designation")
        self.designation.addItem("")
        self.designation.addItem("")
        self.designation.addItem("")
        self.email = QtWidgets.QLineEdit(self.frame_6)
        self.email.setGeometry(QtCore.QRect(160, 20, 261, 31))
        self.email.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(self.frame_6)
        self.password.setGeometry(QtCore.QRect(160, 70, 261, 31))
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setObjectName("password")
        self.add = QtWidgets.QPushButton(Dialog)
        self.add.setGeometry(QtCore.QRect(200, 640, 191, 51))
        self.add.setStyleSheet("background:rgb(211, 215, 207);\n"
"color:black;")
        self.add.setObjectName("add")
        self.update = QtWidgets.QPushButton(Dialog)
        self.update.setGeometry(QtCore.QRect(460, 640, 191, 51))
        self.update.setStyleSheet("background:rgb(211, 215, 207);\n"
"color:black;")
        self.update.setObjectName("update")
        self.delete_2 = QtWidgets.QPushButton(Dialog)
        self.delete_2.setGeometry(QtCore.QRect(720, 640, 191, 51))
        self.delete_2.setStyleSheet("background:rgb(211, 215, 207);\n"
"color:black;")
        self.delete_2.setObjectName("delete_2")
        self.clear = QtWidgets.QPushButton(Dialog)
        self.clear.setGeometry(QtCore.QRect(980, 640, 191, 51))
        self.clear.setStyleSheet("background:rgb(211, 215, 207);\n"
"color:black;")
        self.clear.setObjectName("clear")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


# ##########################################################################""

        self.proofid.currentIndexChanged.connect(self.selectionchange)
        self.stackedWidget.setCurrentWidget(self.vide)

# ##########################################################################""


        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#fce94f;\">NBHJB</span></p></body></html>"))
        self.label.setWhatsThis(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:400;\">EMPLOYEE MANAGEMENT</span></p></body></html>"))
        self.groupBox.setTitle(_translate("Dialog", "Search Employee"))
        self.search.setText(_translate("Dialog", "Search"))
        self.label_2.setText(_translate("Dialog", "Employee ID:"))
        self.label_4.setToolTip(_translate("Dialog", "<html><head/><body><p>DSOO LDO</p></body></html>"))
        self.label_4.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Employee ID:</p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Employee ID:</span></p></body></html>"))
        self.label_5.setToolTip(_translate("Dialog", "<html><head/><body><p>DSOO LDO</p></body></html>"))
        self.label_5.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Employee ID:</p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Name:</span></p></body></html>"))
        self.label_6.setToolTip(_translate("Dialog", "<html><head/><body><p>DSOO LDO</p></body></html>"))
        self.label_6.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Employee ID:</p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Select Gender:</span></p></body></html>"))
        self.label_7.setToolTip(_translate("Dialog", "<html><head/><body><p>DSOO LDO</p></body></html>"))
        self.label_7.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Employee ID:</p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Contact No.</span></p></body></html>"))
        self.label_8.setToolTip(_translate("Dialog", "<html><head/><body><p>DSOO LDO</p></body></html>"))
        self.label_8.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Employee ID:</p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Address:</span></p></body></html>"))
        self.label_9.setToolTip(_translate("Dialog", "<html><head/><body><p>DSOO LDO</p></body></html>"))
        self.label_9.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Employee ID:</p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Proof Of ID:</span></p></body></html>"))
        self.gender.setItemText(0, _translate("Dialog", "male"))
        self.gender.setItemText(1, _translate("Dialog", "female"))
        self.proofid.setItemText(0, _translate("Dialog", "PAN Card"))
        self.proofid.setItemText(1, _translate("Dialog", "DrivelicenceNo"))
        self.proofid.setItemText(2, _translate("Dialog", "Adhar Card"))
        
        
        

        


        self.label_10.setToolTip(_translate("Dialog", "<html><head/><body><p>DSOO LDO</p></body></html>"))
        self.label_10.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Employee ID:</p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p>PAN Card</p><p><br/></p></body></html>"))
        self.label_14.setToolTip(_translate("Dialog", "<html><head/><body><p>DSOO LDO</p></body></html>"))
        self.label_14.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Employee ID:</p></body></html>"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p>DrivelicenceNo</p></body></html>"))
        self.label_15.setToolTip(_translate("Dialog", "<html><head/><body><p>DSOO LDO</p></body></html>"))
        self.label_15.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Employee ID:</p></body></html>"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p>Adhar Card</p></body></html>"))
        self.label_11.setToolTip(_translate("Dialog", "<html><head/><body><p>DSOO LDO</p></body></html>"))
        self.label_11.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Employee ID:</p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Email:</span></p></body></html>"))
        self.label_12.setToolTip(_translate("Dialog", "<html><head/><body><p>DSOO LDO</p></body></html>"))
        self.label_12.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Employee ID:</p></body></html>"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Password:</span></p></body></html>"))
        self.label_13.setToolTip(_translate("Dialog", "<html><head/><body><p>DSOO LDO</p></body></html>"))
        self.label_13.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Employee ID:</p></body></html>"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Designation:</span></p></body></html>"))
        self.designation.setItemText(0, _translate("Dialog", "Choose designation"))
        self.designation.setItemText(1, _translate("Dialog", "Admin"))
        self.designation.setItemText(2, _translate("Dialog", "Employee"))
        self.add.setText(_translate("Dialog", "Add"))
        self.update.setText(_translate("Dialog", "Update"))
        self.delete_2.setText(_translate("Dialog", "Delete"))
        self.clear.setText(_translate("Dialog", "Clear"))





        
#bouttons
        self.search.clicked.connect(self.Search)
        self.add.clicked.connect(self.Ajout_Employee)
        self.update.clicked.connect(self.Update)
        self.delete_2.clicked.connect(self.Delete_Employee)
        self.clear.clicked.connect(self.Clear_Employee)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
