import React from "react";
import Navbar from '../Navbar/Navbar';
import './Header.css';

function Header() {
    return(
        <section className="header">
            <section className="header-top">
                <section className="header-top__logo">
                    <a href="/" className="header-logo">LOGO WEB</a>
                </section>
                <section className="header-top_navbar">
                    <section className="header-top__navigation">
                        <Navbar />
                    </section>
                    <hr className="header-top__seperator"></hr>
                </section>
            </section>
            <section className="header-bottom">
                <section className="header-bottom__phone">
                    0393610575
                </section>
                <section className="header-bottom__email">
                    ship.info@gmail.com.vn
                </section>
            </section>
        </section>
    );
}

export default Header