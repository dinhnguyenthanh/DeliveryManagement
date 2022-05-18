import React from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Home from '../Pages/Home'
import Customer from '../Pages/Customer'
import Service from '../Pages/Service'
import Shipper from '../Pages/Shipper'
import Support from '../Pages/Support'
import Footer from './Footer'
import Navbar from './Navbar'
import Header from './Header'

const Body = () => {
    return(
        <BrowserRouter>
            <Header />
            <Navbar />
            <Routes>
                <Route exact path='/'element={<Home />} />
                <Route exact path='/service' element={<Service />}/>
                <Route exact path='/customer' element={<Customer />}/>
                <Route exact path='/shipper' element={<Shipper />}/>
                <Route exact path='/support' element={<Support />}/>
            </Routes>
            <Footer />
        </BrowserRouter>
    )
}

export default Body;

