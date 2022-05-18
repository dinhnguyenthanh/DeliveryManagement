import React from 'react'
import { Button, Container, Form } from 'react-bootstrap'
import { Link } from 'react-router-dom'
import'../Static/Header.css'

const Header = () => {
    return (
        <div className='main-header'>
            <Container>
                <Form className="d-flex">
                    <div className='main-logo'>
                        <Link to="/">Delivery Web</Link>
                    </div>
                    <Form.Control className="form form-control me-2" type="search" placeholder="" aria-label="Search" />
                    <Button className="btnn" type='submit'>search</Button>
                </Form>
            </Container>
        </div>
    )
}

export default Header
