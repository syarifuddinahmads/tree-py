from flask import Flask
from controller.tree import tree
from controller.user import user

app = Flask(__name__)
app.secret_key = 'tree_python' #secret key application

#register controller
app.register_blueprint(tree)
app.register_blueprint(user)


if __name__ == '__main__':
    app.run(Debug=True)
