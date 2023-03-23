const Author = require("../models/author.model");

module.exports.findAll = (req, res) => {
  Author.find()
    .then((result) => res.json({ authors: result }))
    .catch((err) => res.status(400).json({ message: "Something went wrong", error: err }));
};

module.exports.findOne = (req, res) => {
  Author.findOne({ _id: req.params.id })
    .then((result) => res.json({ author: result }))
    .catch((err) => res.status(400).json({ message: "Something went wrong", error: err }));
};

module.exports.createOne = (req, res) => {
  Author.create(req.body)
    .then((result) => res.json({ author: result }))
    .catch((err) => res.status(400).json({ message: "Something went wrong", error: err }));
};

module.exports.updateOne = (req, res) => {
  Author.updateOne({ _id: req.params.id }, req.body, {
    new: true,
    runValidators: true,
  })
    .then((result) => res.json({ author: result }))
    .catch((err) => res.status(400).json({ message: "Something went wrong", error: err }));
};

module.exports.deleteOne = (req, res) => {
  Author.deleteOne({ _id: req.params.id })
    .then(() => res.json({ message: `Deleted author with id: ${req.params.id}` }))
    .catch((err) => res.status(400).json({ message: "Something went wrong", error: err }));
};
