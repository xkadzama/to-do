from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user, logout_user
from database.engine import db

profile_bp = Blueprint('profile', __name__, template_folder='templates')


@profile_bp.route('/')
@login_required
def profile():
    if current_user.is_authenticated:
        return render_template('profile.html', current_user=current_user)


@profile_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('tasks.get_all_tasks'))


@profile_bp.route('edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        if request.form.get('username'):
            current_user.username = request.form.get('username')
        if request.form.get('email'):
            current_user.email = request.form.get('email')
        db.session.commit()
        return redirect(url_for('profile.profile'))

    return render_template('edit_profile.html')









