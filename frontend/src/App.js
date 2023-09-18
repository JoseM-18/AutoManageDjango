import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import Inventario from './components/Inventario';
import Pedido from './components/Pedido';
import Error from './components/Error';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/inventario" component={Inventario} />
        <Route path="/pedido" component={Pedido} />
        <Route component={Error} />
      </Switch>
    </Router>
  );
}

export default App;