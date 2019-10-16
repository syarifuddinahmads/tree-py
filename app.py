from flask import Flask
from controller.mahasiswa import mahasiswa

app = Flask(__name__)
app.secret_key = 'mahasiswa_python' #secret key application

#register controller mahasiswa
app.register_blueprint(mahasiswa)

if __name__ == '__main__':
    app.run(Debug=True)
