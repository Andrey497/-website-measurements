import React, {useState} from "react";
import {useForm} from "react-hook-form";
import {Table} from "react-bootstrap";

const TablecalculatedCaseByClass = (props) => {
    //Задаем переменыые для работы с таблицей
    function returnValue(element){
        for(const key in element ){
            if(element[key]){
                return element[key];
            }
        }
    }
    const [resivedValues,SetResivedValues] = useState(props.resivedValues);
    let [expirement, SetExpirement] = useState(Array.from(new Set(resivedValues.map(element => element.id_exp))));//массив id экспирементов
    let [parametersId, SetParametersId] = useState(resivedValues
        .filter(element => element.id_exp == Math.min(...expirement))
        .map(element =>({
            id_param:element.id_param.id_param,
            id_type:element.id_param.id_type})).sort((elem1,elem2)=>elem1.id_type-elem2.id_type));//Массив id параметров
    let [rowCount, SetRovCount] = useState(expirement.length);
    let [columnCount, SetColumnCount] = useState(parametersId.length);
    let[CountTypeOfParameter,SetCountTypeOfParameter]=useState(parametersId.reduce( (acc, o) => (acc[o.id_type] = (acc[o.id_type] || 0)+1, acc), {} ));
    let[headerTableTypes,SetheaderTableTypes]=useState(Header());
    function Header(){
        var result = [<th></th>];
        for(const key in CountTypeOfParameter){
            if(CountTypeOfParameter[key]){
                result.push(<th colSpan={CountTypeOfParameter[key]}>{props.typeOfparameters.find(elem=>elem.id_type==key).name}</th>);
            }}
        return result;
    }

    function AddColTypeParameter(id_type){
        let timeElem = CountTypeOfParameter;
        ++timeElem[id_type];
        SetCountTypeOfParameter(timeElem);
    }



    let headerTableParameters = [<th>№Р.С.</th>].concat(parametersId.map(elementId =><th>{props.parameters.find(elem=>elem.id_param==elementId.id_param).name_param}</th>));//Заголовки таблцы
    const {register, handleSubmit} = useForm();
    const {register:registerParameter, handleSubmit:handelsumbitParameter} = useForm();





    resivedValues.sort((a, b) => a.id_exp - b.id_exp);
    let value = expirement.map(element =>
        <tr>
            <td>{element}</td>
            {resivedValues.filter(item => item.id_exp == element)
                .sort((a,b)=>a.id_param.id_type-b.id_param.id_type)
                .map(item2 => <td>
                    {returnValue(item2.value)} </td>)}
        </tr>
    );


    return (
        <div>
            <Table striped bordered hover size="sm">
                <thead>
                <tr>
                    {headerTableTypes}
                </tr>
                <tr>
                    {headerTableParameters}
                </tr>
                </thead>
                <tbody> {value}</tbody>
            </Table>

        </div>
    )}
export  default TablecalculatedCaseByClass