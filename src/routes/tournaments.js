const express = require('express');
const router = express.Router();
const tournamentController = require('../controllers/tournamentController');

router.post('/', tournamentController.createTournament);
router.get('/', tournamentController.getAllTournaments);
router.get('/:id', tournamentController.getTournament);
router.post('/:id/teams', tournamentController.addTeamToTournament);
router.delete('/:id/teams/:teamId', tournamentController.removeTeamFromTournament);
router.post('/:id/start', tournamentController.startTournament);
router.post('/:id/matches/:matchId/result', tournamentController.recordMatchResult);
router.delete('/:id', tournamentController.deleteTournament);

module.exports = router;
