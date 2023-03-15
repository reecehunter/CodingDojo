import React from "react";
import { useParams } from "react-router-dom";

const Word = () => {
  const { word, color1, color2 } = useParams();

  return (
    <div
      style={
        isNaN(color1)
          ? { backgroundColor: color1 }
          : { backgroundColor: "transparent" }
      }
    >
      <h1 style={isNaN(color1) ? { color: color2 } : { color: "black" }}>
        {word}
      </h1>
    </div>
  );
};

export default Word;
