from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['DATABASE'] = 'mysql://root/password@localhost/plants'


    
if __name__ == '__main__':
    app.run(debug=True)
    