# Import os.path module
import os.path


# Import Flask
from flask import Flask, redirect, url_for, request, flash, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user


# Import Werkzeug security
from werkzeug.security import generate_password_hash, check_password_hash


# Import from app.py
from __main__ import app, render_template, request, \
    SQLAlchemy, os, UserMixin, flash, redirect, url_for, \
    generate_password_hash, check_password_hash, login_user, logout_user, LoginManager, login_required


# This route will redirect to the lessons index route
@app.route("/lessen_overzicht")
def lessons_index():
    return render_template(
        "lessons/index.html"
    )
