from config.db import mysql
import pymysql

class TreeModel():

    @classmethod
    def get(self):
        user = ['tes','tes']
        return user
    
    def getUserTree(q):
        user = []
        return user

    def saveUser(req):
        if (req is not None):
            username = req.form['username']
            fullname = req.form['fullname']
            try:
                sql = "INSERT INTO users(username,fullname) VALUES(%s,%s)"
                data = (username, fullname)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()
                return 'success'
            except ex:
                return ex