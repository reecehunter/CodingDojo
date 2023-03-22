const ProductController = require("../controllers/product.controller");

module.exports = (app) => {
  app.get("/api/products", ProductController.findAll);
  app.get("/api/products/:id", ProductController.findOne);
  app.put("/api/products/:id", ProductController.updateOne);
  app.post("/api/products", ProductController.createOne);
  app.delete("/api/products/:id", ProductController.deleteOne);
};
