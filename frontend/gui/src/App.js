import React, { Component } from 'react';
import './App.css';
import 'antd/dist/antd.css';

import CustomLayout from './containers/Layout';
import PostsList from './containers/PostsListView';

class App extends Component {
  render() {
    return (
      <div className="App">
        <CustomLayout>
          <PostsList />
        </CustomLayout> 
      </div>
    );
  }
}

export default App;
