const API_URL = '/api';

// Global state
let players = [];
let teams = [];
let tournaments = [];

// Tab management
function showTab(tabName, event) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remove active class from all buttons
    document.querySelectorAll('.tab-button').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab
    document.getElementById(tabName).classList.add('active');
    if (event && event.target) {
        event.target.classList.add('active');
    }
    
    // Load data for the tab
    if (tabName === 'players') {
        loadPlayers();
    } else if (tabName === 'teams') {
        loadTeams();
    } else if (tabName === 'tournaments') {
        loadTournaments();
    }
}

// Player functions
function showPlayerForm() {
    document.getElementById('playerForm').style.display = 'block';
}

function hidePlayerForm() {
    document.getElementById('playerForm').style.display = 'none';
    document.getElementById('playerForm').querySelector('form').reset();
}

async function createPlayer(event) {
    event.preventDefault();
    
    const name = document.getElementById('playerName').value;
    const gamertag = document.getElementById('playerGamertag').value;
    const skill = document.getElementById('playerSkill').value;
    
    try {
        const response = await fetch(`${API_URL}/players`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, gamertag, skill })
        });
        
        if (response.ok) {
            hidePlayerForm();
            loadPlayers();
        } else {
            alert('Error al crear jugador');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error al crear jugador');
    }
}

async function loadPlayers() {
    try {
        const response = await fetch(`${API_URL}/players`);
        players = await response.json();
        renderPlayers();
    } catch (error) {
        console.error('Error loading players:', error);
    }
}

function renderPlayers() {
    const container = document.getElementById('playersList');
    
    if (players.length === 0) {
        container.innerHTML = '<div class="empty-state"><h3>No hay jugadores registrados</h3><p>Crea tu primer jugador para comenzar</p></div>';
        return;
    }
    
    container.innerHTML = players.map(player => `
        <div class="card">
            <h3>${player.name}</h3>
            <div class="card-info">
                <p><strong>Gamertag:</strong> ${player.gamertag}</p>
                <p><strong>Nivel:</strong> <span class="badge badge-primary">${getSkillLabel(player.skill)}</span></p>
                <p><strong>Victorias:</strong> ${player.wins} | <strong>Derrotas:</strong> ${player.losses}</p>
                <p><strong>Ratio de Victorias:</strong> ${player.wins + player.losses > 0 ? ((player.wins / (player.wins + player.losses)) * 100).toFixed(2) : 0}%</p>
            </div>
            <div class="card-actions">
                <button class="btn-danger" onclick="deletePlayer('${player.id}')">Eliminar</button>
            </div>
        </div>
    `).join('');
}

function getSkillLabel(skill) {
    const labels = {
        'beginner': 'Principiante',
        'intermediate': 'Intermedio',
        'advanced': 'Avanzado',
        'pro': 'Profesional'
    };
    return labels[skill] || skill;
}

async function deletePlayer(id) {
    if (!confirm('¿Estás seguro de eliminar este jugador?')) return;
    
    try {
        await fetch(`${API_URL}/players/${id}`, { method: 'DELETE' });
        loadPlayers();
    } catch (error) {
        console.error('Error:', error);
    }
}

// Team functions
function showTeamForm() {
    // Populate captain select
    const select = document.getElementById('teamCaptain');
    select.innerHTML = '<option value="">Seleccionar jugador...</option>' + 
        players.map(p => `<option value="${p.id}">${p.name} (${p.gamertag})</option>`).join('');
    
    document.getElementById('teamForm').style.display = 'block';
}

function hideTeamForm() {
    document.getElementById('teamForm').style.display = 'none';
    document.getElementById('teamForm').querySelector('form').reset();
}

async function createTeam(event) {
    event.preventDefault();
    
    const name = document.getElementById('teamName').value;
    const captain = document.getElementById('teamCaptain').value;
    
    try {
        const response = await fetch(`${API_URL}/teams`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, captain })
        });
        
        if (response.ok) {
            hideTeamForm();
            loadTeams();
        } else {
            alert('Error al crear equipo');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error al crear equipo');
    }
}

async function loadTeams() {
    try {
        const response = await fetch(`${API_URL}/teams`);
        teams = await response.json();
        renderTeams();
    } catch (error) {
        console.error('Error loading teams:', error);
    }
}

function renderTeams() {
    const container = document.getElementById('teamsList');
    
    if (teams.length === 0) {
        container.innerHTML = '<div class="empty-state"><h3>No hay equipos registrados</h3><p>Crea tu primer equipo para comenzar</p></div>';
        return;
    }
    
    container.innerHTML = teams.map(team => {
        const captain = players.find(p => p.id === team.captain);
        const playerNames = team.players.map(pid => {
            const player = players.find(p => p.id === pid);
            return player ? player.name : 'Desconocido';
        });
        
        return `
            <div class="card">
                <h3>${team.name}</h3>
                <div class="card-info">
                    <p><strong>Capitán:</strong> ${captain ? captain.name : 'Desconocido'}</p>
                    <p><strong>Jugadores:</strong> ${team.players.length}</p>
                    <div>
                        ${playerNames.map(name => `<span class="badge badge-info">${name}</span>`).join('')}
                    </div>
                </div>
                <div class="card-actions">
                    <button class="btn-danger" onclick="deleteTeam('${team.id}')">Eliminar</button>
                </div>
            </div>
        `;
    }).join('');
}

