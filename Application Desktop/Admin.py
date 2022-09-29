# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QMessageBox
from biblio1.EmployeeStacked import Ui_Dialog as EmployeeManagement
from biblio1.productDash2 import Ui_MainWindow as viewproduct
from biblio1.productDash import  Ui_MainWindow as productmanagement
from biblio1.Supplier import Ui_Form as suppliermanagement 
from biblio1.EmployeeDetails import     Ui_Form  as Empdetails
import facture 
from biblio.change_password  import Ui_password
from biblio.session import  Ui_Form 
from biblio.about_us import Ui_about_us  
import  Login 
from biblio1.importf import Ui_Form  as importf
from biblio1.export import Ui_Form  as export
from biblio.emplyee import Ui_employee
from biblio.products import Ui_product



class Ui_pageAdmin(object):
     
         
    
    def boutonlogout(self):
        self.login =QtWidgets.QWidget()
        self.ui=Login.Ui_Login()
        self.ui.setupUi(self.login)
        self.login.show()
    def boutonchangepassword(self):
        self.password = QtWidgets.QWidget()
        self.ui = Ui_password()
        self.ui.setupUi(self.password)
        self.password.show()
    def boutonemployee(self):
        self.employee = QtWidgets.QWidget()
        self.ui = Ui_employee()
        self.ui.setupUi(self.employee)
        self.employee.show()
    def boutonsession(self):
        self.session= QtWidgets.QWidget()
        self.ui = Ui_Form ()
        self.ui.setupUi(self.session)
        self.session.show()
    
    def boutonproduct(self):
        self.product= QtWidgets.QDialog()
        self.ui = Ui_product ()
        self.ui.setupUi(self.product)
        self.product.show()
    def boutonaboutus(self):
        self.about= QtWidgets.QWidget()
        self.ui = Ui_about_us ()
        self.ui.setupUi(self.about)
        self.about.show()






   
    def setupUi(self, pageAdmin):
        pageAdmin.setObjectName("pageAdmin")
        pageAdmin.resize(1438, 766)
        self.centralwidget = QtWidgets.QWidget(pageAdmin)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 3000, 771))
        self.widget.setStyleSheet("background-color: rgb(78, 0, 117);\n"
"background-color: rgb(68, 8, 80);")
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1511, 81))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.Title = QtWidgets.QLabel(self.frame)
        self.Title.setGeometry(QtCore.QRect(690, 10, 371, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setStyleSheet("#Title{\n"
"    \n"
"    color: rgb(0, 0, 127);\n"
"}")
        self.Title.setObjectName("Title")
        self.Time = QtWidgets.QLabel(self.frame)
        self.Time.setGeometry(QtCore.QRect(1310, 10, 121, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Time.sizePolicy().hasHeightForWidth())
        self.Time.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Time.setFont(font)
        self.Time.setObjectName("Time")
        self.Logout = QtWidgets.QPushButton(self.frame)
        self.Logout.setGeometry(QtCore.QRect(10, 50, 120, 23))
        self.Logout.setMinimumSize(QtCore.QSize(120, 0))
        self.Logout.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Logout.setFont(font)
        self.Logout.setStyleSheet("#Logout{\n"
"    \n"
"    background-color: rgb(146, 190, 217);\n"
"}")
        self.Logout.setObjectName("Logout")
        self.Time_2 = QtWidgets.QLabel(self.frame)
        self.Time_2.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Time_2.sizePolicy().hasHeightForWidth())
        self.Time_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Time_2.setFont(font)
        self.Time_2.setStyleSheet("image: url(:/newPrefix/360_F_446441329_ZZ4AtuYHjDNXals44YCJrQldclwamZvJ.jpg);")
        self.Time_2.setText("")
        self.Time_2.setObjectName("Time_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 10, 71, 31))
        self.label.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(560, 20, 101, 41))
        self.label_2.setStyleSheet("image: url(:/newPrefix/Double-J-Design-Origami-Colored-Pencil-Yellow-home.ico);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.Time_2.raise_()
        self.Title.raise_()
        self.Time.raise_()
        self.Logout.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setGeometry(QtCore.QRect(0, 79, 140, 641))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(3)
        self.frame_2.setObjectName("frame_2")
        self.ChangeButton = QtWidgets.QPushButton(self.frame_2)
        self.ChangeButton.setGeometry(QtCore.QRect(4, 130, 131, 128))
        self.ChangeButton.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ChangeButton.setFont(font)
        self.ChangeButton.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.ChangeButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.ChangeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image.qrc/1824728.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ChangeButton.setIcon(icon)
        self.ChangeButton.setIconSize(QtCore.QSize(80, 80))
        self.ChangeButton.setDefault(False)
        self.ChangeButton.setFlat(False)
        self.ChangeButton.setObjectName("ChangeButton")
        self.EmployeeButton = QtWidgets.QPushButton(self.frame_2)
        self.EmployeeButton.setGeometry(QtCore.QRect(6, 258, 131, 128))
        self.EmployeeButton.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.EmployeeButton.setFont(font)
        self.EmployeeButton.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.EmployeeButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.EmployeeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../image.qrc/20698.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EmployeeButton.setIcon(icon1)
        self.EmployeeButton.setIconSize(QtCore.QSize(100, 100))
        self.EmployeeButton.setDefault(False)
        self.EmployeeButton.setFlat(False)
        self.EmployeeButton.setObjectName("EmployeeButton")
        self.SessionButton = QtWidgets.QPushButton(self.frame_2)
        self.SessionButton.setGeometry(QtCore.QRect(6, 386, 131, 128))
        self.SessionButton.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SessionButton.setFont(font)
        self.SessionButton.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.SessionButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.SessionButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../image.qrc/32220.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SessionButton.setIcon(icon2)
        self.SessionButton.setIconSize(QtCore.QSize(75, 75))
        self.SessionButton.setDefault(False)
        self.SessionButton.setFlat(False)
        self.SessionButton.setObjectName("SessionButton")
        self.AboutButton = QtWidgets.QPushButton(self.frame_2)
        self.AboutButton.setGeometry(QtCore.QRect(6, 514, 131, 121))
        self.AboutButton.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AboutButton.setFont(font)
        self.AboutButton.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.AboutButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.AboutButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../image.qrc/2930386.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AboutButton.setIcon(icon3)
        self.AboutButton.setIconSize(QtCore.QSize(70, 70))
        self.AboutButton.setDefault(False)
        self.AboutButton.setFlat(False)
        self.AboutButton.setObjectName("AboutButton")
        self.ProductButton = QtWidgets.QPushButton(self.frame_2)
        self.ProductButton.setGeometry(QtCore.QRect(4, 10, 131, 128))
        self.ProductButton.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ProductButton.setFont(font)
        self.ProductButton.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.ProductButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.ProductButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../image.qrc/products.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ProductButton.setIcon(icon4)
        self.ProductButton.setIconSize(QtCore.QSize(120, 120))
        self.ProductButton.setAutoRepeatDelay(300)
        self.ProductButton.setAutoRepeatInterval(100)
        self.ProductButton.setDefault(False)
        self.ProductButton.setFlat(False)
        self.ProductButton.setObjectName("ProductButton")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(30, 110, 81, 16))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(10, 230, 121, 20))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(30, 360, 81, 16))
        self.label_9.setStyleSheet("background-color: rgb(223, 223, 223);\n"
"background-color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(40, 610, 61, 16))
        self.label_10.setStyleSheet("background-color: rgb(223, 223, 223);\n"
"background-color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(40, 490, 71, 20))
        self.label_11.setStyleSheet("background-color: rgb(223, 223, 223);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.frame_2.raise_()
        self.frame.raise_()
        pageAdmin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(pageAdmin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1438, 26))
        self.menubar.setObjectName("menubar")
        self.menuEmployee = QtWidgets.QMenu(self.menubar)
        self.menuEmployee.setObjectName("menuEmployee")
        self.menusupplier = QtWidgets.QMenu(self.menubar)
        self.menusupplier.setObjectName("menusupplier")
        self.menuProduct = QtWidgets.QMenu(self.menubar)
        self.menuProduct.setObjectName("menuProduct")
        self.menuCustomer_Bills = QtWidgets.QMenu(self.menubar)
        self.menuCustomer_Bills.setObjectName("menuCustomer_Bills")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        self.menuExit_2 = QtWidgets.QMenu(self.menubar)
        self.menuExit_2.setObjectName("menuExit_2")
        self.menuExit_3 = QtWidgets.QMenu(self.menubar)
        self.menuExit_3.setObjectName("menuExit_3")
        self.menuExit_4 = QtWidgets.QMenu(self.menubar)
        self.menuExit_4.setObjectName("menuExit_4")
        pageAdmin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(pageAdmin)
        self.statusbar.setObjectName("statusbar")
        pageAdmin.setStatusBar(self.statusbar)
        self.actionSupplier_Management = QtWidgets.QAction(pageAdmin)
        self.actionSupplier_Management.setObjectName("actionSupplier_Management")
        self.actionProduct_Management = QtWidgets.QAction(pageAdmin)
        self.actionProduct_Management.setObjectName("actionProduct_Management")
        self.actionView_Products = QtWidgets.QAction(pageAdmin)
        self.actionView_Products.setObjectName("actionView_Products")
        self.actionEmployee_Details = QtWidgets.QAction(pageAdmin)
        self.actionEmployee_Details.setObjectName("actionEmployee_Details")
        self.actionEmployee_Management = QtWidgets.QAction(pageAdmin)
        self.actionEmployee_Management.setObjectName("actionEmployee_Management")
        self.actionExport = QtWidgets.QAction(pageAdmin)
        self.actionExport.setObjectName("actionExport")
        self.actionimport = QtWidgets.QAction(pageAdmin)
        self.actionimport.setObjectName("actionimport")
        self.actionCustomer = QtWidgets.QAction(pageAdmin)
        self.actionCustomer.setObjectName("actionCustomer")
        self.menuEmployee.addAction(self.actionEmployee_Details)
        self.menuEmployee.addAction(self.actionEmployee_Management)
        self.menuCustomer_Bills.addAction(self.actionCustomer)
        self.menusupplier.addSeparator()
        self.menusupplier.addAction(self.actionSupplier_Management)
        self.menuProduct.addAction(self.actionProduct_Management)
        self.menuProduct.addAction(self.actionView_Products)
        self.menuExit_2.addAction(self.actionExport)
        self.menuExit_2.addAction(self.actionimport)
        self.menubar.addAction(self.menuEmployee.menuAction())
        self.menubar.addAction(self.menusupplier.menuAction())
        self.menubar.addAction(self.menuProduct.menuAction())
        self.menubar.addAction(self.menuCustomer_Bills.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        self.menubar.addAction(self.menuExit_2.menuAction())
        self.menubar.addAction(self.menuExit_3.menuAction())
        self.actionView_Products.triggered.connect(self.afficheproduct)
        self.actionProduct_Management.triggered.connect(self.afficheproductmanagement)
        self.actionSupplier_Management.triggered.connect(self.affichesupplier)
        self.actionEmployee_Management.triggered.connect(self.afficheemployee)
        self.actionCustomer.triggered.connect(self.affichecostumerbills)
        self.actionEmployee_Details.triggered.connect( self.afficheemployeedetails)
        self.actionExport.triggered.connect(self.afficheexport)
        self.actionimport.triggered.connect(self.afficheimport)
        

        self.retranslateUi(pageAdmin)
        QtCore.QMetaObject.connectSlotsByName(pageAdmin)

    def retranslateUi(self, pageAdmin):
        _translate = QtCore.QCoreApplication.translate
        pageAdmin.setWindowTitle(_translate("pageAdmin", "Admin"))
        self.Title.setText(_translate("pageAdmin", "Retail Mangement System"))
        self.Time.setText(_translate("pageAdmin", "(22:48:27)"))
        self.Logout.setText(_translate("pageAdmin", "Logout"))
        self.label.setText(_translate("pageAdmin", "Admin"))
        self.label_7.setText(_translate("pageAdmin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#0b0b0b;\">Products</span></p></body></html>"))
        self.label_8.setText(_translate("pageAdmin", "<html><head/><body><p><span style=\" font-weight:600;\">Change Password</span></p></body></html>"))
        self.label_9.setText(_translate("pageAdmin", "<html><head/><body><p><span style=\" font-weight:600;\">Employee</span></p></body></html>"))
        self.label_10.setText(_translate("pageAdmin", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">About Us</span></p></body></html>"))
        self.label_11.setText(_translate("pageAdmin", "<html><head/><body><p><span style=\" font-weight:600;\">Session</span></p></body></html>"))
        self.menuEmployee.setTitle(_translate("pageAdmin", "Employee"))
        self.menusupplier.setTitle(_translate("pageAdmin", "Supplier"))
        self.menuProduct.setTitle(_translate("pageAdmin", "Product"))
        self.menuCustomer_Bills.setTitle(_translate("pageAdmin", "Customer Bills"))
        self.menuExit.setTitle(_translate("pageAdmin", "Statistics"))
        self.menuExit_2.setTitle(_translate("pageAdmin", "Export/Import"))
        self.menuExit_3.setTitle(_translate("pageAdmin", "Exit"))
        self.actionSupplier_Management.setText(_translate("pageAdmin", "Supplier Management"))
        self.actionProduct_Management.setText(_translate("pageAdmin", "Product Management"))
        self.actionView_Products.setText(_translate("pageAdmin", "View Products"))
        self.actionEmployee_Details.setText(_translate("pageAdmin", "Employee Details"))
        self.actionEmployee_Management.setText(_translate("pageAdmin", "Employee Management"))
        self.actionExport.setText(_translate("pageAdmin", "Export"))
        self.actionimport.setText(_translate("pageAdmin", "Import"))
        self.actionCustomer.setText(_translate("pageAdmin", "Customer Bills"))
        self.actionView_Products.triggered.connect(lambda :self.afficheproduct)
        self.actionProduct_Management.triggered.connect(lambda :self.afficheproductmanagement)
        self.actionSupplier_Management.triggered.connect(lambda:self.affichesupplier)
        self.actionEmployee_Management.triggered.connect(lambda :self.afficheemployee)
        self.actionCustomer.triggered.connect(lambda :self.affichecostumerbills)
        self.actionEmployee_Details.triggered.connect(lambda : self.afficheemployeedetails)
        self.Logout.clicked.connect(self.boutonlogout)
        self.Logout.clicked.connect(pageAdmin.close)
        self.actionExport.triggered.connect( lambda :self.afficheexport)
        self.actionimport.triggered.connect( lambda :self.afficheimport)
        self.ProductButton.clicked.connect(self.boutonproduct)
        self.ChangeButton.clicked.connect(self.boutonchangepassword)
        self.EmployeeButton.clicked.connect(self.boutonemployee)
        self.SessionButton.clicked.connect(self.boutonsession)
        self.AboutButton.clicked.connect(self.boutonaboutus)
        
        
        
    def affichecostumerbills(self):
        self.EmployeeDashboard = QtWidgets.QWidget()
        self.ui = facture.Ui_EmployeeDashboard()
        self.ui.setupUi(self.EmployeeDashboard)
        self.EmployeeDashboard.show()   
    def afficheproduct(self):
        self.Productv = QtWidgets.QMainWindow()
        self.uiproductv = viewproduct()
        self.uiproductv.setupUi(self.Productv)
        self.Productv.show()
    def afficheemployee(self):
        self.Employee = QtWidgets.QDialog()
        self.uiemployee = EmployeeManagement()
        self.uiemployee.setupUi(self.Employee)
        self.Employee.show()
    def afficheproductmanagement(self):
        self.products = QtWidgets.QMainWindow()
        self.uiproducts = productmanagement()
        self.uiproducts.setupUi(self.products)
        self.products.show()
    def affichesupplier(self):
        self.supplier = QtWidgets.QWidget()
        self.uisupplier =suppliermanagement ()
        self.uisupplier.setupUi(self.supplier)
        self.supplier.show()
    def afficheemployeedetails(self):
        self.details = QtWidgets.QWidget()
        self.uidetails = Empdetails()
        self.uidetails.setupUi(self.details)
        self.details.show()
    def afficheexport(self):
        self.exportfile = QtWidgets.QWidget()
        self.uiexport = export()
        self.uiexport.setupUi(self.exportfile)
        self.exportfile.show()
    def afficheimport(self):
        self.importfile = QtWidgets.QWidget()
        self.uiimport = importf()
        self.uiimport.setupUi(self.importfile)
        self.importfile.show()

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pageAdmin = QtWidgets.QMainWindow()
    ui = Ui_pageAdmin()
    ui.setupUi(pageAdmin)
    #####│
    
   
    pageAdmin.show()
    sys.exit(app.exec_())
