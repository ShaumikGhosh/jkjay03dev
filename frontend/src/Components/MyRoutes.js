import React, {Component} from 'react';
import {Route, Switch} from 'react-router-dom';
import Login from "./pages/Login";
import Profile from "./pages/Profile";
import Signup from "./pages/Signup";


class MyRoutes extends Component{
    render(){
        return(
            <div>
                <Switch>
                    <Route exact path='/' component={Login}/>
                    <Route exact path='/profile' component={Profile}/>
                    <Route exact path='/signup' component={Signup}/>
                </Switch>
            </div>
        )
    }
}

export default MyRoutes;