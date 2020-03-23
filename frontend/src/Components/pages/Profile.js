import React, {Component} from 'react';
import {Redirect} from 'react-router-dom';
import Header from "../includes/Header";


class Profile extends Component {

    constructor(props) {
        super(props);
        this.state = {
            posts: [],
        };
        if (localStorage.getItem('validate_user_token')) {
            this.token = `Token ${localStorage.getItem('validate_user_token')}`;
        } else {
            this.token = null;
        }
    }

    componentDidMount() {
        fetch('http://127.0.0.1:8000/api/v1/create-post/', {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': this.token
            },
        })
            .then(res => res.json())
            .then(res => {
                this.setState({posts: res});
            }).catch(err => {
            console.log(err);
        });
    }

    render() {
        if (this.token === null) {
            return (
                <Redirect to='/'/>
            )
        } else {
            let result = this.state.posts.map(post => {
                return (
                    <div key={post.id} className='post'>
                        <div className='title-area'>
                            <h2>{post.post_title}</h2>
                        </div>
                        <div className='description-area'>
                            <p>{post.post_description}</p>
                        </div>
                    </div>
                )
            });
            return (
                <div className=''>
                    <Header/>
                    <div className='post-area'>
                        {result}
                    </div>
                </div>
            )
        }
    }
}

export default Profile;