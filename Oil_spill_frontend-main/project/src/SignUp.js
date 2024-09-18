import React from 'react';
const SignUp = ({ onClose }) => {
    return (
        <div className="signup-modal">
            <div className="signup-content">
                <h2>Create Account</h2>
                <form>
                    <div className="form-group">
                        <label htmlFor="name">Name</label>
                        <input type="text" id="name" placeholder="Enter your name" required />
                    </div>
                    <div className="form-group">
                        <label htmlFor="email">Email</label>
                        <input type="email" id="email" placeholder="Enter your email" required />
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">Password</label>
                        <input type="password" id="password" placeholder="Enter your password" required />
                    </div>
                    <button type="submit" className="signup-btn">Sign Up</button>
                </form>
                <button className="close-btn" onClick={onClose}>X</button>
            </div>
        </div>
    );
};

export default SignUp;
