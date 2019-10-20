from flask import Blueprint,jsonify, redirect, render_template, request, flash
from model.tree import TreeModel

tree = Blueprint('tree', __name__)

@tree.route('/')
def index():
    user = TreeModel.get()
    return render_template('tree/tree.html', data=user)

def detailUser(q):
    user = TreeModel.getUserTree(q)
    return render_template('tree/tree.html')