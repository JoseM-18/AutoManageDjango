import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Pedido = () => {
  const [pedidos, setPedidos] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    axios.get('/api/pedidos/')
      .then(res => {
        setPedidos(res.data);
      })
      .catch(err => {
        setError('Error al cargar los pedidos');
      });
  }, []);

  const handleDelete = (id) => {
    axios.delete(`/api/pedidos/${id}/`)
      .then(res => {
        setPedidos(pedidos.filter(pedido => pedido.id !== id));
      })
      .catch(err => {
        setError('Error al eliminar el pedido');
      });
  };

  return (
    <div>
      <h1>Pedidos</h1>
      {error && <p>{error}</p>}
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Cliente</th>
            <th>Auto</th>
            <th>Fecha</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {pedidos.map(pedido => (
            <tr key={pedido.id}>
              <td>{pedido.id}</td>
              <td>{pedido.cliente}</td>
              <td>{pedido.auto}</td>
              <td>{pedido.fecha}</td>
              <td>
                <button onClick={() => handleDelete(pedido.id)}>Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Pedido;