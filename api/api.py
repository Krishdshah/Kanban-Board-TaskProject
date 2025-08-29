from flask import Blueprint, request, jsonify
from models.task_model import get_db_connection

api_bp = Blueprint("api", __name__)

# GET all tasks
@api_bp.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return jsonify(tasks)

# ADD a new task
@api_bp.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, priority, due_date, status) VALUES (%s, %s, %s, %s, %s)",
        (data["title"], data.get("description",""), data.get("priority","Low"), data.get("due_date", None), data.get("status","To Do"))
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Task added successfully!"}), 201

# UPDATE task
@api_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET title=%s, description=%s, priority=%s, due_date=%s, status=%s WHERE id=%s",
        (data["title"], data["description"], data["priority"], data["due_date"], data["status"], task_id)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Task updated successfully!"})

# DELETE task
@api_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task deleted successfully!"})
