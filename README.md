# Football Registry ⚽

Sistema de gestión de torneos de fútbol virtual PES (Pro Evolution Soccer). Aplicación web para registrar jugadores, crear equipos y organizar campeonatos de fútbol virtual.

## Características

- 👤 **Gestión de Jugadores**: Registra jugadores con su gamertag, nivel de habilidad y estadísticas
- 👥 **Gestión de Equipos**: Crea equipos y asigna jugadores
- 🏆 **Gestión de Torneos**: Organiza torneos con diferentes formatos:
  - Eliminación directa
  - Todos contra todos
  - Liga
- 📊 **Seguimiento de Partidos**: Registra resultados y visualiza estadísticas
- 🎮 **Interfaz Web**: Interfaz moderna y responsive para gestionar todo desde el navegador

## Tecnologías

- **Backend**: Node.js + Express
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Almacenamiento**: En memoria (puede expandirse a base de datos)

## Instalación

### Requisitos previos

- Node.js (v14 o superior)
- npm (v6 o superior)

### Pasos de instalación

1. Clona el repositorio:
```bash
git clone https://github.com/randUSFQ/football-registry.git
cd football-registry
```

2. Instala las dependencias:
```bash
npm install
```

3. Inicia el servidor:
```bash
npm start
```

O para desarrollo con recarga automática:
```bash
npm run dev
```

4. Abre tu navegador en: `http://localhost:3000`

## Uso

### API Endpoints

#### Jugadores

- `POST /api/players` - Crear jugador
  ```json
  {
    "name": "Juan Pérez",
    "gamertag": "JuanPES",
    "skill": "intermediate"
  }
  ```

- `GET /api/players` - Obtener todos los jugadores
- `GET /api/players/:id` - Obtener un jugador
- `PUT /api/players/:id` - Actualizar jugador
- `DELETE /api/players/:id` - Eliminar jugador

#### Equipos

- `POST /api/teams` - Crear equipo
  ```json
  {
    "name": "Los Campeones",
    "captain": "player-id"
  }
  ```

- `GET /api/teams` - Obtener todos los equipos
- `GET /api/teams/:id` - Obtener un equipo
- `POST /api/teams/:id/players` - Agregar jugador al equipo
- `DELETE /api/teams/:id/players/:playerId` - Remover jugador del equipo
- `DELETE /api/teams/:id` - Eliminar equipo

#### Torneos

- `POST /api/tournaments` - Crear torneo
  ```json
  {
    "name": "Copa PES 2024",
    "type": "single-elimination",
    "maxTeams": 8
  }
  ```

- `GET /api/tournaments` - Obtener todos los torneos
- `GET /api/tournaments/:id` - Obtener un torneo
- `POST /api/tournaments/:id/teams` - Agregar equipo al torneo
- `DELETE /api/tournaments/:id/teams/:teamId` - Remover equipo del torneo
- `POST /api/tournaments/:id/start` - Iniciar torneo
- `POST /api/tournaments/:id/matches/:matchId/result` - Registrar resultado de partido
  ```json
  {
    "team1Score": 3,
    "team2Score": 1
  }
  ```
- `DELETE /api/tournaments/:id` - Eliminar torneo

### Interfaz Web

La aplicación incluye una interfaz web completa con tres secciones principales:

1. **Jugadores**: Registra y gestiona jugadores
2. **Equipos**: Crea y administra equipos
3. **Torneos**: Organiza y ejecuta torneos

## Estructura del Proyecto

```
football-registry/
├── src/
│   ├── controllers/       # Lógica de negocio
│   │   ├── playerController.js
│   │   ├── teamController.js
│   │   └── tournamentController.js
│   ├── models/           # Modelos de datos
│   │   ├── Player.js
│   │   ├── Team.js
│   │   └── Tournament.js
│   ├── routes/           # Rutas de la API
│   │   ├── players.js
│   │   ├── teams.js
│   │   └── tournaments.js
│   ├── public/           # Archivos estáticos
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── app.js
│   ├── views/            # Vistas HTML
│   │   └── index.html
│   └── server.js         # Servidor principal
├── package.json
├── .gitignore
└── README.md
```

## Contribución

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Mejoras Futuras

- [ ] Integración con base de datos (MongoDB/PostgreSQL)
- [ ] Sistema de autenticación de usuarios
- [ ] Chat en tiempo real para coordinación de partidos
- [ ] Estadísticas avanzadas y gráficos
- [ ] Sistema de rankings y puntos
- [ ] Notificaciones por email/SMS
- [ ] Exportación de resultados a PDF/Excel
- [ ] Modo oscuro
- [ ] Aplicación móvil

## Licencia

ISC

## Autor

Desarrollado para la comunidad de jugadores de PES