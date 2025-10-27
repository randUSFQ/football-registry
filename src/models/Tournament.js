const { v4: uuidv4 } = require('uuid');

class Tournament {
  constructor(name, type = 'single-elimination', maxTeams = 8) {
    this.id = uuidv4();
    this.name = name;
    this.type = type; // single-elimination, round-robin, league
    this.maxTeams = maxTeams;
    this.teams = [];
    this.matches = [];
    this.status = 'registration'; // registration, ongoing, completed
    this.winner = null;
    this.createdAt = new Date();
    this.startedAt = null;
    this.completedAt = null;
  }

  addTeam(teamId) {
    if (this.teams.length < this.maxTeams && this.status === 'registration') {
      this.teams.push(teamId);
      return true;
    }
    return false;
  }

  removeTeam(teamId) {
    if (this.status === 'registration') {
      const index = this.teams.indexOf(teamId);
      if (index > -1) {
        this.teams.splice(index, 1);
        return true;
      }
    }
    return false;
  }

  startTournament() {
    if (this.teams.length >= 2 && this.status === 'registration') {
      this.status = 'ongoing';
      this.startedAt = new Date();
      this.generateMatches();
      return true;
    }
    return false;
  }

  generateMatches() {
    // Generate initial bracket matches
    for (let i = 0; i < this.teams.length; i += 2) {
      if (i + 1 < this.teams.length) {
        this.matches.push({
          id: uuidv4(),
          team1: this.teams[i],
          team2: this.teams[i + 1],
          team1Score: null,
          team2Score: null,
          round: 1,
          winner: null,
          completed: false
        });
      }
    }
  }

  recordMatchResult(matchId, team1Score, team2Score) {
    const match = this.matches.find(m => m.id === matchId);
    if (match && !match.completed) {
      match.team1Score = team1Score;
      match.team2Score = team2Score;
      match.winner = team1Score > team2Score ? match.team1 : match.team2;
      match.completed = true;
      
      // Check if tournament is complete
      this.checkTournamentComplete();
      return true;
    }
    return false;
  }

  checkTournamentComplete() {
    const allMatchesCompleted = this.matches.every(m => m.completed);
    if (allMatchesCompleted && this.matches.length > 0) {
      // Find the winner from the last match
      const lastRound = Math.max(...this.matches.map(m => m.round));
      const finalMatch = this.matches.find(m => m.round === lastRound);
      if (finalMatch) {
        this.winner = finalMatch.winner;
        this.status = 'completed';
        this.completedAt = new Date();
      }
    }
  }
}

module.exports = Tournament;
