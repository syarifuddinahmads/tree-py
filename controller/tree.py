from flask import Blueprint,jsonify, redirect, render_template, request, flash
from model.tree import TreeModel

tree = Blueprint('tree', __name__)

@tree.route('/')
def index():
    userAvailable = TreeModel.getUserAvailable()
    return render_template('tree/tree.html',userAvailable = userAvailable)

@tree.route('/<int:id>')
def userTree(id):
    return render_template('tree/tree.html',id=id)

@tree.route('/ajax-data-tree')
def getDataTree():
    tree = TreeModel.getTree()
    return jsonify(tree)

@tree.route('/save-tree',methods=['POST'])
def saveTree():
    try:
        TreeModel.insertTree(request)
    except:
        print('ERRORS')
    return redirect('/')

@tree.route('/get-network-up-tree/<int:id>')
def getUplineTree(id):
    tree = TreeModel.searchNetworkUp(id)
    return jsonify(tree)

@tree.route('/get-network-down-tree/<int:id>')
def getDownlineTree(id):
    tree = TreeModel.searchNetworkDown(id)
    return jsonify(tree)
