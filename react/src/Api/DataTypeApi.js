import axios from "axios";
import {URL_API} from "./ApiUrl";

export const  getAllDataType=()=>{
    return axios.get(`${URL_API}DataType/`)
}