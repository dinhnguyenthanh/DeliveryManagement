import { Card, Col } from 'react-bootstrap'
import { Link } from 'react-router-dom'

export default function Carditem (props) {
    let path = `/categoryitems/${props.obj.id}/goodss/`

    return (
        <Col md={4} xs={12}>
            <Card style={{width:"80%", margin:"auto"}}>
                <Link to={path}>
                    <Card.Img variant="top" src={props.obj.image} />
                </Link>
                <Card.Body>
                     <Card.Title>{props.obj.name}</Card.Title>
                </Card.Body>
            </Card>
        </Col>
    )
}
