const { v4: uuidv4 } = require('uuid');

class Player {
  constructor(name, gamertag, skill = 'beginner') {
    this.id = uuidv4();
    this.name = name;
    this.gamertag = gamertag;
    this.skill = skill; // beginner, intermediate, advanced, pro
    this.wins = 0;
    this.losses = 0;
    this.createdAt = new Date();
  }

  updateStats(won) {
    if (won) {
      this.wins++;
    } else {
      this.losses++;
    }
  }

  getWinRate() {
    const total = this.wins + this.losses;
    return total > 0 ? ((this.wins / total) * 100).toFixed(2) : 0;
  }
}

module.exports = Player;
