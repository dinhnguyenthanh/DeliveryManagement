import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Footer from './components/Footer';
import Navbar from './components/Navbar';
import About from './Pages/About';
import Customer from './Pages/Customer';
import Home from './Pages/Home';
import Service from './Pages/Service';
import Shipper from './Pages/Shipper';
import Support from './Pages/Support';


function App() {
    return (
        <>
            <BrowserRouter>
                <Navbar />
                <Routes>
                    <Route path='/' element={<Home />} />
                    <Route path='/service' element={<Service />} />
                    <Route path='/customer' element={<Customer />} />
                    <Route path='/shipper' element={<Shipper />} />
                    <Route path='/support' element={<Support />} />
                    <Route path='/about' element={<About />} />
                  </Routes>
                  <Footer />
            </BrowserRouter>
        </>
    );
}

export default App;
