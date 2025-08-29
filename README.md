# 📝 Kanban Board - Task Management App

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/flask-2.3+-green.svg)](https://flask.palletsprojects.com/)  
[![MySQL](https://img.shields.io/badge/mysql-8.0+-yellow.svg)](https://www.mysql.com/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)  

A simple and colorful **Kanban Board** web application built with **Flask (Python)**, **MySQL**, and **HTML/CSS/JavaScript**.  
It helps users organize tasks visually using columns like **To Do**, **In Progress**, and **Done**.  

---

## ✨ Features
- 🗂️ **Task Management**  
  - Create, update, and delete tasks  
  - Fields: Title, Description, Priority, Due Date  
- 📌 **Drag & Drop** between columns  
- 🔍 **Sorting & Filtering** by due date, priority, or category  
- 💾 **Persistent Storage** with **MySQL**  
- 🎨 **Responsive & Colorful UI**  
- 🔧 **Extensible for Future Features**:
  - Multiple boards  
 # Upcoming:
  - Multi-user collaboration  
  - Cloud Sync

---

## 🛠️ Tech Stack
**Frontend:** HTML, CSS, JavaScript  
**Backend:** Python (Flask)  
**Database:** MySQL (`mysql-connector-python`)  

---

## 📂 Project Structure

Kanban-Board/
│── app.py
│── config.py
│── create_tables.py
│── requirements.txt
│── .env.example
│── .gitignore
│
├── api/
│ └── api.py
├── models/
│ └── task_model.py
├── templates/
│ └── index.html
└── static/
├── style.css
└── script.js

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Krishdshah/Kanban-Board-TaskProject.git
cd Kanban-Board-TaskProject
```
### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # for Windows
source venv/bin/activate   # for macOS/Linux
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣creating Database
## 1.Create a MySQL database (or just run create_table.py).
## 2.Update config.py with your MySQL id and pswd:

```bash
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'kanban_db'
}
 python run create_table.py
```

### FINALLY : RUN THE APP
```bash
python app.py
```

🎨 UI Preview

Colorful Kanban Columns (To Do, In Progress, Done)

Drag & Drop Support

Priority-based Task Colors

(Add screenshots here once UI is running)

🚀 Future Enhancements

🔑 User authentication

📋 Multiple boards per user

☁️ Cloud sync for multi-device access

⚡ Real-time collaboration with WebSockets

👨‍💻 Author

Krish D Shah
🔗 Portfolio : krishdshah.github.io/portfolio | GitHub: Krishdshah | LinkedIn: thekrishdshah

##--------------THE END--------------------------##