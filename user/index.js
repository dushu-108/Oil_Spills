import express from 'express';
import { config as configDotenv } from 'dotenv';
import cors from 'cors';
import router from "./routes/authRoutes.js";
import mongoose from 'mongoose';

configDotenv();

mongoose.connect(process.env.MONGO_URL)
.then(() => console.log('Connected to database'))
.catch((err) => console.log('Database not connected', err));

// Initialize Express app
const app = express();
const PORT = 4000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use("/", router);

// Start server
app.listen(PORT, () => {
    console.log(`App running on port ${PORT}`);
});
