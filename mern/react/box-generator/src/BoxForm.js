import React, { useState } from "react";

const BoxForm = () => {
  const [boxes, setBoxes] = useState([]);

  const addBox = (e) => {
    e.preventDefault();
    const color = e.target[0].value;
    setBoxes([...boxes, color]);
  };

  return (
    <>
      <form
        onSubmit={(e) => {
          addBox(e);
        }}
      >
        <label for="boxColor">Color: </label>
        <input type="text" name="boxColor" id="boxColor" />
        <input type="submit" value="Add" />
      </form>
      <div>
        {boxes.map((box, i) => (
          <div
            key={i}
            style={{
              backgroundColor: box,
              width: "50px",
              height: "50px",
              display: "inline-block",
              margin: "10px",
            }}
          ></div>
        ))}
      </div>
    </>
  );
};

export default BoxForm;
