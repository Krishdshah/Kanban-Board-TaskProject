async function loadTasks() {
  const res = await fetch("/api/tasks");
  const tasks = await res.json();

  document.getElementById("todo").innerHTML = "";
  document.getElementById("inprogress").innerHTML = "";
  document.getElementById("done").innerHTML = "";

  tasks.forEach(task => {
    let div = document.createElement("div");
    div.className = "task";
    div.textContent = `${task.title} (${task.priority})`;
    document.getElementById(task.status.replace(" ", "").toLowerCase()).appendChild(div);
  });
}

document.addEventListener("DOMContentLoaded", loadTasks);
