import "./App.css";
import React, { Component } from "react";

class Person extends Component {
  render() {
    const { firstName, lastName, age, hairColor } = this.props;

    return (
      <div className="App">
        <h1>
          {lastName} {firstName}
        </h1>
        <p>Age: {age}</p>
        <p>Hair Color: {hairColor}</p>
      </div>
    );
  }
}

export default Person;
