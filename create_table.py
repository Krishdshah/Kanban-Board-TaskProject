import mysql.connector
from config import Config

def create_tables():
    connection = mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD
    )
    cursor = connection.cursor()

    # Create Database if not exists
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.DB_NAME}")
    cursor.execute(f"USE {Config.DB_NAME}")

    # Create Tasks Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT,
        priority ENUM('Low','Medium','High') DEFAULT 'Low',
        due_date DATE,
        status ENUM('To Do','In Progress','Done') DEFAULT 'To Do'
    )
    """)

    connection.commit()
    cursor.close()
    connection.close()
    print("✅ Database and tables created successfully!")

if __name__ == "__main__":
    create_tables()
