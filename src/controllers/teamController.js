const Team = require('../models/Team');
const { players } = require('./playerController');

// In-memory storage
const teams = new Map();

exports.createTeam = (req, res) => {
  try {
    const { name, captain } = req.body;
    
    if (!name || !captain) {
      return res.status(400).json({ error: 'Name and captain are required' });
    }

    if (!players.has(captain)) {
      return res.status(404).json({ error: 'Captain player not found' });
    }

    const team = new Team(name, captain);
    teams.set(team.id, team);
    
    res.status(201).json(team);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.getAllTeams = (req, res) => {
  try {
    const teamList = Array.from(teams.values());
    res.json(teamList);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.getTeam = (req, res) => {
  try {
    const { id } = req.params;
    const team = teams.get(id);
    
    if (!team) {
      return res.status(404).json({ error: 'Team not found' });
    }
    
    res.json(team);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.addPlayerToTeam = (req, res) => {
  try {
    const { id } = req.params;
    const { playerId } = req.body;
    const team = teams.get(id);
    
    if (!team) {
      return res.status(404).json({ error: 'Team not found' });
    }

    if (!players.has(playerId)) {
      return res.status(404).json({ error: 'Player not found' });
    }

    if (team.addPlayer(playerId)) {
      res.json(team);
    } else {
      res.status(400).json({ error: 'Player already in team' });
    }
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.removePlayerFromTeam = (req, res) => {
  try {
    const { id, playerId } = req.params;
    const team = teams.get(id);
    
    if (!team) {
      return res.status(404).json({ error: 'Team not found' });
    }

    if (team.removePlayer(playerId)) {
      res.json(team);
    } else {
      res.status(400).json({ error: 'Cannot remove player (not in team or is captain)' });
    }
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.deleteTeam = (req, res) => {
  try {
    const { id } = req.params;
    
    if (!teams.has(id)) {
      return res.status(404).json({ error: 'Team not found' });
    }
    
    teams.delete(id);
    res.status(204).send();
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// Export teams map for use in other controllers
exports.teams = teams;
