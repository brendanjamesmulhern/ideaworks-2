import React from 'react';
import Nav from '../components/nav';
import Footer from '../components/footer';
import { useState, useEffect } from 'react';
import Login from '../screens/Login';

export default function Home() {
  const [loggedIn, setLoggedIn] = useState(false);
  return (
    <div style={{ height: '100vh', width: '100vw', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', alignItems: 'center' }}>
      <Nav />
      <div style={{ backgroundColor: 'gray', height: '80vh', overflowY: 'scroll', width: '100vw', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center' }}>
          <Login loggedIn={loggedIn} setLoggedIn={setLoggedIn} />

          { loggedIn && <h1>You are logged in!</h1> }
      </div>
      <Footer />
    </div>
  )
};