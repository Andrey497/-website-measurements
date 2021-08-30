import React from "react";
import {Col, ListGroup, Row, Tab} from "react-bootstrap";
import FormAddParameters from "../../component/Forms/AdminForms/FormAddParameters";
import TableParameters from "../../component/table/Admin/TableParameters";

const AdminUsers = (props) => {
    let data = [
        {
            "id_type": 1,
            "name": "Геометрические параметры"
        },
        {
            "id_type": 2,
            "name": "Режимные параметры"
        },
        {
            "id_type": 3,
            "name": "Теплофизические параметры"
        },
        {
            "id_type": 4,
            "name": "Параметры сетки"
        },
        {
            "id_type": 5,
            "name": "Настройки решателя "
        },
        {
            "id_type": 6,
            "name": "Результаты"
        }
    ];
    let listGroup = data.map(item => <ListGroup.Item action href={`#${item.id_type}`}>{item.name}</ListGroup.Item>);
    let TabPen = data.map(item =>

        <Tab.Pane eventKey={`#${item.id_type}`}>
            <TableParameters id_type={item.id_type}/>
            <FormAddParameters id_type={item.id_type}/>
        </Tab.Pane>);
    return (
        <div>
            <Tab.Container id="list-group-tabs-example" defaultActiveKey="#link1">
                <Row>
                    <Col sm={4} md={3} lg={2}>
                        <ListGroup>
                            {listGroup}
                        </ListGroup>
                    </Col>
                    <Col sm={8} md={9} lg={10}>
                        <Tab.Content>
                            {TabPen}
                        </Tab.Content>
                    </Col>
                </Row>
            </Tab.Container>
        </div>

    )
}
export default AdminUsers