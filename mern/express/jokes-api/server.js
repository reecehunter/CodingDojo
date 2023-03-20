const express = require("express");
require("dotenv").config();

const app = express();
const port = process.env.PORT;

require("./config/mongoose.config");

app.use(express.json(), express.urlencoded({ extended: true }));

const AllJokeRoutes = require("./routes/jokes.routes");
AllJokeRoutes(app);

app.listen(port, () => console.log(`Listening on port ${port}`));
