import mysql.connector
from config import Config

def create_database_and_tables():
    conn = mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD
    )
    cursor = conn.cursor()

    # Create DB if not exists
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.DB_NAME}")
    conn.database = Config.DB_NAME

    # Create tasks table
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

    conn.commit()
    conn.close()
    print("Database and tables created successfully.")

if __name__ == "__main__":
    create_database_and_tables()
