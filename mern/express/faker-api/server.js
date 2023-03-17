const express = require("express");
const { faker } = require("@faker-js/faker");

const app = express();
const port = 8000;

app.get("/api/users/new", (req, res) => {
  const user = createUser(
    faker.datatype.uuid(),
    faker.name.firstName(),
    faker.name.lastName(),
    faker.internet.email(),
    faker.internet.password()
  );
  res.json(user);
});

app.get("/api/companies/new", (req, res) => {
  const company = createCompany(faker.datatype.uuid(), faker.company.name(), {
    street: faker.address.streetName(),
    city: faker.address.city(),
    state: faker.address.state(),
    zipCode: faker.address.zipCode(),
    country: faker.address.country(),
  });
  res.json(company);
});

app.get("/api/company", (req, res) => {
  const user = createUser(
    faker.datatype.uuid(),
    faker.name.firstName(),
    faker.name.lastName(),
    faker.internet.email(),
    faker.internet.password()
  );
  const company = createCompany(faker.datatype.uuid(), faker.company.name(), {
    street: faker.address.street(),
    city: faker.address.city(),
    state: faker.address.state(),
    zipCode: faker.address.zipCode(),
    country: faker.address.country(),
  });
  res.json({ company, user });
});

const createUser = (_id, firstName, lastName, phoneNumber, email, password) => {
  return {
    _id,
    firstName,
    lastName,
    phoneNumber,
    email,
    password,
  };
};

const createCompany = (_id, name, address) => {
  return {
    _id,
    name,
    address,
  };
};

app.listen(port, () => console.log(`Listening on port ${port}`));
