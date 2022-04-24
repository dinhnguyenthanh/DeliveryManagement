import React from "react"
import { Link } from "react-router-dom"
import './Navbar.css';

function Navbar() {
    return(
        <section>
            <Link to="/" className="navbar-item">Trang chủ</Link>
            <Link to="/orderLists/1/products"className="navbar-item">Thiết bị di động</Link>
            <Link to="/orderLists/2/products"className="navbar-item">Thiết bị Tablet</Link>
            <Link to="/orderLists/3/products"className="navbar-item">Thiết bị Laptop</Link>
        </section>
    )
}

export default Navbar