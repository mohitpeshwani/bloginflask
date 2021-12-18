# Blog Application on Flask
This is the Blog web Application built on Flask app wit ORM support of SQLALCHEMY.<br>
Front-end is taken from the bootstrap website.<br><hr>
<strong>Install virtual Environment and activate virtual Environment</strong>
<ul>
<li>to install virtual environment type in cmd <strong>$ pip install virtualenv</strong></li>
<li>to create virtual environment <strong> $ virtualenv my_name</strong></li>
<li>to activate virtual environment in windows<strong>  $ venv\Scripts\activate.bat </strong></li></ul>

<hr>
<strong>Install SQLALCHEMY and create Database </strong>
<ul>
<li>to install sql-alchemy<strong> $ pip install flask-sqlalchemy</strong></li>
<li>In flask app we have to config <strong> app.config['SQL_DATABASE_URI']=""sqlite:\\\myuser.db</strong></li>
<li>To create the database we got to the python <strong> <br>from app import db <br> db.create_all<br> </strong></li>
<li>To create the model we do <strong><br> from app import User,Blog <br>User.query.all()<br>Blog.query.all()<br></strong></li>
<li>we have to commite it <strong><br>db.session.commit()<br></strong></li></ul>
<br>
<hr>
<strong>Required installation</strong>
<ol type="I">
<li>flask</li>
<li>flask-login</li>
<li>flask-sqlalchemy</li>
<li>python 3+ version</li>
</ol>
<hr>
<h3>TO run the flask blog web app <h3>
<p> <i>Activate the Virtual Environment (optional)</i>.<br>
Run the command in cmd  To activate the flask app <ul type=" square"><li><strong><i>python app.py</i></strong></li></ul>
View the flask blogs on browser through anyone of following
<ul type=" square"><li><i>http://localhost:5000/</li> <li>127.0.0.1:5000</i></li></ul></p>
<hr>
<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://www.linkedin.com/in/mohitpeshwani/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="mohit peshwani" height="30" width="40" /></a>
<a href="https://instagram.com/coding_nightmare" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="coding_nightmare" height="30" width="40" /></a>
<a href="https://www.figma.com/@mohitpeshwani" target="blank"><img align="center" src="https://logowik.com/content/uploads/images/figma.jpg" alt="mohit peshwani" height="30" width="40" /></a>
</p>
