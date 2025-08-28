from flask import Blueprint, jsonify, request
import mysql.connector
from config import Config

api_bp = Blueprint("api", __name__)

# -----------------------
# Database Connection Helper
# -----------------------
def get_db_connection():
    conn = mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME
    )
    return conn


# -----------------------
# Get all tasks
# -----------------------
@api_bp.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(tasks), 200


# -----------------------
# Get a single task
# -----------------------
@api_bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    task = cursor.fetchone()

    cursor.close()
    conn.close()

    if task:
        return jsonify(task), 200
    else:
        return jsonify({"error": "Task not found"}), 404


# -----------------------
# Create new task
# -----------------------
@api_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks (title, description, priority, due_date, status)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        data.get("title"),
        data.get("description"),
        data.get("priority", "low"),
        data.get("due_date"),
        data.get("status", "todo")
    ))

    conn.commit()
    task_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return jsonify({"id": task_id, **data}), 201


# -----------------------
# Update task
# -----------------------
@api_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET title=%s, description=%s, priority=%s, due_date=%s, status=%s
        WHERE id=%s
    """, (
        data.get("title"),
        data.get("description"),
        data.get("priority"),
        data.get("due_date"),
        data.get("status"),
        task_id
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"id": task_id, **data}), 200


# -----------------------
# Delete task
# -----------------------
@api_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Task deleted"}), 200
