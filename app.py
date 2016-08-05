from flask import Flask, render_template
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
    return "searching"


if __name__ == '__main__':
    app.run(debug=True)
