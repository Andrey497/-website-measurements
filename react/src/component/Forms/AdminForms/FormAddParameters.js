import React, {useEffect, useState} from "react";
import {useForm} from "react-hook-form";
import {CreateParameter, getParametersByType} from "../../../Api/Parameters_api";

export default function FormAddParameters(props) {
    const {register, handleSubmit} = useForm();
    const [parameters, setAppState] = useState([]);
    useEffect(() => {
        getParametersByType(Number(props.id_type)).then((resp) => {
            const allPersons = resp.data;
            setAppState(allPersons);
        });
    }, []);
    const onSubmit = data => {

        data.id_type = props.id_type;
        data.string_values=[];
        let findParameter= parameters.find(elem=>elem.name_param.toLowerCase() == data.name_param.toLowerCase());
        if(findParameter){
            alert("Такой параметер уже есть");
            console.log(findParameter);
        }
         else {

            let response = CreateParameter(data);
            alert(JSON.stringify(data));
            console.log(JSON.stringify(data));
            response.then((resp)=> {
            }).catch((error)=>{
                console.log(error.response);
            });
         }
    }
    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <p>

                <input  {...register("name_param", {required: true})} />
                <label>Название прараметра</label>
            </p>
            <p>

                <input {...register("short_name_param", {required: true})} />
                <label>Обозначение параметра</label>
            </p>

            <input {...register("unit_param", {required: true})} />
            <label>Еденицы измерения</label>
            <p>
                <input type="submit"/>
            </p>
        </form>
    );
}