const { v4: uuidv4 } = require('uuid');

class Team {
  constructor(name, captain) {
    this.id = uuidv4();
    this.name = name;
    this.captain = captain;
    this.players = [captain];
    this.createdAt = new Date();
  }

  addPlayer(playerId) {
    if (!this.players.includes(playerId)) {
      this.players.push(playerId);
      return true;
    }
    return false;
  }

  removePlayer(playerId) {
    const index = this.players.indexOf(playerId);
    if (index > -1 && playerId !== this.captain) {
      this.players.splice(index, 1);
      return true;
    }
    return false;
  }
}

module.exports = Team;
