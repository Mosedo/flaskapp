from flask import Flask, render_template,session,request,redirect,url_for,flash
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime


app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:vmbxNugImDm2cSbpOvUq@containers-us-west-105.railway.app:6652/railway'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:vmbxNugImDm2cSbpOvUq@containers-us-west-105.railway.app:6652/railway'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shinda'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.secret_key = "JNSDJFGUDFHIDUMDUF9I9"

user = {
    "name":"Musa Ibrahim",
    "email":"ibrahmmusauon@gmail.com",
    "password":"password",
    "image":"https://play-lh.googleusercontent.com/hYPZe_34_z5lI17PmszXNfXTAqoQommnofwjrYrs4javrcOdp_U_jrzckmPRUj5qx0r6=w240-h480-rw",
    "status":"My status"
}



@app.route('/login',methods = ['GET','POST'])
def login():

    if "user" in session:
        return redirect(url_for('home'))
    else:
        if request.method == 'GET':
            return render_template('userauth/login.html')
        else:
            if request.form["email"] == user["email"]:
                if request.form["password"] != user["password"]:
                    flash({"msg":"You entered the wrong password","type":"password"},'warning')
                    return redirect(url_for('login'))
                else:
                    session["user"] = user
                    return redirect(url_for('home'))
            else:
                flash({"msg":"User does not exist!","type":"email"},'warning')
                return redirect(url_for('login'))
                #return render_template('userauth/login.html',login_response="Non existent")
    



@app.route('/',methods = ['GET'])
def home():

    if "user" in session:
        return render_template('index.html')
        # return render_template('partials/home.html')
    else:
        return redirect(url_for('login'))
    

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))



    # users = [
    #     {
    #         "name":"Musa Ibrahim",
    #         "age": 28,
    #         "height":"6 ft",
    #         "university":"U.o.N"
    #     },
    #     {
    #         "name":"John Doe",
    #         "age": 30,
    #         "height":"5.7 ft",
    #         "university":"T.U.K"
    #     }
    # ]
    # return render_template('partials/home.html', users = users)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)