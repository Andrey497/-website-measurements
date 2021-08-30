import axios from "axios";
import {URL_API} from "./ApiUrl";

export const  getAllTypeParameters=()=>{
    return axios.get(`${URL_API}TypeOfParameters/`)
}