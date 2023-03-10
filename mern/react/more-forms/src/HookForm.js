import React, { useState } from "react";

const HookForm = () => {
  const [state, setState] = useState({
    firstName: "",
    lastName: "",
    email: "",
    password: "",
    confirmPassword: "",
  });
  const [error, setError] = useState([]);

  const handleChange = (e) => {
    setState({
      ...state,
      [e.target.id]: e.target.value,
    });
  };

  return (
    <>
      <form>
        {state.firstName.length < 2 && state.firstName.length > 0 && (
          <p className="red">First name must be at least 2 characters.</p>
        )}
        <input
          name="firstName"
          id="firstName"
          placeholder="First Name"
          onChange={(e) => handleChange(e)}
        />

        {state.lastName.length < 2 && state.lastName.length > 0 && (
          <p className="red">Last name must be at least 2 characters.</p>
        )}
        <input
          name="lastName"
          id="lastName"
          placeholder="Last Name"
          onChange={(e) => handleChange(e)}
        />

        {state.email.length < 5 && state.email.length > 0 && (
          <p className="red">Email must be at least 5 characters.</p>
        )}
        <input
          name="email"
          id="email"
          placeholder="Email"
          onChange={(e) => handleChange(e)}
        />

        {state.password.length < 8 && state.password.length > 0 && (
          <p className="red">Password must be at least 8 characters.</p>
        )}
        <input
          name="password"
          id="password"
          placeholder="Password"
          onChange={(e) => handleChange(e)}
        />

        {state.confirmPassword !== state.password &&
          state.confirmPassword.length > 0 && (
            <p className="red">Passwords must match.</p>
          )}
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
