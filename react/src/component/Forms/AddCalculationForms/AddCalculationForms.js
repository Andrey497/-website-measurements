import React, {useState} from "react";
import {useForm} from "react-hook-form";
import {Table} from "react-bootstrap";
import InputFunction from "./Inputs/InputFunction";
import {CreateExpirement, DeleteExpirement, UpdateExpirement} from "../../../Api/ExpirementApi";
///Нужен сильный рефактор кода
const AddCalculationForms = (props) => {
//Переменные нееобходимые для работы с таблицой
    const [resivedValues] = useState(props.resivedValues);
    let [maxReciveId] = useState(Math.max(...resivedValues.map(element => element.id_value)));//максимальный id пришедшего
    let [maxId, SetMaxId] = useState((maxReciveId == -Infinity) ? 1 : maxReciveId);//максимальный id
    let [newValues, SetNewValues] = useState(JSON.parse(JSON.stringify(resivedValues)));//значение
    let [expirement, SetExpirement] = useState(Array.from(new Set(newValues.map(element => element.id_exp))));//массив id экспирементов
    let [parametersId, SetParametersId] = useState(newValues
        .filter(element => element.id_exp == Math.min(...expirement))
        .map(element => ({
            id_param: element.id_param.id_param,
            id_type: element.id_param.id_type,
            id_data: element.id_data
        })).sort((elem1, elem2) => elem1.id_type - elem2.id_type));//Массив id параметров
    let [rowCount, SetRovCount] = useState(expirement.length);
    let [deleteRow] = useState([]);
    let [deleteColumn] = useState([]);
    let [columnCount, SetColumnCount] = useState(parametersId.length);
    let [idTypeOfParameters] = useState(props.typeOfparameters.map(elem => elem.id_type));
    let [CountTypeOfParameters, SetCountTypeOfParameters] = useState(parametersId.reduce((acc, o) => (acc[o.id_type] = (acc[o.id_type] || 0) + 1, acc), {}));
    let [CountTypeOfParameter, SetCountTypeOfParameter] = useState(idTypeOfParameters.reduce((acc, o) => (acc[o] = (CountTypeOfParameters[o] || 0), acc), {}));
    let [headerTableTypes, SetheaderTableTypes] = useState(Header());
    console.log(props.parameters.find(elem => elem.id_param == 2).string_values.map(elemem => elemem));

    //Функция строющая шапку таблицы состаящию из головной части типов параметров
    function Header() {
        var result = [<th></th>];
        for (const key in CountTypeOfParameter) {
            if (CountTypeOfParameter[key]) {
                result.push(<th
                    colSpan={CountTypeOfParameter[key]}>{props.typeOfparameters.find(elem => elem.id_type == Number(key)).name}</th>);
            }
        }
        return result;
    }

    //Функция добовляющая колонку
    function addRow() {
        SetRovCount(rowCount + 1);
        SetMaxId(maxId + columnCount);
        SetExpirement(expirement.concat([++rowCount]));
        let newRow = [];
        for (let i = 0; i < columnCount; i++) {
            SetMaxId(++maxId);
            let obj = {
                id_value: maxId,
                id_field:props.class,//Заглушка
                id_exp: rowCount,
                id_param: {
                    id_param: parametersId[i].id_param,
                    id_type: props.parameters.find(elem => elem.id_param == parametersId[i].id_param).id_type,
                },
                value: {
                    value_number: null,
                    value_range: null,
                    value_string: "",
                    value_image: ""
                },
                id_data: parametersId[i].id_data
            }

            newRow.push(obj);
        }

        SetNewValues(newValues.concat(newRow));
    }

    //Функция удаления строки
    function DeleteRow(id_row) {
        if (resivedValues.map(element => element.id_exp).indexOf(id_row) != -1) {
            deleteRow.push(id_row);
        }
        SetColumnCount(--columnCount);
        SetNewValues(newValues.filter(element => element.id_exp != id_row));
        SetExpirement(expirement.filter(elem => elem != id_row));
    }

    function DeleteColumn(id_parameter) {
        if (resivedValues.map(element => element.id_param.id_param).indexOf(id_parameter) != -1) {
            deleteColumn.push(id_parameter);
        }
        SetColumnCount(--columnCount);
        SubtractColTypeParameter(parametersId.find(elem => elem.id_param == id_parameter).id_type);
        SetParametersId(parametersId.filter(element => element.id_param != id_parameter));
        SetNewValues(newValues.filter(element => element.id_param.id_param != id_parameter));
        SetheaderTableTypes(Header());
    }


    //Нужна для счета количества типов параметров,чтобы построить таблицу(геометрические,тепловые и т.д)
    function AddColTypeParameter(id_type) {
        let timeElem = CountTypeOfParameter;
        ++timeElem[id_type];
        SetCountTypeOfParameter(timeElem);
    }

    //Нужна для счета количества типов параметров,чтобы построить таблицу(геометрические,тепловые и т.д)
    function SubtractColTypeParameter(id_type) {
        let timeElem = CountTypeOfParameter;
        --timeElem[id_type];
        SetCountTypeOfParameter(timeElem);
    }

    function CaseInput(id_data, id_value, value, id_param) {
        let inputCase = null;
        switch (id_data) {
            case 1:
                console.log(value);
                inputCase = <input type={'number'} key={id_value}  {...register(`number${id_value}`, {required: true})}
                                   defaultValue={value.value_number}/>
                break;
            case 2:
                inputCase = <div>
                    <input type={'number'} key={id_value + ".1"}
                           defaultValue={value.value_range} {...register(`range.1.${id_value}`, {required: true})}/> -
                    <input key={id_value + ".2"}
                           type={'number'}
                           defaultValue={value.value_range} {...register(`range.2.${id_value}`, {required: true})}/>
                </div>
                break;
            case 3:
                inputCase = <div>
                    <input list={`list${id_value}`} key={id_value}
                           {...register(`string${id_value}`, {required: true})}
                           defaultValue={value.value_string}/>
                    <datalist id={`list${id_value}`}>
                        {props.parameters.find(elem => elem.id_param == id_param).string_values.map(elem =>
                            <option>{elem.value}</option>)}

                    </datalist>
                </div>
                break;
            case 4:
                inputCase =
                    <InputFunction/>
                break;
        }
        return inputCase;
    }


    //Функция добовляющая столбец
    function addColumn(data) {
        SetColumnCount(++columnCount);
        SetMaxId(maxId + rowCount);
        SetParametersId(parametersId.concat([{
            id_param: Number(data.param),
            id_type: props.parameters.find(elem => elem.id_param == Number(data.param)).id_type,
            id_data: Number(data.type)
        }]).sort((elem1, elem2) => elem1.id_type - elem2.id_type));

        let newcolumn = [];
        for (let i = 0; i < rowCount; i++) {
            SetMaxId(++maxId);
            let obj = {
                id_value: maxId,
                id_field: props.class,//Заглушка
                id_exp: expirement[i],
                id_param: {
                    id_param: Number(data.param),
                    id_type: props.parameters.find(elem => elem.id_param == Number(data.param)).id_type,
                },
                value: {
                    value_number: null,
                    value_range: null,
                    value_string: "",
                    value_image: ""
                },
                id_data: Number(data.type)
            }
            newcolumn.push(obj);
        }
        SetNewValues(newValues.concat(newcolumn));
        AddColTypeParameter(Number(props.parameters.find(elem => elem.id_param == data.param).id_type));
        SetheaderTableTypes(Header());

    }

    let headerTableParameters = [
        <th>№Р.С.</th>
    ].concat(parametersId.map(elementId =>
        <th>
            <button type={"button"} onClick={() => DeleteColumn(elementId.id_param)}>❌</button>
            <br/>
            {props.parameters.find(elem => elem.id_param == elementId.id_param).name_param}
        </th>
    ));//Заголовки таблцы
    const
        {
            register, handleSubmit
        }
            = useForm();
    const
        {
            register: registerParameter, handleSubmit:
            handelsumbitParameter
        }
            = useForm();
    //Отправка данных
    const onSubmit = data => {
        newValues.forEach(element => {
                switch (element.id_data) {
                    case 1:
                        element.value.value_number = data[`number${element.id_value}`]
                        break;
                    case 2:
                        element.value.value_range = [data[`range.1.${element.id_value}`], data[`range.1.${element.id_value}`]];
                        break;
                    case 3:
                        element.value.value_string = data[`string${element.id_value}`]
                        break;
                    case 4:
                        break;
                }
            }
        );
        newValues.forEach(elem => {
            let id_param = elem.id_param.id_param;
            delete elem.id_param;
            elem.id_param = id_param;
        })
        var createValue = JSON.parse(JSON.stringify(newValues.filter(element => element.id_value > maxReciveId)));
        createValue.forEach(element => {
            delete element.id_value
        });
        var updateValues = newValues.filter(element => element.id_value <= maxReciveId);
        if (deleteRow.length || deleteColumn.length) {
            console.log(deleteRow.length || deleteColumn.length);
            DeleteExpirement({
                "experiment_class": props.class,
                "rows": deleteRow,
                "columns": deleteColumn
            }).catch(error => {
                if (!error.response) {
                    console.log("Please check your internet connection.");
                    const deleteExpirement ={
                        "experiment_class": props.class,
                        "rows": deleteRow,
                        "columns": deleteColumn
                    };
                    localStorage.setItem("Ispalit_delete_Expirement",JSON.stringify(JSON.stringify(deleteExpirement)));
                }
            });
        }
        if (updateValues.length)
            UpdateExpirement(updateValues).catch(error => {
                if (!error.response) {
                    console.log("Please check your internet connection.");
                    localStorage.setItem("Ispalit_update_Expirement",JSON.stringify(updateValues));
                }
            });
        if (createValue.length)
            CreateExpirement(createValue).catch(error => {
                if (!error.response) {
                    console.log("Please check your internet connection.");
                    localStorage.setItem("Ispalit_create_Expirement",JSON.stringify(createValue));
                }
            });
        console.log(createValue);


    }
    //Передача данных для добовления столбца
    const onSubmitParameter = data => {
        if (parametersId.map(element => element.id_param).indexOf(Number(data.param)) == -1) {
            addColumn(data);
        } else {
            alert("Такой параметер уже есть");
        }
    }
    newValues.sort((a, b) => a.id_exp - b.id_exp);
    let value = expirement.map((element, index) =>
        <tr>
            <td>
                <button type={"button"} onClick={() => DeleteRow(element)}>❌</button>
                {element}
            </td>
            {newValues.filter(item => item.id_exp == element)
                .sort((a, b) => a.id_param.id_type - b.id_param.id_type)
                .map(item2 => <td>
                    {CaseInput(item2.id_data, item2.id_value, item2.value, item2.id_param.id_param)}</td>)}
        </tr>
    );


    return (
        <div>
            <form onSubmit={handleSubmit(onSubmit)}>
                <Table striped bordered hover size="sm">
                    <thead>
                    <tr>
                        {headerTableTypes}
                    </tr>
                    <tr>
                        {headerTableParameters}
                    </tr>
                    </thead>
                    {newValues.length > 0 && (
                        <tbody> {value}</tbody>)}
                </Table>
                <input type="submit"/>
            </form>

            <form onSubmit={handelsumbitParameter(onSubmitParameter)}>
                <p>
                    <select {...registerParameter("param")}>
                        {props.parameters.map(elem => <option value={elem.id_param}>{elem.name_param}</option>)}
                    </select>
                </p>
                <p>
                    <select {...registerParameter("type")}>
                        {props.dataType.map(elem => <option value={elem.id_data}>{elem.name_data}</option>)}
                    </select>
                </p>
                <input type="submit"/>
            </form>
            <button onClick={addRow}> добавить расчетный случай</button>
        </div>
    )
}
export default AddCalculationForms