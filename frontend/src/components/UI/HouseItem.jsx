import React, { useState } from "react";
import { Col, Button, Modal, ModalHeader, ModalBody, ModalFooter } from "reactstrap";
import "../../styles/house-item.css";

const HouseItem = ({ item, onUpdate, onDelete }) => {
  const { name, imgUrl, rating, price, description } = item;

  const [modal, setModal] = useState(false);
  const toggle = () => setModal(!modal);

  const [formData, setFormData] = useState({
    name: name,
    imgUrl: imgUrl,
    rating: rating,
    price: price,
    description: description,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onUpdate(formData);
    toggle();
  };

  return (
    <Col lg="4" md="6" sm="12" className="mb-4">
      <div className="house-item text-center">
        <div className="house-img">
          <img src={imgUrl} alt={name} className="img-fluid" style={{ height: "280px", objectFit: "cover" }} />
        </div>

        <div className="house-item-content mt-3">
          <h5 className="house-name">{name}</h5>
          <div className="house-rating mb-2">
            {[...Array(Math.floor(rating))].map((_, index) => (
              <i key={index} className="ri-star-s-fill"></i>
            ))}
            {rating % 1 !== 0 && <i className="ri-star-s-half-fill"></i>}
          </div>
          <p className="house-description">{description}</p>
          <h6 className="house-price">
            sh {price}.00 <span>/ Day</span>
          </h6>

          <div className="d-flex justify-content-center mt-3">
            <Button color="primary" onClick={toggle} className="mx-2">
              Update
            </Button>{" "}
            <Button color="danger" onClick={() => onDelete(item.id)} className="mx-2">
              Delete
            </Button>
          </div>

          <Modal isOpen={modal} toggle={toggle} centered>
            <ModalHeader toggle={toggle}>Update House Item</ModalHeader>
            <ModalBody>
              <form onSubmit={handleSubmit}>
                <div className="form-group">
                  <label htmlFor="name">Name</label>
                  <input
                    type="text"
                    className="form-control"
                    id="name"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="imgUrl">Image URL</label>
                  <input
                    type="text"
                    className="form-control"
                    id="imgUrl"
                    name="imgUrl"
                    value={formData.imgUrl}
                    onChange={handleChange}
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="rating">Rating</label>
                  <input
                    type="number"
                    className="form-control"
                    id="rating"
                    name="rating"
                    value={formData.rating}
                    onChange={handleChange}
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="price">Price</label>
                  <input
                    type="number"
                    className="form-control"
                    id="price"
                    name="price"
                    value={formData.price}
                    onChange={handleChange}
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="description">Description</label>
                  <textarea
                    className="form-control"
                    id="description"
                    name="description"
                    value={formData.description}
                    onChange={handleChange}
                  />
                </div>
                <ModalFooter className="justify-content-center">
                  <Button color="primary" type="submit">
                    Save Changes
                  </Button>{" "}
                  <Button color="secondary" onClick={toggle}>
                    Cancel
                  </Button>
                </ModalFooter>
              </form>
            </ModalBody>
          </Modal>
        </div>
      </div>
    </Col>
  );
};

export default HouseItem;
