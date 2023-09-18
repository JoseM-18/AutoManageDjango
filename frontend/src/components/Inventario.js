import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Inventario = () => {
  const [cars, setCars] = useState([]);
  const [newCar, setNewCar] = useState({
    make: '',
    model: '',
    year: '',
    price: '',
  });

  useEffect(() => {
    axios.get('/api/cars/')
      .then(res => {
        setCars(res.data);
      })
      .catch(err => {
        console.log(err);
      });
  }, []);

  const handleChange = e => {
    setNewCar({
      ...newCar,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = e => {
    e.preventDefault();
    axios.post('/api/cars/', newCar)
      .then(res => {
        setCars([...cars, res.data]);
        setNewCar({
          make: '',
          model: '',
          year: '',
          price: '',
        });
      })
      .catch(err => {
        console.log(err);
      });
  };

  const handleDelete = id => {
    axios.delete(`/api/cars/${id}/`)
      .then(res => {
        setCars(cars.filter(car => car.id !== id));
      })
      .catch(err => {
        console.log(err);
      });
  };

  return (
    <div>
      <h1>Inventario</h1>
      <table>
        <thead>
          <tr>
            <th>Marca</th>
            <th>Modelo</th>
            <th>Año</th>
            <th>Precio</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {cars.map(car => (
            <tr key={car.id}>
              <td>{car.make}</td>
              <td>{car.model}</td>
              <td>{car.year}</td>
              <td>{car.price}</td>
              <td>
                <button onClick={() => handleDelete(car.id)}>Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <h2>Agregar carro</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Marca:
          <input type="text" name="make" value={newCar.make} onChange={handleChange} />
        </label>
        <label>
          Modelo:
          <input type="text" name="model" value={newCar.model} onChange={handleChange} />
        </label>
        <label>
          Año:
          <input type="text" name="year" value={newCar.year} onChange={handleChange} />
        </label>
        <label>
          Precio:
          <input type="text" name="price" value={newCar.price} onChange={handleChange} />
        </label>
        <button type="submit">Agregar</button>
      </form>
    </div>
  );
};

export default Inventario;