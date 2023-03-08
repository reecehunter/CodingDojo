import "./App.css";
import React, { Component } from "react";

class Person extends Component {
  constructor(props) {
    super(props);
    this.state = {
      age: props.age,
    };
  }

  render() {
    const { firstName, lastName, age, hairColor } = this.props;
    return (
      <div className="App">
        <h1>
          {lastName} {firstName}
        </h1>
        <p>Age: {this.state.age}</p>
        <p>Hair Color: {hairColor}</p>
        <button
          onClick={() => {
            this.setState({
              age: parseInt(this.state.age) + 1,
            });
          }}
        >
          Increment Age for {firstName}
        </button>
      </div>
    );
  }
}

export default Person;
