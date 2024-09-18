import React, { useState } from 'react';
import SignUp from './SignUp'; // Import SignUp component
import Login from './Login'; // Import Login component


const Sidebar = () => {
    const [isCollapsed, setCollapsed] = useState(false);
    const [showSignUp, setShowSignUp] = useState(false); // Track SignUp modal visibility
    const [showLogin, setShowLogin] = useState(false); // Track Login modal visibility

    // Handle sidebar toggle (collapse/expand)
    const toggleSidebar = () => {
        setCollapsed(!isCollapsed);
    };

    // Handle opening and closing of the Sign Up modal
    const toggleSignUpModal = () => {
        setShowSignUp(!showSignUp);
    };

    // Handle opening and closing of the Login modal
    const toggleLoginModal = () => {
        setShowLogin(!showLogin);
    };

    return (
        <>
            <div className={`sidebar ${isCollapsed ? 'collapsed' : ''}`}>
                <div className="sidebar-header">
                    <h3>{isCollapsed ? '' : 'custom options'}</h3>
                    <button className="toggle-btn" onClick={toggleSidebar}>
                        {isCollapsed ? '>>' : '<<'}
                    </button>
                </div>
                <ul className="sidebar-menu">
                    <li className="sidebar-item">
                        <i className="fas fa-ship"></i>
                        {!isCollapsed && <span>Ships</span>}
                    </li>
                    <li className="sidebar-item">
                        <i className="fas fa-anchor"></i>
                        {!isCollapsed && <span>Ports</span>}
                    </li>
                    <li className="sidebar-item">
                        <i className="fas fa-globe"></i>
                        {!isCollapsed && <span>Map</span>}
                    </li>
                    <li className="sidebar-item">
                        <i className="fas fa-info-circle"></i>
                        {!isCollapsed && <span>About</span>}
                    </li>
                    <li className="sidebar-item" onClick={toggleSignUpModal}>
                        <i className="fas fa-user-plus"></i>
                        {!isCollapsed && <span>Sign up</span>}
                    </li>
                    <li className="sidebar-item" onClick={toggleLoginModal}>
                        <i className="fas fa-sign-in-alt"></i>
                        {!isCollapsed && <span>Login</span>}
                    </li>
                </ul>
            </div>

            {/* Show the Sign Up modal if the button is clicked */}
            {showSignUp && <SignUp onClose={toggleSignUpModal} />}
            {/* Show the Login modal if the button is clicked */}
            {showLogin && <Login onClose={toggleLoginModal} />}
        </>
    );
};

export default Sidebar;
