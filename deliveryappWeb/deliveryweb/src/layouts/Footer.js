import React from 'react'
import { Button, Card } from 'react-bootstrap'

const Footer = () => {
    return (
        <>
            <Card className="text-center">
                <Card.Header>Thank you</Card.Header>
                <Card.Body>
                    <Card.Title>Trang web vận chuyển hàng hóa</Card.Title>
                    <Card.Text>
                        Mọi thông tin xin vui lòng hiên hệ
                    </Card.Text>
                </Card.Body>
                <Card.Footer className="text-muted">2 days ago</Card.Footer>
            </Card>
        </>
    )
}

export default Footer