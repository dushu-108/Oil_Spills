import express from "express";
import userModel from "../models/user.js";

// Test route
const test = (req, res) => {
    res.json("test successful");
}

// Register a new user
const registerUser = async (req, res) => {
    try {
        const { name, email, password } = req.body;

        // Validate name
        if (!name) {
            return res.status(400).json({
                error: 'Name is required',
            });
        }

        // Validate password
        if (!password || password.length < 6) {
            return res.status(400).json({
                error: 'Password is required and should be at least 6 characters long',
            });
        }

        // Check if the email already exists
        const exists = await userModel.findOne({ email });
        if (exists) {
            return res.status(400).json({
                error: 'Email already exists',
            });
        }

        // Create the user
        const user = await userModel.create({
            name,
            email,
            password,
        });

        // Return the user object as a response
        return res.status(201).json(user);
    } catch (error) {
        console.error(error);
        return res.status(500).json({
            error: 'Server error. Please try again later.',
        });
    }
}

// Get all users
const getUsers = async (req, res) => {
    try {
        const users = await userModel.find({});
        return res.status(200).json(users);
    } catch (error) {
        console.error(error);
        return res.status(500).json({
            error: 'Failed to fetch users. Please try again later.',
        });
    }
}

export { test, registerUser, getUsers };

