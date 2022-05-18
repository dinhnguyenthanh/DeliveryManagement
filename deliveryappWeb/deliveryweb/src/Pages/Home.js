import React from 'react'
import { Button, Card, Carousel } from 'react-bootstrap'
import '../image/banner1.jpg'

const Home = () => {
    return(
        <div className='container' style={{marginTop:"40px", paddingLeft:"0px", paddingRight:"0px"}}>
            <Carousel variant="dark" style={{height:"500px"}}>
                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src='banner1.jpg'
                        alt="First slide" />
                    <Carousel.Caption>
                        <h5>Giano hàng nhanh</h5>
                        <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
                    </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src="holder.js/800x400?text=Second slide&bg=eee"
                        alt="Second slide"/>
                    <Carousel.Caption>
                        <h5>Second slide label</h5>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                    </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src="holder.js/800x400?text=Third slide&bg=e5e5e5"
                        alt="Third slide"/>
                    <Carousel.Caption>
                        <h5>Third slide label</h5>
                        <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
                    </Carousel.Caption>
                </Carousel.Item>
            </Carousel>

            <Card style={{ width: '18rem' }}>
                <Card.Img variant="top" src="holder.js/100px180" />
                <Card.Body>
                    <Card.Title>Card Title</Card.Title>
                    <Card.Text>
                        Some quick example text to build on the card title and make up the bulk of
                        the card's content.
                    </Card.Text>
                    <Button variant="primary">Go somewhere</Button>
                </Card.Body>
            </Card>
        </div>
    )
}

export default Home