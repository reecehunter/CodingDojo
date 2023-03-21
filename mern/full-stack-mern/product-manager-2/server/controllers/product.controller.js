const Product = require("../models/product.model");

module.exports.findAll = (req, res) => {
  Product.find()
    .then((result) => res.json({ products: result }))
    .catch((err) => res.json({ message: "Something went wrong", error: err }));
};

module.exports.findOne = (req, res) => {
  Product.findOne({ _id: req.params.id })
    .then((result) => res.json({ product: result }))
    .catch((err) => res.json({ message: "Something went wrong", error: err }));
};

module.exports.createOne = (req, res) => {
  Product.create(req.body)
    .then((result) => res.json({ product: result }))
    .catch((err) => res.json({ message: "Something went wrong", error: err }));
};

module.exports.updateOne = (req, res) => {
  Product.updateOne({ _id: req.params.id }, req.body, {
    new: true,
    runValidators: true,
  })
    .then((result) => res.json({ product: result }))
    .catch((err) => res.json({ message: "Something went wrong", error: err }));
};

module.exports.deleteOne = (req, res) => {
  Product.deleteOne({ _id: req.params.id })
    .then(() =>
      res.json({ message: `Deleted product with id: ${req.params.id}` })
    )
    .catch((err) => res.json({ message: "Something went wrong", error: err }));
};
