import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';
import Home from './components/Home';
import Product from './components/Product';
import Header from './layout/Header';

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path='/' element={<Home />}/>
        <Route path='/orderLists/:orderListId/products' element={<Product />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
