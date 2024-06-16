import React, { useState, useEffect } from 'react';  
import { Container, Form, FormGroup, Label, Input, Button, Alert } from 'reactstrap';
import { useForm, Controller } from 'react-hook-form';

const AddHouseForm = () => {
  const [houseTypes, setHouseTypes] = useState([]);

  useEffect(() => {
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
  }, []);

  const { control, handleSubmit, formState: { errors }, register } = useForm();

  const onSubmit = (formData) => {
    console.log('Form submitted:', formData);
    // Handle form submission logic here
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
            placeholder="Enter name"
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
          <Input
            type="text"
            id="location"
            {...register('location', { required: 'Location is required' })}
            placeholder="Enter location"
          />
          {errors.location && <Alert color="danger">{errors.location.message}</Alert>}
        </FormGroup>
        <FormGroup>
          <Label for="image">Image URL</Label>
          <Input
            type="url"
            id="image"
            {...register('image', { required: 'Image URL is required' })}
            placeholder="Enter image URL"
          />
          {errors.image && <Alert color="danger">{errors.image.message}</Alert>}
        </FormGroup>
        <FormGroup>
          <Label for="description">Description</Label>
          <Input
            type="textarea"
            id="description"
            {...register('description', { required: 'Description is required' })}
            placeholder="Enter description"
          />
          {errors.description && <Alert color="danger">{errors.description.message}</Alert>}
        </FormGroup>
        <FormGroup>
          <Label for="yearOfBirth">Year of Birth</Label>
          <Input
            type="number"
            id="yearOfBirth"
            {...register('yearOfBirth', { required: 'Year of Birth is required' })}
            placeholder="Enter year of birth"
          />
          {errors.yearOfBirth && <Alert color="danger">{errors.yearOfBirth.message}</Alert>}
        </FormGroup>
        <Button color="primary" type="submit">Add House</Button>
      </Form>
    </Container>
  );
};

export default AddHouseForm;




