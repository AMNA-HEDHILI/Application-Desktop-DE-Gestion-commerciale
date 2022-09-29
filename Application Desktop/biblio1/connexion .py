import  pymongo
from pymongo import MongoClient
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication


#création bd
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["DesktopApp"]
#collection categorie
collectionCategory=db.category


"""""
#Ajout
collectionCategory=db.category
category_1 = {
        "Name":"végétal"
}

rec_id1 = collectionCategory.insert_one(category_1)
cursor = collectionCategory.find()
for record in cursor:
    print(record)
print(myclient.list_database_names())

#Modfication
result = collectionCategory.update_many(
        {"Name":"alimentaire"},
        {
                "$set":{
                        "Name":"informatique"
                        }
                  
        }
        )
print("Data modifié ",result)
  
# affichage du nouvel enregisstrement
cursor2 = collectionCategory.find()
for record in cursor2:
    print(record)


"""

