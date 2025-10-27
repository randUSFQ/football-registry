const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path');

const playerRoutes = require('./routes/players');
const teamRoutes = require('./routes/teams');
const tournamentRoutes = require('./routes/tournaments');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// API Routes
app.use('/api/players', playerRoutes);
app.use('/api/teams', teamRoutes);
app.use('/api/tournaments', tournamentRoutes);

// Serve index page
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'index.html'));
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'ok', message: 'Football Registry API is running' });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
  console.log(`⚽ Football Registry API running on port ${PORT}`);
  console.log(`📊 Visit http://localhost:${PORT} to access the web interface`);
});

module.exports = app;
