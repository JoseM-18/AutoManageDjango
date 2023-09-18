import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div>
      <h1>Bienvenido al Concesionario de Automóviles</h1>
      <p>Seleccione una opción:</p>
      <ul>
        <li><Link to="/inventario">Inventario</Link></li>
        <li><Link to="/pedido">Pedidos</Link></li>
      </ul>
    </div>
  );
}

export default Home;