import React from "react";
import { Link } from "react-router-dom";
function Header() {
    return(
        <>
            <Link to="/">Trang chủ</Link>
            <Link to="/orderLists/1/products">Thiết bị di động</Link>
            <Link to="/orderLists/2/products">Thiết bị iPad</Link>
            
        </>
    );
}

export default Header