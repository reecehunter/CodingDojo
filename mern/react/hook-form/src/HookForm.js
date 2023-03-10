import React, { useState } from "react";

const HookForm = () => {
  const [state, setState] = useState({
    firstName: "",
    lastName: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const handleChange = (e) => {
    console.log(e.target.id);
    setState({
      ...state,
      [e.target.id]: e.target.value,
    });
  };

  return (
    <>
      <form>
        <input
          name="firstName"
          id="firstName"
          placeholder="First Name"
          onChange={(e) => handleChange(e)}
        />
        <input
          name="lastName"
          id="lastName"
          placeholder="Last Name"
          onChange={(e) => handleChange(e)}
        />
        <input
          name="email"
          id="email"
          placeholder="Email"
          onChange={(e) => handleChange(e)}
        />
        <input
          name="password"
          id="password"
          placeholder="Password"
          onChange={(e) => handleChange(e)}
        />
        <input
          name="confirmPassword"
          id="confirmPassword"
          placeholder="Confirm Password"
          onChange={(e) => handleChange(e)}
        />
      </form>
      <div>
        <p>First Name: {state.firstName}</p>
        <p>Last Name: {state.lastName}</p>
        <p>Email: {state.email}</p>
        <p>Password: {state.password}</p>
        <p>Confirm Password: {state.confirmPassword}</p>
      </div>
    </>
  );
};

export default HookForm;
