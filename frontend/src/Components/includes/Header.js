import React, {Component} from 'react';
import {Redirect} from 'react-router-dom';


class Header extends Component{

    constructor(props) {
        super(props);
        this.state ={
            login: true,
            token: null,
        };
    };

    onSubmit = (event) =>{
        event.preventDefault();
        fetch('http://127.0.0.1:8000/api/v1/logout/', {
            method: 'POST',
            headers: {
               'Accept': 'application/json',
               'Content-Type': 'application/json',
                'Authorization': `Token ${localStorage.getItem('validate_user_token')}`,
            },
        })
        .then(()=>{
            localStorage.removeItem('validate_user_token');
            this.setState({login: false});
        });
    };

    render() {
        if (!this.state.login){
            return (
                <Redirect to='/'/>
            )
        }
        return (
            <div className='header-area'>
                <div className='header'>
                    <div className='header-left'>
                        <img src='https://logodownload.org/wp-content/uploads/2019/08/alba-logo.png' alt='' width='100'/>
                    </div>
                    <div className='header-right'>
                        <form method='POST' onSubmit={this.onSubmit}>
                            <button type='submit'>Logout</button>
                        </form>
                    </div>
                </div>
            </div>
        )
    }
}

export default Header;