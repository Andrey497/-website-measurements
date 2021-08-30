import React, {useEffect, useState} from "react";
import Dop from "../component/Forms/AddCalculationForms/Dop";
import {
    getAllPhisicalProcess,
    getArea,
    getEqupmentByPhysicalProcess,
    getExpirementClassByparameters
} from "../Api/ExpirementClassApi";

const AddCalculatedCase = (props) => {
    const [PhisicalProcessAarray, SetPhisicalProcessArray] = useState([]);
    const [PowerEqupmentArray, SetPowerEqupmentArray] = useState([]);
    const [PhisicalProcess, SetPhisicalProcess] = useState(0);
    const [PowerEqupment, SetPowerEqupment] = useState(0);
    const [AreaArray, SetAreaArray] = useState([]);
    const [Area, SetArea] = useState(0);
    const [ExpirementClass, SetExpirementClass] = useState();
    const [rootAreas, SetRootAreas] = useState({
        areaName: '',
        subareas: [],
    },);
    const [rootAreaID, SetrootAreaId] = useState(0);
    const [subareas, SetSubareas] = useState([]);
    useEffect(() => {
        getAllPhisicalProcess().then(res => SetPhisicalProcessArray(res.data));
    }, []);
    const handleSumbit = () => {
        if (Area && PowerEqupment && PhisicalProcess) {
            const PhpTpe = PowerEqupmentArray.filter(elem => elem.id_t_p_e_field.id_type = PowerEqupment).id_ph_p_t_p_e_field;
            getExpirementClassByparameters(Area, PhisicalProcess, PowerEqupment).then(res => SetExpirementClass(res.data.message)
            );
        } else {
            alert("Не все поля заполнены");
        }
    }
    const subareasAvaliable = () => {
        return subareas.length > 0;
    }
    const handleChangePhisicalProcess = (props) => {
        SetPhisicalProcess(props);
        getEqupmentByPhysicalProcess(props).then(res => SetPowerEqupmentArray(res.data));
    }
    const handleChangeEqupment = (props) => {
        SetPowerEqupment(props);
        getArea(1, 0, PhisicalProcess, props).then(res => {
            SetAreaArray(res.data.subareas);
            SetRootAreas({
                'areaName': res.data.area_name,
                subareas: res.data.subareas
            })
        });
        SetSubareas([]);
    }
    const handleChangeArea = (area_id, parentSubareId, index) => {
        getArea(area_id, parentSubareId, PhisicalProcess, PowerEqupment).then(res => {

            const subarea = {
                id: area_id,
                areaName: res.data.area_name,
                subareas: res.data.subareas
            };
            subareas.splice(index);
            SetSubareas(subareas.concat(subarea));
        }).catch(() => {
                subareas.splice(index);
            }
        );

        console.log(subareas);
        SetArea(parentSubareId);
        console.log(subareas);
    }
    function SelectArea(){return subareas.map((subarea, index) =>
        <div key={subarea.id}>
            <label>{subarea.areaName}</label>
            <select key={subarea.id} onChange={(event) => handleChangeArea(subarea.id+1,event.target.value,(index+1))}>
                <option disabled hidden selected>
                    Не выбран
                </option>
                {subarea.subareas.map(elem=><option  key={elem.id} value={elem.id}>{elem.name}</option>)}
            </select></div>);}

    console.log(subareas);
    console.log(ExpirementClass);
    return (
        (ExpirementClass==undefined)?
        <div>
            <form onSubmit={() => handleSumbit()}>
                <p>
                    <label>
                        Физический процесс
                    </label>
                    <select required={true} onChange={(event) => handleChangePhisicalProcess(event.target.value)}>
                        <option selected="true" disabled="disabled">Выберите значение</option>
                        {PhisicalProcessAarray.map(elem => <option value={elem.id_ph_p_field}>{elem.name}</option>)}
                    </select>
                </p>
                <p>
                    <label>
                        Обородование
                    </label>
                    <select required={true} onChange={(event) => handleChangeEqupment(event.target.value)}>
                        <option selected="true" disabled="disabled">Выберите значение</option>
                        {PowerEqupmentArray.map(elem => <option
                            value={elem.id_t_p_e_field.id_type}>{elem.id_t_p_e_field.name}</option>)}
                    </select>
                </p>

                <p>
                    <label>
                        {rootAreas.areaName}
                    </label>
                    <select required={true} onChange={(event) => handleChangeArea(2, event.target.value,0)}>
                        <option selected="true" disabled="disabled">Выберите значение</option>
                        {AreaArray.map(elem => <option value={elem.id}>{elem.name}</option>)}
                    </select>
                </p>
                {(subareasAvaliable())?
                    SelectArea(): SelectArea()}
                <input type={"button"} onClick={() => handleSumbit()} value="Отправить"/>
            </form>
        </div> : <Dop class={ExpirementClass}/>
    );

}

export default AddCalculatedCase