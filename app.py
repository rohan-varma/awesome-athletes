from flask import Flask, render_template, Response
from flask import jsonify
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def hello_world():
    print "change made"
    return render_template('index.html')

@app.route('/search/<query>')
def search(query):
    #supported query :
        # similar to salvidor perez
    #parse query get similar athletes and return results in json
    dat = jsonify(athlete = "none",
                      error = "errors!")
    return dat


if __name__ == '__main__':
    app.run(debug=True)
