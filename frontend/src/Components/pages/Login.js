import React, {Component} from 'react';
import {Redirect} from 'react-router-dom';
import {Link} from 'react-router-dom';


class Login extends Component{

    constructor(props) {
        super(props);
        this.state ={
            username: "",
            password: "",
            login: false,
        };
    };

    onChangeHandler = (event) => {
        let inputs = event.target.name;
        let inputsData = event.target.value;

        this.setState({[inputs]:inputsData})
    };

    onSubmit = (event) =>{
        event.preventDefault();
        fetch('http://127.0.0.1:8000/api/v1/login/', {
            method: 'POST',
            headers: {
               'Accept': 'application/json',
               'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "username": this.state.username,
                "password": this.state.password
            })
        })
        .then(res=>res.json())
        .then(res=>{
            localStorage.setItem('validate_user_token', res.token);
            this.setState({login: true});
        }).catch(err => {
            console.log(err);
        });
    };

    render() {
        if (this.state.login){
            return (
                <Redirect to='/profile'/>
            )
        }else {
            return (
                <div>
                    <h2>Login here</h2>
                    <form onSubmit={this.onSubmit} method='POST'>
                        <input onChange={this.onChangeHandler} name='username' type='text' placeholder='Enter username'/>
                        <br/>
                        <input onChange={this.onChangeHandler} name='password' type='password' placeholder='Enter password'/>
                        <br/>
                        <button type='submit'>Login</button>
                        <Link to='/signup'>Signup</Link>
                    </form>
                </div>
            )
        }
    };
}

export default Login;