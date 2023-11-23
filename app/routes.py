from flask import jsonify, request, abort
from app import app
from app.models import Task

tasks = []

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({'tasks': [task.__dict__ for task in tasks]})

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

    # Ensure required fields are present in the request
    required_fields = ["title", "description", "completed", "due_date"]
    if not all(field in data for field in required_fields):
        abort(400, description="Missing required fields in the request")
    
    # Generate a unique ID for the new task
    new_task_id = len(tasks) + 1

    # Create a new Task object
    new_task = Task(
        id = new_task_id,
        title=data["title"],
        description=data["description"],
        completed=data["completed"],
        due_date=data["due_date"]
    )

    # Add the new task to the list of tasks
    tasks.append(new_task)
    return jsonify({'task': new_task.__dict__}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t.id == task_id), None)

    if task is None:
        abort(404, description=f'Task with ID {task_id} not found')

    data = request.get_json()

    # Update task attributes if present in the request
    for key, value in data.items():
        setattr(task, key, value)

    return jsonify({'task': task.__dict__})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]

    return jsonify({'message': f'Task with ID {task_id} has been deleted'})