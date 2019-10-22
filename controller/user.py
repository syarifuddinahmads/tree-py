from flask import Blueprint,jsonify, redirect, render_template, request, flash
from model.user import UserModel

user = Blueprint('user', __name__)

@user.route('/users')
def users():
    usersList = UserModel.getAllUsers()
    return render_template('user/users.html',users=usersList)

@user.route('/add-user')
def addUser():
    return render_template('user/add.html')

@user.route('/save-user',methods=['POST'])
def saveUser():
    try:
        UserModel.saveUser(request)
    except:
        print('ERRORS')
    return redirect('users')
