import React from 'react'
import { Card, Col } from 'react-bootstrap'
import '../json/data.json'

const cardItemService = (props) => {
    return (
        <Col md={4} sx={12}>
            <Card style={{ width: '18rem' }}>
                <Card.Img variant="top" src={props.obj.image} />
                <Card.Body>
                    <Card.Title>{props.obj.name}</Card.Title>
                    <Card.Text>
                            
                    </Card.Text>
                </Card.Body>
            </Card>
        </Col>
    )
}

export default cardItemService