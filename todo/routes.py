from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user
from database.todoModels.models import Task
from database.engine import db

tasks_bp = Blueprint('tasks', __name__, template_folder='templates')

@tasks_bp.route('/')
def get_all_tasks():
    tasks_list = Task.query.all()
    print(tasks_list)
    return render_template('todo.html', tasks_list=tasks_list, current_user=current_user)


@tasks_bp.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form.get('title')
        task = Task(title=title)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('tasks.get_all_tasks'))
    return render_template('add_task.html')


@tasks_bp.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    Task.query.filter_by(id=task_id).delete()
    db.session.commit()
    return redirect(url_for('tasks.get_all_tasks'))