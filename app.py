from flask import Flask, render_template, request, url_for, redirect
import models

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def log():
    if request.method=='GET':
        pass
    else:
        name = request.form.get('name')
        post = request.form.get('post')
        models.create_post(name, post)
    posts = models.get_posts()
    return render_template('chat.html', posts=posts)


@app.route('/todo', methods=['GET', 'POST'])
def to_do():
    if request.method == 'GET':
        pass
    else:
        task_content = request.form['content']
        models.add_task(task_content)
    tasks = models.get_tasks()
    return render_template('todo.html', tasks=tasks)


@app.route('/todo/delete/<int:id>')
def delete(id):
    models.alter_task(id)
    return redirect('/todo')


@app.route('/todo/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        task_to_update = models.get_tasks(id)[0]
        return render_template('update.html', task=task_to_update)
    else:
        task_content = request.form['content']
        models.alter_task(id, task_content)
        return redirect('/todo')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
