import React, {useState, useEffect, useRef} from "react";
import {getExpirementsByExpirementClass} from "../../../Api/ExpirementApi";
import Home from "../../../Pages/Home";
import {getAllParameters} from "../../../Api/Parameters_api";
import {getAllTypeParameters} from "../../../Api/TypeOfParameters";
import {getAllDataType} from "../../../Api/DataTypeApi";
import AddCalculationForms from "./AddCalculationForms";


const Dop = (props) => {
//Задаем переменыые для работы с таблицей
    var [load, Setload] = useState(0);
    const [resivedValues, SetResivedValues] = useState([]);
    const [parameters, SetParameters] = useState([]);
    const [typeParameters, SetTypeParameters] = useState([]);
    const [datatype, SetDataType] = useState([]);

    useEffect(() => {
            getAllDataType()
                .then(res => {
                    const allValues = res.data;
                    SetDataType(allValues);
                    console.log(load);
                    Setload(++load);
                });
            getExpirementsByExpirementClass(props.class.id)
                .then(res => {
                    const allValues = res.data;
                    SetResivedValues(allValues);
                    console.log(load);
                    Setload(++load);
                });
            getAllParameters()
                .then(res => {
                    const allValues = res.data;
                    SetParameters(allValues);
                    Setload(++load);
                    console.log(load);
                });

            getAllTypeParameters()
                .then(res => {
                    const allValues = res.data;
                    SetTypeParameters(allValues);
                    Setload(++load);
                    console.log(load);
                });
        }, []
    );
    console.log(load);
    return (
        (load == 4) ?
            <AddCalculationForms resivedValues={resivedValues} typeOfparameters={typeParameters} parameters={parameters}
                                 dataType={datatype} class={props.class.id}/> :
            <Home/>
    )
}

export default Dop