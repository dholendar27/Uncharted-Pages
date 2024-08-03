from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user

blog = Blueprint('blog',__name__,url_prefix='/blog', template_folder='templates/blog/')


@blog.route('/home',endpoint='home')
@login_required
def homepage():
    return render_template('home.html', user=current_user)