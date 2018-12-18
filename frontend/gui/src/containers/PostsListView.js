import React from 'react';
import axios from 'axios';

import Posts from '../components/Posts';

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
            <Posts data={this.state.posts} />
        );
    }
}

export default PostsList;