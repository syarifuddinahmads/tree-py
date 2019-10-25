from config.db import mysql
import pymysql

class TreeModel():

    @classmethod    
          
    def searchUserNetwork(id):
        if (id is not None):
            sql = "select * from t_tree where id=%s"
            id = id
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql,id)
            user = cursor.fetchone()
            return user
    
    def searchNetworkUp(id):
        if (id is not None):
            sql = "select * from t_tree t join users u on u.id = t.id_user where t.Lnum <= %s and t.Rnum >= %s"
            user = TreeModel.searchUserNetwork(id)
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql,(user['Lnum'],user['Rnum']))
            user = cursor.fetchone()
            return user
        
    def getTree():
        sql = "select * from t_tree tr join users u on u.id = tr.id_user"
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        user = cursor.fetchall()
        return user
            
            