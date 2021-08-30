import React from "react";
import {NavLink} from "react-router-dom";
import {Nav, Navbar, NavDropdown} from "react-bootstrap";


const Navlinks = (props) => {
    return (
        <div >
            <Navbar   collapseOnSelect expand="lg" bg="dark" variant="dark"  >
                <Navbar.Brand>Мой Сайт</Navbar.Brand>
                <Navbar.Toggle aria-controls="responsive-navbar-nav"/>
                <Navbar.Collapse id="responsive-navbar-nav">
                    <Nav className="mr-auto">
                        <Nav.Link as={NavLink} to='/' exact>Home</Nav.Link>
                        <Nav.Link as={NavLink} to='/add_calculation_case'>Добавить расчетный случай </Nav.Link>
                        <Nav.Link as={NavLink} to='/search_calculation_case'>Поиск расчетного случая</Nav.Link>
                        <Nav.Link as={NavLink} to='/write_calculation_case'>Вывести расчетный случай</Nav.Link>
                        <NavDropdown title="Админка" id="basic-nav-dropdown">
                            <NavDropdown.Item  as={NavLink} to='/admin/users'>Пользователи</NavDropdown.Item>
                            <NavDropdown.Item as={NavLink} to='/admin/parameters'>Параметры</NavDropdown.Item>
                        </NavDropdown>
                        <Nav.Link as={NavLink} to='/FCA'>ФСА</Nav.Link>
                        <Nav.Link as={NavLink} to='Description'>Справка</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        </div>
    )
}

export default Navlinks