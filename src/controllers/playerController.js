const Player = require('../models/Player');

// In-memory storage (in production, use a database)
const players = new Map();

exports.createPlayer = (req, res) => {
  try {
    const { name, gamertag, skill } = req.body;
    
    if (!name || !gamertag) {
      return res.status(400).json({ error: 'Name and gamertag are required' });
    }

    const player = new Player(name, gamertag, skill);
    players.set(player.id, player);
    
    res.status(201).json(player);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.getAllPlayers = (req, res) => {
  try {
    const playerList = Array.from(players.values());
    res.json(playerList);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.getPlayer = (req, res) => {
  try {
    const { id } = req.params;
    const player = players.get(id);
    
    if (!player) {
      return res.status(404).json({ error: 'Player not found' });
    }
    
    res.json(player);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.updatePlayer = (req, res) => {
  try {
    const { id } = req.params;
    const player = players.get(id);
    
    if (!player) {
      return res.status(404).json({ error: 'Player not found' });
    }
    
    const { name, gamertag, skill } = req.body;
    if (name) player.name = name;
    if (gamertag) player.gamertag = gamertag;
    if (skill) player.skill = skill;
    
    res.json(player);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.deletePlayer = (req, res) => {
  try {
    const { id } = req.params;
    
    if (!players.has(id)) {
      return res.status(404).json({ error: 'Player not found' });
    }
    
    players.delete(id);
    res.status(204).send();
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// Export players map for use in other controllers
exports.players = players;
