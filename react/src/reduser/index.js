import {combineReducers, createStore, applyMiddleware} from "redux"
import resposReduser from "./resposReduser";

const rootReduse = combineReducers({
        respos: resposReduser
    }
)