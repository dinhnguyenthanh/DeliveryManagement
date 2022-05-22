import React from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Home from '../pages/Home'
import Header from './Header'
import Footer from './Footer'
import Service from '../pages/Service'

const Body = () => {
    return (
        <BrowserRouter>
            <Header />
            <Routes>
                <Route exact path='/' element={<Home />} />
                <Route axact path='/categoryitems/:categoryId/goodss/' element={<Service />} />
            </Routes>
            <Footer />
        </BrowserRouter>
    )
}

export default Body