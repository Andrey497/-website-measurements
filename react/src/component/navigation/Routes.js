import React from "react";
import {Route,Switch} from "react-router-dom";
import Home from "../../Pages/Home";
import AdminUsers from "../../Pages/admin/AdminUsers";
import AddCalculatedCase from "../../Pages/AddCalculatedCase";
import SearchCalculatedCase from "../../Pages/SearchCalculatedCase";
import WriteCalculatedCase from "../../Pages/WriteCalculatedCase";
import FCA from "../../Pages/FCA";
import Description from "../../Pages/Description";
import AdminParameters from "../../Pages/admin/AdminParameters";
import Dop from "../Forms/AddCalculationForms/Dop";
import Dop2 from "../table/Dop2";

const Routes = (props) => {
    return (
        <div>
            <Switch>
            <Route exact path='/'> <Home/></Route>
            <Route path='/admin/users'><AdminUsers/></Route>
            <Route path='/admin/parameters'><AdminParameters/></Route>
            <Route path='/add_calculation_case'><AddCalculatedCase /></Route>
            <Route path='/search_calculation_case'><SearchCalculatedCase/></Route>
            <Route path='/write_calculation_case'> <WriteCalculatedCase/></Route>
            <Route path='/FCA'> <FCA/></Route>
            <Route path='/Description'> <Description/></Route>
            </Switch>
        </div>
    )
}
export default Routes