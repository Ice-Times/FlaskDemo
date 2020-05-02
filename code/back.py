from flask import Flask,url_for,request,render_template,send_from_directory
app  =  Flask(__name__)
# @app.route('/submit', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         return render_template('submit.html', title= request.form['word'])
#
#     return render_template('submit.html', title= "")

@app.route('/', methods=['POST', 'GET'])
def log():
    return render_template('submit.html', title= "")

@app.route('/submit', methods=['POST', 'GET'])
def log2():
    if request.method == 'POST':
        return render_template('submit.html', title= request.form['word'])

@app.route("/download")
def index():
    #return send_from_directory(r"D:\\csv",filename="res.csv",as_attachment=True)
    return send_from_directory(r".\\static", filename="test.jpg", as_attachment=True)

@app.route('/function2')
def function2():
    return render_template('submit.html', output= "功能二")

@app.route('/function1')
def function1():
    return render_template('submit.html', output= "功能一")



if __name__ == "__main__":
    app.run(debug=True)