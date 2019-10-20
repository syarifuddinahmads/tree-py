from flask import Flask
from controller.tree import tree
from os import path, walk

app = Flask(__name__)
#app.secret_key = 'mahasiswa_python' #secret key application
app.secret_key = 'tree_python' #secret key application

#register controller
# app.register_blueprint(mahasiswa)
app.register_blueprint(tree)

extra_dirs = ['directory/to/watch',]
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in walk(extra_dir):
        for filename in files:
            filename = path.join(dirname, filename)
            if path.isfile(filename):
                extra_files.append(filename)

if __name__ == '__main__':
    app.run(Debug=True,extra_files=extra_files)
