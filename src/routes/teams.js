const express = require('express');
const router = express.Router();
const teamController = require('../controllers/teamController');

router.post('/', teamController.createTeam);
router.get('/', teamController.getAllTeams);
router.get('/:id', teamController.getTeam);
router.post('/:id/players', teamController.addPlayerToTeam);
router.delete('/:id/players/:playerId', teamController.removePlayerFromTeam);
router.delete('/:id', teamController.deleteTeam);

module.exports = router;
