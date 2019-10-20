from flask import Blueprint,jsonify, redirect, render_template, request, flash
from model.tree import TreeModel

tree = Blueprint('tree', __name__)

@tree.route('/')
def index():
    user = TreeModel.get()
    return render_template('tree/tree.html', data=user)

@tree.route('/add-user')
def addUser():
    return render_template('tree/add.html')

@tree.route('/user/<int:id>')
def detailUser(id):
    user = TreeModel.getUserTree(id)
    return render_template('tree/tree.html')

@tree.route('/save-user',methods=['POST'])
def saveUser():
    try:
        TreeModel.saveUser(request)
    except ex:
        print('ERRORS = ',ex)
    return render_template('tree/add.html')
