from config.db import mysql
import pymysql

class UserModel():
    
    @classmethod
    
    def getAllUsers(self):
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql= "select * from users"
        cursor.execute(sql)
        user = cursor.fetchall()
        return user
    
    def saveUser(req):
        if (req is not None):
            try:
                sql = "insert into users(username,fullname) values (%s,%s)"
                data = (req.form['username'], req.form['fullname'])
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()
                return 'success'
            except ex:
                return ex