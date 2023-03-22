import React from "react";
import { Link } from "react-router-dom";
import DeleteButton from "./DeleteButton";

const ProductList = (props) => {
  const { products, setProducts } = props;

  const filterList = (id) => {
    const filteredList = products.filter((product) => product._id !== id);
    setProducts(filteredList);
  };

  return (
    <>
      {products.map((product, index) => (
        <div key={index} className="product">
          <Link to={`/${product._id}`}>{product.title}</Link>
          <DeleteButton
            id={product._id}
            onDelete={() => filterList(product._id)}
          />
        </div>
      ))}
    </>
  );
};

export default ProductList;
