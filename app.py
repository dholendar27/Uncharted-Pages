from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "[Fx,Iuhv3oq]NtTGO[i_@cxm(h1O19'i2[a"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    from main import api
    app.register_blueprint(api,url_prefix='/')

    from auth import auth
    app.register_blueprint(auth,url_prefix='/auth')

    from blog import blog
    app.register_blueprint(blog,url_prefix="/blog")

    return app

   
if __name__ == "__main__":
    
    app = create_app()
    app.run(debug=True)