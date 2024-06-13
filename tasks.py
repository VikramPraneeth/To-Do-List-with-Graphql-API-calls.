from app.models import Todo

def get_all_todos(user):
    return Todo.query.all()

def get_todo_by_id(user, id):
    return Todo.query.get(id)

def create_todo(user, title, description, due_time, image=None):  # Add image for pro
