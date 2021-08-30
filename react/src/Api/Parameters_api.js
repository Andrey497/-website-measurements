import axios from "axios";
import {URL_API} from "./ApiUrl";

export const  getAllParameters=()=>{
    return axios.get(`${URL_API}Parameters/`)
}
export const getParametersByType=(id_type)=>{
    return axios.get(`${URL_API}Parameters/?id_type=${id_type}`)
}

export const  getDetailParameter=(id)=>{
    return axios.get(`${URL_API}Parameters/${id}/`)
}

export const  CreateParameter=(parameter)=>{
    return axios.post(`${URL_API}Parameters/`,parameter)
}
export const  UpdateParameter=(parameter)=>{
    return axios.put(`${URL_API}Parameters/`,parameter)
}

export const  Deleteparameter=(id)=>{
    return axios.delete(`${URL_API}Parameters/${id}/`)
}