async function deleteTeam(id) {
    if (!confirm('¿Estás seguro de eliminar este equipo?')) return;
    
    try {
        await fetch(`${API_URL}/teams/${id}`, { method: 'DELETE' });
        loadTeams();
    } catch (error) {
        console.error('Error:', error);
    }
}

// Tournament functions
function showTournamentForm() {
    document.getElementById('tournamentForm').style.display = 'block';
}

function hideTournamentForm() {
    document.getElementById('tournamentForm').style.display = 'none';
    document.getElementById('tournamentForm').querySelector('form').reset();
}

async function createTournament(event) {
    event.preventDefault();
    
    const name = document.getElementById('tournamentName').value;
    const type = document.getElementById('tournamentType').value;
    const maxTeams = parseInt(document.getElementById('tournamentMaxTeams').value);
    
    try {
        const response = await fetch(`${API_URL}/tournaments`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, type, maxTeams })
        });
        
        if (response.ok) {
            hideTournamentForm();
            loadTournaments();
        } else {
            alert('Error al crear torneo');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error al crear torneo');
    }
}

async function loadTournaments() {
    try {
        const response = await fetch(`${API_URL}/tournaments`);
        tournaments = await response.json();
        renderTournaments();
    } catch (error) {
        console.error('Error loading tournaments:', error);
    }
}

function renderTournaments() {
    const container = document.getElementById('tournamentsList');
    
    if (tournaments.length === 0) {
        container.innerHTML = '<div class="empty-state"><h3>No hay torneos registrados</h3><p>Crea tu primer torneo para comenzar</p></div>';
        return;
    }
    
    container.innerHTML = tournaments.map(tournament => {
        const statusClass = `status-${tournament.status}`;
        const statusLabel = {
            'registration': 'En Registro',
            'ongoing': 'En Curso',
            'completed': 'Completado'
        };
        
        return `
            <div class="card">
                <h3>${tournament.name}</h3>
                <div class="card-info">
                    <p><strong>Tipo:</strong> ${getTournamentTypeLabel(tournament.type)}</p>
                    <p><strong>Equipos:</strong> ${tournament.teams.length}/${tournament.maxTeams}</p>
                    <div class="tournament-status ${statusClass}">
                        ${statusLabel[tournament.status]}
                    </div>
                    ${tournament.winner ? `<p><strong>🏆 Ganador:</strong> ${getTeamName(tournament.winner)}</p>` : ''}
                    ${tournament.matches.length > 0 ? renderMatches(tournament.matches) : ''}
                </div>
                <div class="card-actions">
                    ${tournament.status === 'registration' ? `
                        <button class="btn-success" onclick="startTournament('${tournament.id}')">Iniciar</button>
                    ` : ''}
                    ${tournament.status === 'ongoing' ? `
                        <button class="btn-info" onclick="viewTournamentDetails('${tournament.id}')">Ver Detalles</button>
                    ` : ''}
                    <button class="btn-danger" onclick="deleteTournament('${tournament.id}')">Eliminar</button>
                </div>
            </div>
        `;
    }).join('');
}

function getTournamentTypeLabel(type) {
    const labels = {
        'single-elimination': 'Eliminación Directa',
        'round-robin': 'Todos contra Todos',
        'league': 'Liga'
    };
    return labels[type] || type;
}

function getTeamName(teamId) {
    const team = teams.find(t => t.id === teamId);
    return team ? team.name : 'Desconocido';
}

function renderMatches(matches) {
    if (matches.length === 0) return '';
    
    return `
        <div class="match-list">
            <h4>Partidos:</h4>
            ${matches.map(match => `
                <div class="match-item ${match.completed ? 'completed' : ''}">
                    <strong>${getTeamName(match.team1)}</strong> vs <strong>${getTeamName(match.team2)}</strong>
                    ${match.completed ? 
                        ` - Resultado: ${match.team1Score} - ${match.team2Score}` : 
                        ' - Pendiente'}
                </div>
            `).join('')}
        </div>
    `;
}

async function startTournament(id) {
    if (!confirm('¿Iniciar el torneo? No se podrán agregar más equipos.')) return;
    
    try {
        const response = await fetch(`${API_URL}/tournaments/${id}/start`, {
            method: 'POST'
        });
        
        if (response.ok) {
            loadTournaments();
        } else {
            const data = await response.json();
            alert(data.error || 'Error al iniciar torneo');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error al iniciar torneo');
    }
}

function viewTournamentDetails(id) {
    const tournament = tournaments.find(t => t.id === id);
    if (tournament) {
        alert(`Detalles del torneo: ${tournament.name}\nPartidos: ${tournament.matches.length}\nCompletados: ${tournament.matches.filter(m => m.completed).length}`);
    }
}

async function deleteTournament(id) {
    if (!confirm('¿Estás seguro de eliminar este torneo?')) return;
    
    try {
        await fetch(`${API_URL}/tournaments/${id}`, { method: 'DELETE' });
        loadTournaments();
    } catch (error) {
        console.error('Error:', error);
    }
}

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    loadPlayers();
});
