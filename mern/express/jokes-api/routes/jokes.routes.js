const JokeController = require("../controllers/jokes.controller");

module.exports = (app) => {
  app.get("/api/jokes", JokeController.findAllJokes);
  app.get("/api/jokes/:id", JokeController.findOneJoke);
  app.put("/api/jokes/:id", JokeController.updateOneJoke);
  app.post("/api/jokes", JokeController.createOneJoke);
  app.delete("/api/jokes/:id", JokeController.deleteOneJoke);
};
