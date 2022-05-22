import React, { useEffect, useState } from 'react'
import { Container, Row } from 'react-bootstrap'
import { useParams } from 'react-router'
import Carditem from '../components/Carditem'
import Api, {endpoints} from '../configs/Api'

const Service = () => {
    const [goodss, setGoods] = useState([])
    const {categoryitemId} = useParams()

    useEffect(() => {
      let loadGoods = async() => {
            try {
                let res = await Api.get(endpoints['goodss'](categoryitemId))
                setGoods(res.data)
            } catch (error) {
                console.info(error)
            }
        }
      
        loadGoods()
    }, [])
    

    return (
        <Container style={{paddingTop:"30px", margin:"auto"}}>
            <h1 className='text-center text-danger'>Danh sách các hàng hóa dịch vụ</h1>

            <Row>
                {goodss?.map((g) => (
                    <Carditem obj={g} />
                ))}
            </Row>
        </Container>
    )
}

export default Service