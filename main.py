from flask import Flask, redirect, request, url_for

app = Flask(__name__)

# @app.route('/welcome')

# def hello_world():
#     return "Welcome to the Flask Project"

# @app.route('/blog/<float:id>')

# def blog(id):
#     return "Hello %f" % id

# @app.route('/blogids/<int:blogid>')

# def blogids(blogid):
#     return "Hello %f" % blogid

@app.route('/success/<name>/<password>')

def success(name,password):
    return "Your user_name is: %s" %name + " \n Your password is: %s" %password

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':    
        user = request.form['nm']
        password = request.form['nm1']
        return redirect(url_for('success', name = user, password = password))

if __name__ == '__main__':
    app.run(debug=True) 