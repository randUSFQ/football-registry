const Tournament = require('../models/Tournament');
const { teams } = require('./teamController');

// In-memory storage
const tournaments = new Map();

exports.createTournament = (req, res) => {
  try {
    const { name, type, maxTeams } = req.body;
    
    if (!name) {
      return res.status(400).json({ error: 'Tournament name is required' });
    }

    const tournament = new Tournament(name, type, maxTeams);
    tournaments.set(tournament.id, tournament);
    
    res.status(201).json(tournament);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.getAllTournaments = (req, res) => {
  try {
    const tournamentList = Array.from(tournaments.values());
    res.json(tournamentList);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.getTournament = (req, res) => {
  try {
    const { id } = req.params;
    const tournament = tournaments.get(id);
    
    if (!tournament) {
      return res.status(404).json({ error: 'Tournament not found' });
    }
    
    res.json(tournament);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.addTeamToTournament = (req, res) => {
  try {
    const { id } = req.params;
    const { teamId } = req.body;
    const tournament = tournaments.get(id);
    
    if (!tournament) {
      return res.status(404).json({ error: 'Tournament not found' });
    }

    if (!teams.has(teamId)) {
      return res.status(404).json({ error: 'Team not found' });
    }

    if (tournament.addTeam(teamId)) {
      res.json(tournament);
    } else {
      res.status(400).json({ error: 'Cannot add team (tournament full or already started)' });
    }
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.removeTeamFromTournament = (req, res) => {
  try {
    const { id, teamId } = req.params;
    const tournament = tournaments.get(id);
    
    if (!tournament) {
      return res.status(404).json({ error: 'Tournament not found' });
    }

    if (tournament.removeTeam(teamId)) {
      res.json(tournament);
    } else {
      res.status(400).json({ error: 'Cannot remove team (tournament already started or team not in tournament)' });
    }
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.startTournament = (req, res) => {
  try {
    const { id } = req.params;
    const tournament = tournaments.get(id);
    
    if (!tournament) {
      return res.status(404).json({ error: 'Tournament not found' });
    }

    if (tournament.startTournament()) {
      res.json(tournament);
    } else {
      res.status(400).json({ error: 'Cannot start tournament (need at least 2 teams or already started)' });
    }
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.recordMatchResult = (req, res) => {
  try {
    const { id, matchId } = req.params;
    const { team1Score, team2Score } = req.body;
    const tournament = tournaments.get(id);
    
    if (!tournament) {
      return res.status(404).json({ error: 'Tournament not found' });
    }

    if (team1Score === undefined || team2Score === undefined) {
      return res.status(400).json({ error: 'Both team scores are required' });
    }

    if (tournament.recordMatchResult(matchId, team1Score, team2Score)) {
      res.json(tournament);
    } else {
      res.status(400).json({ error: 'Cannot record result (match not found or already completed)' });
    }
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.deleteTournament = (req, res) => {
  try {
    const { id } = req.params;
    
    if (!tournaments.has(id)) {
      return res.status(404).json({ error: 'Tournament not found' });
    }
    
    tournaments.delete(id);
    res.status(204).send();
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// Export tournaments map
exports.tournaments = tournaments;
