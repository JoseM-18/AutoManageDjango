import React from 'react';
import { Link } from 'react-router-dom';

const Error = () => {
  return (
    <div className="error">
      <h2>Oops! Something went wrong.</h2>
      <p>We're sorry, but there was an error processing your request.</p>
      <Link to="/" className="btn btn-primary">Go back to home</Link>
    </div>
  );
};

export default Error;