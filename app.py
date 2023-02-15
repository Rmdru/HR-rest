<<<<<<< HEAD
from flask import Flask, redirect, url_for, request, flash, render_template, jsonify, send_from_directory
import os.path
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import mimetypes


=======
from flask import Flask, redirect, url_for, request, flash, render_template, send_file
import os.path
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
>>>>>>> origin/qrCode
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user

LISTEN_ALL = "0.0.0.0"
FLASK_IP = LISTEN_ALL
FLASK_PORT = 81
FLASK_DEBUG = True

app = Flask(__name__)

# Add custom MIME type for JavaScript files, so we can use the import function
@app.route('/static/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path, mimetype='application/javascript')


# This command creates the "<application directory>/databases/hogeschool_rotterdam.db" path
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(app.root_path, 'databases', 'hogeschool_rotterdam.db')
db.init_app(app)

# import declared routes
import routes.authRoutes
<<<<<<< HEAD
import routes.lessonRoutes
routes.lessonRoutes.setup_lesson_routes(app)
routes.authRoutes.setup_auth_routes(app)
=======
import routes.qrRoutes
>>>>>>> origin/qrCode

# Secret key for the session
app.secret_key = '1335eb3948fb7b64a029aa29'


# This route will redirect to the login route
@app.route("/")
def start():
    return redirect(url_for('login'))

<<<<<<< HEAD
=======

# This route will redirect to the login route
>>>>>>> origin/qrCode
@app.route("/index")
def index():
    return render_template(
        "index.html", name=current_user.name
    )

<<<<<<< HEAD
=======

>>>>>>> origin/qrCode
if __name__ == "__main__":
    app.run(host=FLASK_IP, port=FLASK_PORT, debug=FLASK_DEBUG)
