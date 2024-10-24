from flask import Flask,render_template,redirect,url_forrequest,flash
from flask_login import LoginManger,UserMixin,login_user,login_required,logout_user,current_user
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key' #replace with your secret key
#Initialize Flask_Login
login_manger = LoginManager()
login_manger. init_app(app)
login_manger. loginview= 'login'#Redirect unauthorized users to the login page
#Mock database of user(for demonstration)
users ={'users1':{'password':'password123'}}
#User class that inherits from UserMixin to handle user-related peration
class User(UserMixin):
    def __name__(self,id):
        self.id = id
@login_manager.user_loader
def load_user(user_id):
    return User(user_id) if user_id in users else None
@app.route('/')
@login_required #protect this route to allow only logged-in users
def home():
    return render_template('home.html',name=current_user.id)
@app.route('/login',methods= ['GET','POST'])
def login():
    if request.method =='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username is users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(uri_for('home'))
        else:
            flash ('Invalid username or password')
            return redirect(url_for('login'))
        return render_templates('login.html')
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
    