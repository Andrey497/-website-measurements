import React from "react";

const InputNumrange = (props) => {
    return (
        // eslint-disable-next-line no-undef
        <input key={props.id_value}  {...register(`name${props.id_value}`, {required: true})}
               defaultValue={props.value.value_number}/>
    )
}
export  default InputNumrange