import React from 'react';
import axios from 'axios';

import { Card, Button } from 'antd';

import CustomForm from '../components/Form';

class PostsDetails extends React.Component {

    state = {
        post: {}
    }

    componentDidMount() {
        const postID = this.props.match.params.postID;
        axios.get(`http://127.0.0.1:8000/api/${postID}`)
            .then(res => {
                this.setState({
                    post: res.data
                });
            })
    }

    handleDelete = (event) => {
        const postID = this.props.match.params.postID;
        axios.delete(`http://127.0.0.1:8000/api/${postID}`);
        this.props.history.push('/');
        this.forceUpdate();
    }

    render() {
        return (
            <div>
                <Card title={this.state.post.title}>
                    <p>{this.state.post.content}</p>
                </Card>
                <CustomForm requestType="put" postID={this.props.match.params.postID} btnText="Update"/>
                <form onSubmit={this.handleDelete}>
                    <Button type="danger" htmlType="submit">Delete</Button>
                </form>
            </div>
        )
    }
}

export default PostsDetails;