import { useEffect, useState } from 'react'
import './App.css'
import Auth from './pages/auth/auth'
import Dash from './pages/dashboard/dash'
import Help from './pages/help/help'
import Connect from './pages/connect/connect'
import {BrowserRouter,Routes,Route} from "react-router-dom"


function App()
{
  return(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Auth />} />

      <Route path="/dashboard" element ={<Dash />} />


    <Route path="/help" element ={<Help />} />
    <Route path="/connect" element ={<Connect />} />
    



    </Routes>
  
  </BrowserRouter>
  );
}

export default App;
