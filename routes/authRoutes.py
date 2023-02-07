from __main__ import app, render_template, request, \
    SQLAlchemy, os, UserMixin, flash, redirect, url_for, \
    generate_password_hash, check_password_hash, login_user, logout_user, LoginManager, login_required

# This command creates the "<application directory>/databases/hogeschool_rotterdam.db" path
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(app.root_path, 'databases', 'hogeschool_rotterdam.db')
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = "De gebruiker moet ingelogd zijn om deze pagina te bekijken"

# Database model for the user
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# This route will display the login view
@app.route('/login')
def login():
    return render_template(
        "/auth/login.html"
    )


# Het inladen van de users
@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


# This route will display the sign up view
@app.route('/signup')
def signup():
    return render_template(
        "/auth/signup.html"
    )


# This route will trigger the singup request
@app.route('/signupReq', methods=['POST'])
def signup_post():
    # Gets the data of the request
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(
        email=email).first()  # Checks if email already exist

    if user:
        flash('Email is al in gebruik')
        return redirect(url_for('signup'))

    if name == '':
        flash('Vul alle velden in')
        return redirect(url_for('signup'))

    # Makes a new users ands hashed the password
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # Adds user to db
    db.session.add(new_user)
    db.session.commit()

    # Send client to login view
    return redirect(url_for('login'))


# This route will trigger the login request
@app.route('/loginReq', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    # Checks if user exist
    if not user or not check_password_hash(user.password, password):
        flash('Controleer uw inloggegevens en probeer het opnieuw.')
        return redirect(url_for('login'))  # Als de user niet bestaat gaat hij naar de login pagina

    # Will log the user in
    login_user(user)

    return redirect(url_for('index'))


# Het
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

