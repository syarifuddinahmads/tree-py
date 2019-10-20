from flask import Flask
from controller.tree import tree

app = Flask(__name__)
#app.secret_key = 'mahasiswa_python' #secret key application
app.secret_key = 'tree_python' #secret key application

#register controller
# app.register_blueprint(mahasiswa)
app.register_blueprint(tree)

if __name__ == '__main__':
    app.run(Debug=True)
