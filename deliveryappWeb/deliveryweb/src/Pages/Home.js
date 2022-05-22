import React, { useEffect, useState } from 'react'
import { Button, ButtonGroup, Container, Row} from 'react-bootstrap'
import { useLocation } from 'react-router-dom'
import Carditem from '../components/Carditem'
import Api, { endpoints } from '../configs/Api'
import carouselCompo from '../components/carouselCompo'

const Home = () => {

    const [categoryitems, setCategoryitems] = useState([])
    const location = useLocation()
    const [prev, setPrev] = useState(false)
    const [next, setNext] = useState(false)
    const [page, setPage] = useState(1)

    useEffect(() => {
        let loadCategoryitems = async() => {
            let query = location.search
            if (query === "")
                query = `?page=${page}`
            else 
                query += `&page=${page}`

            try {
                let res = await Api.get(`${endpoints['categoryitems']}${query}`)
                setCategoryitems(res.data.results)

                setNext(res.data.next !== null)
                setPrev(res.data.previous !== null)
            } catch (error) {
                console.info(error)
            }
        }

        loadCategoryitems()
    }, [location.search, page])

    const paging = (inc) => {
        setPage(page + inc)
    }


    return (
        <Container style={{paddingTop:"30px", margin:"auto"}}>
            <carouselCompo />

            <h1 style={{marginTop:"20px", marginBottom:"20px"}} className='text-center text-danger'>Danh mục</h1>
            
            <ButtonGroup>
                <Button onClick={() => paging(-1)} variant='info' disabled={!prev}>&lt;&lt;</Button>
                <Button onClick={() => paging(1)} variant='info' disabled={!next}>&gt;&gt;</Button>
            </ButtonGroup>

            <Row>
                {categoryitems?.map((c) => (
                    <Carditem obj={c} />
                ))}
            </Row>
        </Container>
    )
}

export default Home