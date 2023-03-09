from flask import Flask ,request,jsonify
# GET - Post a data in URL
# POST - Posting a data in body

app = Flask(__name__)

@app.route('/add',methods = ['GET','POST'])
def Addition():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify(result)

@app.route('/mul',methods = ['GET','POST'])
def Multiplication():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a*b
        return jsonify(result)

@app.route('/sub',methods = ['GET','POST'])
def Substraction():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a-b
        return jsonify(result)

@app.route('/div',methods = ['GET','POST'])
def Division():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a/b
        return jsonify(result)


if __name__=='__main__':
    app.run()

