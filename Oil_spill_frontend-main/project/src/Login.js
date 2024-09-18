import React from 'react';


const Login = ({ onClose }) => {
    return (
        <div className="login-modal">
            <div className="login-content">
                <h2>Login</h2>
                <form>
                    <div className="form-group">
                        <label htmlFor="email">Email</label>
                        <input type="email" id="email" placeholder="Enter your email" required />
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">Password</label>
                        <input type="password" id="password" placeholder="Enter your password" required />
                    </div>
                    <button type="submit" className="login-btn">Login</button>
                </form>
                <button className="close-btn" onClick={onClose}>Close</button>
            </div>
        </div>
    );
};

export default Login;
