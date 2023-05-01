import { useState } from 'react'
import { NavLink } from 'react-router-dom'
// import { ReactComponent as Hamburger } from '../../assets/icons/hamburger.svg'
// import { ReactComponent as Brand } from '../../assets/icons/logo.svg'
import './TopNavigation.css'

const TopNavigation = () => {
  const [showNavbar, setShowNavbar] = useState(false)

  const handleShowNavbar = () => {
    setShowNavbar(!showNavbar)
  }

  return (
    <div>
        <div className='top-heading'>
            <h2>Personalized Smart Home control</h2>
        </div>
        <nav className="navbar">
        <div className="container">
            <div className="logo">
            {/* <Brand /> */}
            </div>
            <div className="menu-icon" onClick={handleShowNavbar}>
            {/* <Hamburger /> */}
            </div>
            <div className={`nav-elements  ${showNavbar && 'active'}`}>
            <ul>
                <li>
                <NavLink to="/">Dashboard</NavLink>
                </li>
                <li>
                <NavLink to="/personaldata">Personal Data</NavLink>
                </li>
                <li>
                <NavLink to="/mlmodel">Machine Learning model</NavLink>
                </li>
                <li>
                <NavLink to="/control">Control weather</NavLink>
                </li>
                <li>
                <NavLink to="/contact">Contact</NavLink>
                </li>
            </ul>
            </div>
        </div>
        </nav>
    </div>
  )
}

export default TopNavigation;