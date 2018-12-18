import React from 'react';
import axios from 'axios';

import Posts from '../components/Posts';
import CustomForm from '../components/Form';

class PostsList extends React.Component {

    state = {
        posts: []
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/')
            .then(res => {
                this.setState({
                    posts: res.data
                });
            })
    }

    render() {
        return (
            <div>
                <Posts data={this.state.posts} />
                <br />
                <h2>Create an article</h2>
                <CustomForm requestType="post" postID={null} btnText="Submit"/>
            </div>
        );
    }
}

export default PostsList;