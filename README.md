 2016 Skunkworks Project: Using Machine Learning to Learn from athlete-related data
 
Getting Started With the Environment:
 - Clone the repository..
 - Ensure that you have `npm` and `pip` installed. 
 - To install pip, run `sudo easy_install pip`.
 - Install virtualenv. This is so that we can have mulitple versions of Python/Python libraries. Virtualenv lets you have many different installations for python, useful if you use it for other projects. Run `sudo easy_install virtualenv`.
 - Set up the backend by creating a virtual environment and then installing the backend requirements with `pip`:
 
 ```python
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
(NOTE: `requirements.txt` may not be completely up-to-date with the latest python library dependencies. If you get an error saying a certain module couldn't be found, run `pip install x` where x is the missing module. 

For the front end, use npm to install webpack and the dependencies as listed in `package.json`:
`npm install -g webpack` and then `npm install`.


To bundle up the JS files, run `webpack`. This will create a bundled front-end file `static/bundle.js`.
Run `webpack --watch` to make changes to the front-end without having to restart the backend.

Run the backend:
Activate the virtualenv with `source venv/bin/activate`. Then run `python app.py` and go to the localhost the app is listening on. 

Development: 
- Make changes to the backend by editing `app.py`. 
- Make changes to the front-end by editing the JS files and recompiling them with `webpack --watch`.

Screenshots:

- Front-end UI: Query for athletes: 
![UI](https://raw.githubusercontent.com/rohan-varma/awesome-athletes/master/images/intro_screen.png "Front-end UI")

- Results page rendered after parsing JSON response from backend:
![Results](https://raw.githubusercontent.com/rohan-varma/awesome-athletes/master/images/query_results.png "Results page")
