'''
Created on 29 jul 2015

@author: Emil
'''

import os
import sqlite3
from types import NoneType
from PIL import Image
import StringIO

class DAL(object):
    
    CARDS_TABLE = "cards"
    IMAGES_TABLE = "images"
    
    CARDS_ID = "id"
    CARDS_MIN_AP = "minAp"
    CARDS_MAX_AP = "maxAp"
    CARDS_MIN_DP = "minDp"
    CARDS_MAX_DP = "maxDp"
    CARDS_MIN_HP = "minHp"
    CARDS_MAX_HP = "maxHp"
    CARDS_NAME = "name"
    CARDS_DESCRIPTION = "description"
    CARDS_IMAGE = "image"
    
    IMAGES_ID = "id"
    IMAGES_NAME = "name"
    IMAGES_TYPE = "type"
    IMAGES_BLOB = "image_data"
    
    __connection = None
    __dbName = "data.sqlite"
    __dbPath = None
    

    def __init__(self, *args, **kwargs):
        self.__dbPath = os.path.join(os.getcwd(), "..", "data", self.__dbName)
        
    def GetAllCards(self):
        sql = "SELECT * FROM %s" % self.CARDS_TABLE
        
        self.__connOpen()
        self.__connection.row_factory = sqlite3.Row
        cur = self.__connection.cursor()
        
        result = cur.execute(sql).fetchall()
        
        self.__connClose()
        return result
    
    def GetPictureById(self, pictureId):
        sql = "SELECT * FROM %s WHERE %s=?" % (self.IMAGES_TABLE, self.IMAGES_ID)
        
        self.__connOpen()
        self.__connection.row_factory = sqlite3.Row
        cur = self.__connection.cursor()
        
        result = cur.execute(sql,(pictureId,)).fetchone()
        self.__connClose()
        
        buffer = StringIO.StringIO(result[self.IMAGES_BLOB])
        
        image = Image.open(buffer)
        
        return image
        
    def __connOpen(self):
        if self.__connection == None:
            self.__connection = sqlite3.connect(self.__dbPath)
        else:
            self.__connClose()
            self.__connOpen()
        
    def __connClose(self):
        try:
            self.__connection.close()
            self.__connection = None
        except:
            self.__connection = None