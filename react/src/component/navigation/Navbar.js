import React from "react";
import {BrowserRouter} from "react-router-dom";
import Routes from "./Routes";
import Navlinks from "./Navlinks";

const Navbar=(props)=>{
return (
    <div>
<BrowserRouter>
    <Navlinks/>
    <Routes/>
</BrowserRouter>
        </div>
)
}
export default Navbar