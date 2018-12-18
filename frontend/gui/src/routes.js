import React from 'react';
import { Route } from 'react-router-dom';

import PostsList from './containers/PostsListView';
import PostsDetails from './containers/PostsDetailView';

const BaseRouter = () => (
    <div>
        <Route exact path='/' component={PostsList} />
        <Route exact path='/:postID' component={PostsDetails} />
    </div>
);

export default BaseRouter;