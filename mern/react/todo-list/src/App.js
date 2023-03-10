import React, { useState } from "react";
import "./App.css";
import Task from "./Task";
import TodoForm from "./TodoForm";

function App() {
  const [tasks, setTasks] = useState([]);

  const deleteTask = (label) => {
    setTasks(tasks.filter((task) => task.label !== label));
  };

  return (
    <div className="container">
      <TodoForm tasks={tasks} setTasks={setTasks} />
      <div id="tasks">
        {tasks.map((task, idx) => (
          <Task
            key={idx}
            tasks={tasks}
            setTasks={setTasks}
            label={task.label}
            complete={task.complete}
            onDelete={deleteTask}
          />
        ))}
      </div>
    </div>
  );
}

export default App;
