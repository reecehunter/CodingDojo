const Joke = require("../models/jokes.model");

module.exports.findAllJokes = (req, res) => {
  Joke.find()
    .then((result) => res.json({ jokes: result }))
    .catch((err) => res.json({ message: "Something went wrong", error: err }));
};

module.exports.findOneJoke = (req, res) => {
  Joke.findOne({ _id: req.params.id })
    .then((result) => res.json({ joke: result }))
    .catch((err) => res.json({ message: "Something went wrong", error: err }));
};

module.exports.createOneJoke = (req, res) => {
  Joke.create(req.body)
    .then((result) => res.json({ joke: result }))
    .catch((err) => res.json({ message: "Something went wrong", error: err }));
};

module.exports.updateOneJoke = (req, res) => {
  Joke.updateOne({ _id: req.params.id }, req.body, {
    new: true,
    runValidators: true,
  })
    .then((result) => res.json({ joke: result }))
    .catch((err) => res.json({ message: "Something went wrong", error: err }));
};

module.exports.deleteOneJoke = (req, res) => {
  Joke.deleteOne({ _id: req.params.id })
    .then(() => res.json({ message: `Deleted joke ${req.params.id}` }))
    .catch((err) => res.json({ message: "Something went wrong", error: err }));
};
