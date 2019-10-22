from flask import Blueprint,jsonify, redirect, render_template, request, flash
from model.tree import TreeModel

tree = Blueprint('tree', __name__)

@tree.route('/')
def index():
    return render_template('tree/tree.html')
