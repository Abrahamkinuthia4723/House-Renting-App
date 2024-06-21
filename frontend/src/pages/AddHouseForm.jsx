import React, { useState, useEffect } from 'react';
import { Container, Form, FormGroup, Label, Input, Button, Alert } from 'reactstrap';
import { useForm, Controller } from 'react-hook-form';

const AddHouseForm = () => {
  const [priceRanges, setPriceRanges] = useState([]);
  const [locations, setLocations] = useState([]);
  const [houseTypes, setHouseTypes] = useState([]);
  const { control, handleSubmit, formState: { errors }, register, reset } = useForm();

  useEffect(() => {
    fetchHouseTypes();
    fetchLocations();
    fetchPriceRanges();
  }, []);

  const fetchHouseTypes = () => {
    fetch(`http://localhost:8000/house_types`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
    .then((res) => res.json())
    .then((data) => {
      setHouseTypes(data);
    })
    .catch((err) => console.log(err));
  };

  const fetchLocations = () => {
    fetch(`http://localhost:8000/locations`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
    .then((res) => res.json())
    .then((data) => {
      setLocations(data);
    })
    .catch((err) => console.log(err));
  };

  const fetchPriceRanges = () => {
    fetch(`http://localhost:8000/price_ranges`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
    .then((res) => res.json())
    .then((data) => {
      setPriceRanges(data);
    })
    .catch((err) => console.log(err));
  };

  const onSubmit = (formData) => {
    console.log('Form submitted:', formData);
    fetch(`http://localhost:8000/houses`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
    .then((res) => res.json())
    .then((data) => {
      console.log('House added:', data);
      reset(); 
    })
    .catch((err) => console.error('Error adding house:', err));
  };

  return (
    <Container>
      <h2 className="mt-4 mb-4">Add House Form (In case you want to rent out your house)</h2>
      <Form onSubmit={handleSubmit(onSubmit)}>
        <FormGroup>
          <Label for="name">Name</Label>
          <Input
            type="text"
            id="name"
            {...register('name', { required: 'Name is required' })}
            placeholder="Enter your name"
          />
          {errors.name && <Alert color="danger">{errors.name.message}</Alert>}
        </FormGroup>
        <FormGroup>
          <Label for="type">Type</Label>
          <Controller
            name="type"
            control={control}
            rules={{ required: 'Type is required' }}
            render={({ field, fieldState }) => (
              <>
                <Input
                  type="select"
                  id="type"
                  {...field}
                  placeholder="Select type of house"
                >
                  <option value="">Select type of house</option>
                  {houseTypes.map((houseType) => (
                    <option key={houseType.id} value={houseType.id}>
                      {houseType.name}
                    </option>
                  ))}
                </Input>
                {fieldState.error && <Alert color="danger">{fieldState.error.message}</Alert>}
              </>
            )}
          />
        </FormGroup>
        <FormGroup>
          <Label for="location">Location</Label>
          <Controller
            name="location"
            control={control}
            rules={{ required: 'Location is required' }}
            render={({ field }) => (
              <>
                <Input
                  type="select"
                  id="location"
                  {...field}
                  placeholder="Select location"
                >
                  <option value="">Select location of the house</option>
                  {locations.map((location) => (
                    <option key={location.id} value={location.id}>
                      {location.name}
                    </option>
                  ))}
                </Input>
              </>
            )}
          />
          {errors.location && <Alert color="danger">{errors.location.message}</Alert>}
        </FormGroup>
        <FormGroup>
          <Label for="price">Price Range</Label>
          <Controller
            name="price"
            control={control}
            rules={{ required: 'Price Range is required' }}
            render={({ field }) => (
              <Input
                type="select"
                id="price"
                {...field}
                placeholder="Select price range"
              >
                <option value="">Select price range for expected rent per day</option>
                {priceRanges.map((range) => (
                  <option key={range.id} value={range.id}>
                    ${range.min_price} - ${range.max_price}
                  </option>
                ))}
              </Input>
            )}
          />
          {errors.price && <Alert color="danger">{errors.price.message}</Alert>}
        </FormGroup>
        <FormGroup>
          <Label for="image">Image URL</Label>
          <Input
            type="url"
            id="image"
            {...register('image', { required: 'Image URL is required' })}
            placeholder="Enter image URL of the house"
          />
          {errors.image && <Alert color="danger">{errors.image.message}</Alert>}
        </FormGroup>
        <FormGroup>
          <Label for="description">Description</Label>
          <Input
            type="textarea"
            id="description"
            {...register('description', { required: 'Description is required' })}
            placeholder="Enter description of the house"
          />
          {errors.description && <Alert color="danger">{errors.description.message}</Alert>}
        </FormGroup>
        <FormGroup>
          <Label for="yearOfBirth">Year of Birth</Label>
          <Input
            type="number"
            id="yearOfBirth"
            {...register('yearOfBirth', { required: 'Year of Birth is required' })}
            placeholder="Enter your year of birth"
          />
          {errors.yearOfBirth && <Alert color="danger">{errors.yearOfBirth.message}</Alert>}
        </FormGroup>
        <Button color="primary" type="submit">Add House</Button>
      </Form>
    </Container>
  );
};

export default AddHouseForm;


