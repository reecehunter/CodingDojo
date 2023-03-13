import React from "react";

const Task = (props) => {
  const deleteTask = () => {
    props.setTasks(props.tasks.filter((task) => task.label !== props.label));
  };

  const toggleComplete = () => {
    const updatedTasks = props.tasks.map((task, idx) => {
      if (task.label === props.label) task.complete = !task.complete;
      return task;
    });
    console.log(updatedTasks);
    props.setTasks(updatedTasks);
  };

  return (
    <div className="task">
      <p>{props.label}</p>
      <input
        type="checkbox"
        onChange={toggleComplete}
        checked={props.complete}
      />
      <button onClick={deleteTask}>Delete</button>
    </div>
  );
};

export default Task;
