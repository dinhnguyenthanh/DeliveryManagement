import React , {useEffect} from 'react';
import '../Static/Navbar.css';
import { Link } from 'react-router-dom';
import $ from 'jquery';
import { Button, ButtonGroup, Container, Nav } from 'react-bootstrap';
import '../json/data.json'

const Navbar = () => {

    function animation(){
        var tabsNewAnim = $('#navbarSupportedContent');
        var activeItemNewAnim = tabsNewAnim.find('.active');
        var activeWidthNewAnimHeight = activeItemNewAnim.innerHeight();
        var activeWidthNewAnimWidth = activeItemNewAnim.innerWidth();
        var itemPosNewAnimTop = activeItemNewAnim.position();
        var itemPosNewAnimLeft = activeItemNewAnim.position();

        $(".hori-selector").css({
            "top":itemPosNewAnimTop.top + "px", 
            "left":itemPosNewAnimLeft.left + "px",
            "height": activeWidthNewAnimHeight + "px",
            "width": activeWidthNewAnimWidth + "px"
        });

        $("#navbarSupportedContent").on("click","li",function(e){
            $('#navbarSupportedContent ul li').removeClass("active");
                $(this).addClass('active');
                var activeWidthNewAnimHeight = $(this).innerHeight();
                var activeWidthNewAnimWidth = $(this).innerWidth();
                var itemPosNewAnimTop = $(this).position();
                var itemPosNewAnimLeft = $(this).position();
                $(".hori-selector").css({
                    "top":itemPosNewAnimTop.top + "px", 
                    "left":itemPosNewAnimLeft.left + "px",
                    "height": activeWidthNewAnimHeight + "px",
                    "width": activeWidthNewAnimWidth + "px"
            });
        });
    }

    useEffect(() => {
        animation();
        $(window).on('resize', function(){
            setTimeout(function(){ 
                animation(); 
            }, 500);
        });
    }, []);


    return (
        <Nav className="navbar navbar-expand-lg navbar-mainbg">
            <Container>
                <button className="navbar-toggler"
                        onClick={ function(){
                            setTimeout(function(){ 
                                animation(); 
                            });
                    }}
                    type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <i className="fas fa-bars text-white"></i>
                </button>
            
                <div 
                    className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav ml-auto">
                        <div className="hori-selector">
                            <div className="left"></div>
                            <div className="right"></div>
                        </div>
                        
                        <li className="nav-item active">
                            <Link className="nav-link" to="/">
                                <i className="fas fa-home"></i>
                                Trang Ch???
                            </Link>
                        </li>

                        <li className="nav-item">
                            <Link className="nav-link" to="/service">
                                <i className="fab fa-servicestack"></i>
                                D???ch v???
                            </Link> 
                        </li>

                        <li className="nav-item">
                            <Link className="nav-link" to="/customer" >
                                <i className="far fa-address-book"> </i>
                                Kh??ch h??ng
                            </Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to="/shipper" >
                                <i className="fas fa-shipping-fast"></i>
                                T??i x???
                            </Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to="/support" >
                                <i className="fas fa-envelope-open"></i>
                                H??? tr???
                            </Link>
                        </li>
                    </ul>
                </div>
                <div className='main-login'>
                    <ButtonGroup size='sm'>
                        <Button className='registor'>????ng k??</Button>
                        <Button className='login'>????ng nh???p</Button>
                    </ButtonGroup>
                </div>
            </Container>
        </Nav>
        
    )
}
export default Navbar;