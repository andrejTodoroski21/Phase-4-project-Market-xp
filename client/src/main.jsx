import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './components/App.jsx'
import Home from './components/Home.jsx'
import Listings from './components/Listings.jsx'
import Profile from './components/Profile.jsx'
import About from './components/About.jsx'
import Login from './components/UserPanel/Login.jsx'
import Signup from './components/UserPanel/Signup.jsx'
import NewListing from './components/NewListing.jsx'

import './index.css'

import { createBrowserRouter, RouterProvider } from 'react-router-dom'


//ROUTES
const routes = [
  {
    path: "/",
    element: <App />,
    children: [
      {
        index: true,
        element: <Home />
      },
      {
        path: "listings",
        element: <Listings />
      },
      {
        path: "profile",
        element: <Profile />
      },
      {
        path: "about",
        element: <About />
      },
      {
        path: "login",
        element: <Login />
      },
      {
        path: 'signup',
        element: <Signup />
      },
      {
        path: "newlisting",
        element: <NewListing />
      },
    ]
  }
]

const router = createBrowserRouter(routes)

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
