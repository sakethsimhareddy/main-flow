import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import Notes from './pages/Notes';
import EditNote from './pages/EditNote';
import CreateNote from './pages/CreateNote';

export default function BasicExample() {
  return (
    <Router>
      <>
        <Switch>
          <Route exact path="/" component={Notes} />
          <Route exact path="/notes/:id/edit" component={EditNote} />
          <Route exact path="/notes/create" component={CreateNote} />
        </Switch>
      </>
    </Router>
  );
}
