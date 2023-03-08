# our problem statement is if we write some function here I will call the function somewhere else.
# e.g. ippa oru addition function inga eludhurom na, adha vera edathula irundhu call pannanum, that is problem statement.

# his requirement is he dont want to call hear, he want to call in postman


from flask import Flask, request, render_template, jsonify

app = Flask(__name__) # I will be able to utilize the return inside the flask, this is the meaning of this line.
# this app is nothing but its a object of flask, it can be anything my name or your name.
# __name__ means all the named function its going to import

@app.route("/xyz", methods=['POST']) #anyone if they hit the xyz route they will able to get this function
def test():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify(str(result))

@app.route('/abc/sudh', methods=["POST"])
def test1():
    if (request.method == 'POST'):
        a = request.json['num3']
        b = request.json['num4']
        result = a + b
        return jsonify(str(result))

@app.route('/abc/sudh/kumar', methods=["POST"])
def test2():
    if (request.method == 'POST'):
        a = request.json['num5']
        b = request.json['num6']
        result = a + b
        return jsonify(str(result))

@app.route('/abcxyz', methods=["POST"])
def test3():
    if (request.method == 'POST'):
        a = request.json['sudh']
        b = request.json['kumar']
        result = a + b
        return jsonify(str(result))                                                                                                                                                                                                                     
    
if __name__ == '__main__': #this is the construct at all python main function we are trying to give
    app.run(host="127.0.0.1", port=5000)
# try to call the main of the pythonic class with __name__ and try to execute the app.
# (app) in top line app=Flask(__name__)

# we hear lot of times facebook is down, linkedin is down, that means system is down - In which particular program or particular software is running so that is down.

# That's why we do last 2 lines in flask
# This will keep my server up and run.

# Task
# 1. Write a function to fetch data from sql table via api
# 2. Write a function to fetch a data from mongodb table

