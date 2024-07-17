from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Boolean, default=False)  # False for active, True for completed

    def __repr__(self):
        return f'<Todo {self.id}>'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo_content = request.form['content']
    new_todo = Todo(content=todo_content)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/toggle/<int:id>', methods=['POST'])
def toggle(id):
    todo = Todo.query.get_or_404(id)
    todo.status = not todo.status
    db.session.commit()
    return jsonify({'status': todo.status})

if __name__ == '__main__':
    app.run(debug=True)