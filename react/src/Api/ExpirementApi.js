import axios from "axios";
import {URL_API} from "./ApiUrl";

export const  getAllExpirements=()=>{
    return axios.get(`${URL_API}ExperimentRead/`)
}
export const getExpirementsByExpirementClass=(id_class)=>{
    return axios.get(`${URL_API}ExperimentRead/?id_field=${id_class}`)
}

export const  getDetailExpirement=(id)=>{
    return axios.get(`${URL_API}ExperimentRead/${id}/`)
}

export const  CreateExpirement=(parameter)=>{
    return axios.post(`${URL_API}ExperimentWrite/`,parameter)
}
export const  UpdateExpirement=(parameter)=>{
    return axios.post(`${URL_API}update_Expirement/`,parameter)
}

export const  DeleteExpirement=(parameter)=>{
    return axios.post(`${URL_API}delete_expirements/`,parameter)
}