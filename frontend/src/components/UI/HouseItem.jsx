import React from "react";
import { Col } from "reactstrap";
import "../../styles/house-item.css";

const HouseItem = (props) => {
  const { name, imgUrl, rating, price, description } = props.item;

  return (
    <Col lg="4" md="4" sm="6" className="mb-5">
      <div className="house__item">
        <div className="house__img">
          <img src={imgUrl} alt={name} style={{ width: "100%", height: "280px",  }} />
        </div>

        <div className="house__item-content mt-4">
          <h6 className="rent__price text-center mt-2">
            sh {price}.00 <span>/ Day</span>
          </h6>
          <p className="text-center mb-0">{name}</p>
          <div className="text-center">
            {[...Array(Math.floor(rating))].map((_, index) => (
              <i key={index} className="ri-star-s-fill"></i>
            ))}
            {rating % 1 !== 0 && (
              <i className="ri-star-s-half-fill"></i>
            )}
          </div>
          <p className="text-center mt-2">{description}</p>
        </div>
      </div>
    </Col>
  );
};

export default HouseItem;
