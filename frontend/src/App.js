import React from 'react';
import './App.css';
import MyRoutes from './Components/MyRoutes';
import MyNavigations from './Components/MyNavigations';
import {BrowserRouter as Router} from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Router>
        <MyNavigations/>
        <MyRoutes/>
      </Router>
    </div>
  );
}

export default App;
