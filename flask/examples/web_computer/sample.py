from flask import Flask,render_template,request
from models import user_details

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


    
# @app.route("/")
# @app.route("/home")
# def home():
#     courses = ["python","Java","c++","html"]
#     is_course=True
#     return render_template("home.html",home_course=courses,is_home_course=is_course)

# @app.route("/aboutpython")
# def about():
#     python = ["Python Basics","Input/Output","Python Data Types","Variables","Python Operators",
#               "Object Oriented Concepts"]
#     return render_template("aboutpython.html",about_python = python)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/conform",methods=["POST","GET"])
def conf():
    if request.method == 'POST':
        fname = request.form.get('firstname')
        lname = request.form.get('lastname')
        age = request.form.get("age")
        city = request.form.get('city')

        return render_template("conform.html",fname=fname,lname=lname,age=age,city=city)


# @app.route("/<name>")
# def data_type(name):
#     # return f"<h2>Welcome {name.upper()}</h2>"
#     fruits = ["Apple","Orange","Mango"]
#     detail ={"Name":"Indhu",
#              "Profession":"Python Developer"}
#     return render_template("user.html",user_name=name,user_fruits=fruits,user_detail=detail)




if __name__ == "__main__":
    app.run(debug=True)
