// Modal controls
const modal = document.getElementById("taskModal");
const addTaskBtn = document.getElementById("addTaskBtn");
const closeBtn = document.querySelector(".close");
const taskForm = document.getElementById("taskForm");

addTaskBtn.onclick = () => modal.classList.remove("hidden");
closeBtn.onclick = () => modal.classList.add("hidden");

// Load tasks from API
async function loadTasks() {
  const res = await fetch("/api/tasks");
  const tasks = await res.json();

  document.querySelectorAll(".task-list").forEach(list => list.innerHTML = "");

  tasks.forEach(task => {
    renderTask(task);
  });
}

function renderTask(task) {
  const taskDiv = document.createElement("div");
  taskDiv.className = "task";
  taskDiv.draggable = true;
  taskDiv.dataset.id = task.id;

  taskDiv.innerHTML = `
    <div class="task-header">
      <strong>${task.title}</strong>
      <span class="task-priority ${task.priority}">●</span>
    </div>
    <p>${task.description || ""}</p>
    <div class="task-footer">
      Due: ${task.due_date || "N/A"}
    </div>
  `;

  document.getElementById(task.status).appendChild(taskDiv);

  // Drag events
  taskDiv.addEventListener("dragstart", () => taskDiv.classList.add("dragging"));
  taskDiv.addEventListener("dragend", () => taskDiv.classList.remove("dragging"));
}

// Handle drag & drop
document.querySelectorAll(".task-list").forEach(list => {
  list.addEventListener("dragover", e => {
    e.preventDefault();
    const dragging = document.querySelector(".dragging");
    if (dragging) list.appendChild(dragging);
  });

  list.addEventListener("drop", async e => {
    const dragging = document.querySelector(".dragging");
    if (!dragging) return;
    const newStatus = list.id;
    const taskId = dragging.dataset.id;

    // Update status via API
    await fetch(`/api/tasks/${taskId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ status: newStatus })
    });

    loadTasks();
  });
});

// Add task form
taskForm.addEventListener("submit", async e => {
  e.preventDefault();

  const task = {
    title: document.getElementById("title").value,
    description: document.getElementById("description").value,
    priority: document.getElementById("priority").value,
    due_date: document.getElementById("due_date").value,
    status: "todo"
  };

  await fetch("/api/tasks", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(task)
  });

  modal.classList.add("hidden");
  taskForm.reset();
  loadTasks();
});

// Initial load
loadTasks();
