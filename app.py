from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
@app.route('/')
@app.route('/index')
def hello_world():
    print "change made"
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
