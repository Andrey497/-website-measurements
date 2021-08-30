import React from "react";
import { useFormContext} from "react-hook-form";
const InputNumber = (props) => {
    console.log(12);
    const { register } = useFormContext(); // retrieve all hook methods
    return (

        <input key={props.id_value}  {...register(`name${props.id_value}`, {required: true})}
               defaultValue={props.value.value_number}/>
    )
}
export  default InputNumber