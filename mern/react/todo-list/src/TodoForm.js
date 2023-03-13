import React from "react";

const TodoForm = (props) => {
  const addToForm = (e) => {
    e.preventDefault();
    props.setTasks([
      ...props.tasks,
      { label: e.target[0].value, complete: false },
    ]);
  };

  return (
    <form onSubmit={(e) => addToForm(e)}>
      <input type="text" name="label" id="label" />
      <input type="submit" value="Add" />
    </form>
  );
};

export default TodoForm;
