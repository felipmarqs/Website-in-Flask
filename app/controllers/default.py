from flask import Flask, render_template, flash, redirect, url_for
from flask import Blueprint
from app import create_app, db, login_manager
from flask_login import login_user, LoginManager, logout_user

from app.models.tables import User  
from app.models.forms import LoginForm

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

default_bp = Blueprint('default', __name__)

'''Função para definir rotas do site  '''
@default_bp.route("/index")
@default_bp.route("/")
def index():
    return render_template('index.html')

@default_bp.route("/login/", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("default.index"))
            flash("Logged in.")
        else:
            flash("Invalid login")
    else:
        print(form.errors)
    return render_template('login.html',
                           form=form)

@default_bp.route("/teste/<info>")
@default_bp.route("/teste",defaults={"info": None})
def teste(info):
    r = User.query.filter_by(username="georgia").first()
    r.name = "Georgia"
    db.session.add(r)
    db.session.commit()
    return "ok"




@default_bp.route("/logout")
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("default.index"))

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)