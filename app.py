from flask import Flask, redirect, url_for, request, flash, render_template
import os.path
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user



LISTEN_ALL = "0.0.0.0"
FLASK_IP = LISTEN_ALL
FLASK_PORT = 81
FLASK_DEBUG = True

app = Flask(__name__)

# import declared routes
import routes.authRoutes
import routes.lessons_routes

# Secret key for the session
app.secret_key = '1335eb3948fb7b64a029aa29'


# This route will redirect to the login route
@app.route("/")
def start():
    return redirect(url_for('login'))

# This route will redirect to the login route
@app.route("/index")
def index():
    return render_template(
        "index.html", name=current_user.name
    )



if __name__ == "__main__":
    app.run(host=FLASK_IP, port=FLASK_PORT, debug=FLASK_DEBUG)
