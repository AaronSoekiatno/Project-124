"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'
@app.route('/details')
def details():
    return 'Hi I am Aaron! I am really excited to create my first Api'

if __name__ == '__main__':
   app.run()
"""
