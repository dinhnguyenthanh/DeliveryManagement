import React, { useEffect, useState } from 'react'
import { useNavigate } from "react-router";
import { Button, Container, Form, FormControl, Nav, Navbar } from 'react-bootstrap'
import { Link } from 'react-router-dom'
import Api, {endpoints} from '../configs/Api'


const Header = () => {
    const [categories, setCategories] = useState([])
    const [kw, setKw] = useState("")
    const nav = useNavigate()


    useEffect(() => {
        let loadCategories = async() => {
            let res = await Api.get(endpoints['categories'])

            setCategories(res.data)
        }

        loadCategories()
    }, []);

    const search = (event) => {
        event.preventDefault()
        nav(`/?kw=${kw}`)
    }

    return (
        <>
        <Navbar bg="light" expand="lg">
            <Container fluid>
                <Navbar.Brand href="#">Delivery Web</Navbar.Brand>
                <Navbar.Toggle aria-controls="navbarScroll" />
                <Navbar.Collapse id="navbarScroll">
                <Nav className="me-auto my-2 my-lg-0" style={{ maxHeight: '100px' }} navbarScroll >
                    <Link className='nav-link' to="/">Trang chủ</Link>
                    {categories.map(c => { 
                        const url = `/?category_id=${c.id}`
                        return <Link className="nav-link" to={url}>{c.name}</Link> 
                    })}
                </Nav>
                <Form className="d-flex" onSubmit={search}>
                    <FormControl type="search" placeholder="" className="me-2" 
                                aria-label="Search"
                                value={kw} onChange={(event) => setKw(event.target.value)}/>

                    <Button style={{width:"100px", fontSize:"12px"}} type= "submit"
                            variant="outline-success">Tìm kiếm</Button>
                </Form>
                </Navbar.Collapse>
            </Container>
        </Navbar>
        </>
    )
}

export default Header