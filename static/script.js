async function fetchTasks() {
  const res = await fetch("/api/tasks");
  const tasks = await res.json();

  document.getElementById("todo-list").innerHTML = "";
  document.getElementById("inprogress-list").innerHTML = "";
  document.getElementById("done-list").innerHTML = "";

  tasks.forEach(task => {
    const div = document.createElement("div");
    div.className = "task";
    div.innerHTML = `
      <h3>${task.title}</h3>
      <p>${task.description || ""}</p>
      <small>Priority: ${task.priority} | Due: ${task.due_date || "N/A"}</small>
      <br>
      <button onclick="deleteTask(${task.id})">🗑️</button>
    `;

    if (task.status === "To Do") {
      document.getElementById("todo-list").appendChild(div);
    } else if (task.status === "In Progress") {
      document.getElementById("inprogress-list").appendChild(div);
    } else {
      document.getElementById("done-list").appendChild(div);
    }
  });
}

async function addTask() {
  const task = {
    title: document.getElementById("title").value,
    description: document.getElementById("description").value,
    priority: document.getElementById("priority").value,
    due_date: document.getElementById("due_date").value,
    status: "To Do"
  };

  await fetch("/api/tasks", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(task)
  });

  fetchTasks();
}

async function deleteTask(id) {
  await fetch(`/api/tasks/${id}`, { method: "DELETE" });
  fetchTasks();
}

window.onload = fetchTasks;
