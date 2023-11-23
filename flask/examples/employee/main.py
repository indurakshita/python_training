
from flask import Flask,render_template,request
from models import db

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employee.db"
db.init_app(app)

@app.route("/",methods=["POST","GET"])

def employees():
    name =''
    profession = ''
    if request.method == "POST":
        name = request.form.get("name")
        profession = request.form.get("profession")
        
    return render_template("form.html",name=name,profession=profession)



if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0')


 
 