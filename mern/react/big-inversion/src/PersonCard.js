import React from "react";

const PersonCard = (props) => {
  const { firstName, lastName, age, hairColor } = props;
  return (
    <div>
      <h3>
        {firstName} {lastName}
      </h3>
      <p>Age: {age}</p>
      <p>Hair Color: {hairColor}</p>
    </div>
  );
};

export default PersonCard;
