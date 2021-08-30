import React, {useEffect, useState} from "react";
import {Table} from "react-bootstrap";
import {getAllParameters, getParametersByType} from "../../../Api/Parameters_api";
export default function TableParameters(props) {
    const [appState, setAppState] = useState([]);
    useEffect(() => {
        getParametersByType(Number(props.id_type)).then((resp) => {
            const allPersons = resp.data;
            setAppState(allPersons);
        });
    }, [setAppState]);
    let tableValue = appState.map((item,i)=><tr>
        <td>{i+1}</td>
        <td>{item.name_param}</td>
        <td>{item.short_name_param}</td>
        <td>{item.unit_param}</td>
    </tr>);
    return(
        <div>
            <Table responsive="sm">
                <thead>
                <tr>
                    <th>№</th>
                    <th>Название</th>
                    <th>Обозначение</th>
                    <th>Единицы измерения</th>
                </tr>
                </thead>
                <tbody>
                {tableValue}
                </tbody>
            </Table>
        </div>

    );
}