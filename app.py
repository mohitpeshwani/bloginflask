from enum import unique
from flask import Flask,request,redirect,flash,url_for
from flask.sessions import NullSession
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user,UserMixin,logout_user
from datetime import datetime

from sqlalchemy.orm import defaultload

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///myuser.db"
app.config['SECRET_KEY']="thisiskey"
db=SQLAlchemy(app)
login_manager=LoginManager()
login_manager.init_app(app)


class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),unique=True,nullable=False)
    first=db.Column(db.String(50),unique=False,nullable=False)
    last=db.Column(db.String(50),unique=False,nullable=False)
    password=db.Column(db.String(50),unique=False,nullable=False)

    def __repr__(self):
        return '<User %r>' %self.username
class Blog(db.Model):
    block_id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(120),nullable=False)
    author=db.Column(db.String(120),nullable=False)
    content=db.Column(db.Text(),nullable=False)
    pub_date=db.Column(db.DateTime(),nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return '<Blog %r>' %self.title
    
@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))    

@app.route('/')
def home():
    return render_template('index.html')    


@app.route('/index')
def index():
    data=Blog.query.all()
    return render_template('index.html',data=data)

@app.route('/login',methods=['GET','POST'])
def log():
    if request.method=='POST':
        username=request.form.get('uname')
        password=request.form.get('pswd')
        user=User.query.filter_by(username=username).first()
        if user and password==user.password:
            login_user(user)
            return redirect('/index')
        else:
            flash("Invalid password/userid(email)",'info')
            return redirect('/login')

    return render_template('login.html')


@app.route('/signup',methods=['POST','GET'])
def login():
    if request.method=='POST':
        uname=request.form.get('uname')
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        pswd=request.form.get('pswd')
        adder=User(username=uname,first=fname,last=lname,password=pswd)
        db.session.add(adder)
        db.session.commit()
        flash('You are registered Successfully','success')
        return redirect('/login')
    

    return render_template('signup.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

@app.route('/blogpost',methods=['GET','POST'])
def blogpost():
    if request.method=='POST':
        title=request.form.get('title')
        
        author=request.form.get('author')
        content=request.form.get('content')
        blog1=Blog(title=title,author=author,content=content)
        db.session.add(blog1)
        db.session.commit()
        flash("Your Blog have been submitted Successfully",'success')
        return redirect('/')
    return render_template('blog.html')
@app.route("/blog_detail/<int:id>",methods=['GET','POST'])
def blog_details(id):
    blog=Blog.query.get(id)
    return render_template('blog_details.html',blog=blog)

@app.route("/delete/<int:id>",methods=['GET','POST'])
def blog_delete(id):
    blog=Blog.query.get(id)
    db.session.delete(blog)
    db.session.commit()
    flash('Blog is deleted successfully','success')
    return redirect('/')

@app.route("/edit/<int:id>",methods=['GET','POST'])
def blog_edit(id):
    blog=Blog.query.get(id)
    if request.method=='POST':
        blog.title=request.form.get('title')
        blog.author=request.form.get('author')
        blog.content=request.form.get('content')
        db.session.commit()
        flash('Post have been edited','success')
        redirect('/index')
    return render_template('edit.html',blog=blog)




if __name__=='__main__': 
    app.run(debug=True)