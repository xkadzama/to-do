from flask import Flask
from flask_login import LoginManager

from auth.routes import auth_bp
from database.authModels.models import User
from database.engine import db
from profile.routes import profile_bp
from todo.routes import tasks_bp

app = Flask(__name__)
login_manager = LoginManager()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecret'

db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = 'auth.login'

app.register_blueprint(tasks_bp, url_prefix='/tasks')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(profile_bp, url_prefix='/profile')

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()


@app.route('/')
def index():
    return 'MAIN PAGE'


if __name__ == '__main__':
    app.run(debug=True, port=8000)
