import axios from "axios";
import {URL_API} from "./ApiUrl";

export const  getAllPhisicalProcess=()=>{
    return axios.get(`${URL_API}PhysicalProcess/`);
}
export const  getEqupmentByPhysicalProcess=(id_ph_p_field)=>{
    return axios.get(`${URL_API}PhpTpeRead/?id_ph_p_field=${id_ph_p_field}`);
}

export const getArea=(area_id,parent_subarea_id,phys_proc_id, equpment_type_id)=>{
    return axios.get(`${URL_API}returnAreaTree/?area_id=${area_id}&parent_subarea_id=${parent_subarea_id}&phys_proc_id=${phys_proc_id}&equpment_type_id=${equpment_type_id}`);
}

export const getExpirementClassByparameters=(subarea_id,phys_proc_id, equpment_type_id)=>{
    return axios.get(`${URL_API}ReturnExpirementClass/?subarea_id=${subarea_id}&phys_proc_id=${phys_proc_id}&equpment_type_id=${equpment_type_id}`);
}