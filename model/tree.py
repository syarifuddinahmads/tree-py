from config.db import mysql
import pymysql

class TreeModel():

    @classmethod    

    def searchUserNetwork(self,id):
        if (id is not None):
            sql = "select * from t_tree t where t.id_user=%s"
            id = id
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql,id)
            user = cursor.fetchone()
            return user
    
    def searchNetworkUp(id):
        if (id is not None):
            user = TreeModel.searchUserNetwork(id)
            data = (user['Lnum'],user['Rnum'])
            sql = "select * from t_tree t join users u on u.id = t.id_user where t.Lnum <= %s and t.Rnum >= %s"
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql,data)
            tree = cursor.fetchall()
            return tree
        
    def searchNetworkDown(id):
        if (id is not None):
            user = TreeModel.searchUserNetwork(id)
            data = (user['Lnum'],user['Rnum'])
            sql = "select * from t_tree t join users u on u.id = t.id_user where t.Lnum >= %s and t.Rnum <= %s"
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql,data)
            tree = cursor.fetchall()
            return tree
        
    def getTree():
        sql = "select * from t_tree tr join users u on u.id = tr.id_user"
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        user = cursor.fetchall()
        return user
    
    def getUserAvailable():
        sql = "select * from users u where u.id not in (select t.id_user from t_tree t)"
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        user = cursor.fetchall()
        return user
    
    def insertTree(req):
        if (req is not None):
            lnum = req.form['rnum']
            rnum = int(req.form['rnum']) + 1
            idparent = req.form['idparent']
            iduser = req.form['user']  
            try:
                data = (iduser,idparent,lnum,rnum)
                sql = "insert into t_tree (id_user, id_parent,Lnum,Rnum) values (%s,%s,%s,%s)"
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()
                return 'success'
            except ex:
                return ex
    
    def updateLnumRnum():
        return ""