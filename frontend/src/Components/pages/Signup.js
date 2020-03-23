import React, {Component} from 'react';
import {Link} from 'react-router-dom';


class Signup extends Component{

    constructor(props) {
        super(props);
        this.state ={
            username: "",
            password: "",
            email: "",
            successMsg: "",
        };
    };

    onChangeHandler = (event) => {
        let inputs = event.target.name;
        let inputsData = event.target.value;

        this.setState({[inputs]:inputsData})
    };

    onSubmit = (event) =>{
        event.preventDefault();
        fetch('http://127.0.0.1:8000/api/v1/register/', {
            method: 'POST',
            headers: {
               'Accept': 'application/json',
               'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "username": this.state.username,
                "password": this.state.password,
                "email": this.state.email,
            })
        })
        .then(res=>res.json())
        .then(res=>{
            this.setState({successMsg:res.message})
        }).catch(err => {
            console.log(err);
        });
    };

    render() {
        return (
            <div>
                <h2>Signup here</h2>
                <form onSubmit={this.onSubmit} method='POST'>
                    <input onChange={this.onChangeHandler} name='username' type='text' placeholder='Enter username'/>
                    <br/>
                    <input onChange={this.onChangeHandler} name='email' type='email' placeholder='Enter email'/>
                    <br/>
                    <input onChange={this.onChangeHandler} name='password' type='password' placeholder='Enter password'/>
                    <br/>
                    <button type='submit'>Signup</button>
                    <Link to='/'>Login</Link>
                </form>
            </div>
        )
    }
}

export default Signup;