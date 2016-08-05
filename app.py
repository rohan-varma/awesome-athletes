from flask import Flask, render_template, Response
from flask import jsonify
from flask import json
from main import Main
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def hello_world():
    print "change made"
    return render_template('index.html')

@app.route('/search/<query>')
def search(query):
    #"similar to full name in 2016"
    li = query.split()
    name = li[2]
    last = li[3]
    year = int(li[5])
    m = Main(name, last, year)
    thing = m.get_thing()




    #supported query :
        # similar to salvidor perez
    #parse query get similar athletes and return results in json
    obj = []
    for item in thing:
        dat = json.dumps(item.tolist())
        obj.append(dat)
    a = json.dumps(obj)
    return a



if __name__ == '__main__':
    app.run(debug=True)
