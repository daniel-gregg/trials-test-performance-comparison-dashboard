const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(helmet());
app.use(cors());
app.use(morgan('combined'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.get('/api/health', (req, res) => {
  res.json({ status: 'OK', message: 'Trials Dashboard API is running' });
});

// Trials data endpoints
app.get('/api/trials', (req, res) => {
  // Placeholder for getting all trials
  res.json({ 
    trials: [],
    message: 'Trials endpoint ready for implementation' 
  });
});

app.post('/api/trials', (req, res) => {
  // Placeholder for creating new trial
  res.json({ 
    message: 'Trial creation endpoint ready for implementation',
    data: req.body 
  });
});

// Price data endpoints
app.get('/api/prices', (req, res) => {
  // Placeholder for getting price data
  res.json({ 
    prices: [],
    message: 'Prices endpoint ready for implementation' 
  });
});

app.post('/api/prices', (req, res) => {
  // Placeholder for updating prices
  res.json({ 
    message: 'Price update endpoint ready for implementation',
    data: req.body 
  });
});

// Performance comparison endpoint
app.post('/api/compare', (req, res) => {
  // Placeholder for performance comparison logic
  res.json({ 
    comparison: {},
    message: 'Comparison endpoint ready for implementation',
    inputData: req.body 
  });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// 404 handler
app.use('*', (req, res) => {
  res.status(404).json({ error: 'Route not found' });
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
  console.log(`API Health Check: http://localhost:${PORT}/api/health`);
});

module.exports = app;