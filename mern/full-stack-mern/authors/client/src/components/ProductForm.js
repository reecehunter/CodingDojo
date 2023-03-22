import React from "react";

const ProductForm = (props) => {
  const { submitCallback, title = "", price = 0, description = "" } = props;

  return (
    <form className="container" onSubmit={(e) => submitCallback(e)}>
      <input
        type="text"
        name="title"
        id="title"
        placeholder="Title"
        defaultValue={title}
      />
      <input
        type="number"
        name="price"
        id="price"
        placeholder="1"
        defaultValue={price}
      />
      <input
        type="text"
        name="description"
        id="description"
        placeholder="Description"
        defaultValue={description}
      />
      <input type="submit" value="Add Product" />
    </form>
  );
};

export default ProductForm;
