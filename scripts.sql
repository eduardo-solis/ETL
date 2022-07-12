DROP DATABASE IF EXISTS etl;
CREATE DATABASE etl;
USE etl;

CREATE TABLE competicion(
	idCompeticion INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50)
);

CREATE TABLE equipo(
	idEquipo INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50)
);

CREATE TABLE competicion_equipo(
	idCompeticionEquipo INT PRIMARY KEY AUTO_INCREMENT,
    idCompeticion INT,
    idEquipo INT,
    FOREIGN KEY (idCompeticion) REFERENCES competicion(idCompeticion),
    FOREIGN KEY (idEquipo) REFERENCES equipo(idEquipo)
);

CREATE TABLE jugador(
	idJugador INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    apePaterno VARCHAR(50),
    apeMaterno VARCHAR(50),
    fechaNacimiento DATE,
    idEquipo INT,
    FOREIGN KEY (idEquipo) REFERENCES equipo(idEquipo)
);

CREATE TABLE temporada(
	idTemporada INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50)
);

CREATE TABLE estadistica(
	idEstadistica INT PRIMARY KEY AUTO_INCREMENT,
    partidos INT,
    goles INT,
    asistencias INT,
    idJugador INT,
    idTemporada INT,
    FOREIGN KEY (idJugador) REFERENCES jugador(idjugador),
    FOREIGN KEY (idTemporada) REFERENCES temporada(idTemporada)
);

INSERT INTO competicion(nombre) VALUES ('La Liga Santander'), ('Serie A'), ('Bundesliga');
INSERT INTO equipo(nombre) VALUES ('Real Madrid CF'), ('AC Milan'), ('Bayern Múnich');
INSERT INTO competicion_equipo(idCompeticion, idEquipo) VALUES (1, 1), (2, 2), (3, 3);
INSERT INTO temporada(nombre) VALUES
('1958-59'), 
('1971-72'), 
('1985-86'), 
('2003-04'),
('2010-11'),
('2011-12'),
('2014-15'),
('2019-20'),
('2021-22');

INSERT INTO jugador(nombre, apePaterno, apeMaterno, fechaNacimiento, idEquipo) VALUES
('Cristiano Ronaldo ', 'Dos Santos', ' Aveiro', '1985-02-05', 1),
('Marco', ' van Basten', null, '1964-02-05', 2),
('Gerhard ', 'Müller', null, '1945-11-03', 3),
('Karim Mostafa ', 'Benzema ', null, '1987-12-19', 1),
('Andriy', 'Mykolayovych  ', 'Shevchenko  ', '1976-06-25', 2),
('Robert ', ' Lewandowski', null, '1988-08-21', 3),
('Alfredo ', ' Di Stéfano', null, '1926-07-04', 1),
('Ruud', ' Gullit ', null, '1962-09-01', 2),
(' Arjen', ' Robben ', null, '1984-01-23', 3),
(' Mesut', 'Özil', null, '1988-10-13', 1),
('Zlatan ', 'Ibrahimović', null, '1981-10-31', 2),
(' Franck Henry', 'Ribéry', null, '1983-04-07', 3),
(' Luka', 'Modrić ', null, '1985-09-09', 1),
('Andrea ', 'Pirlo ', null, '1979-05-19', 2),
('Thomas ', 'Müller ', null, '1989-08-13', 3);

INSERT INTO estadistica(partidos, goles, asistencias, idJugador, idTemporada) VALUES
(35, 48, 16, 1, 7),
(31, 25, 6, 2, 3),
(34, 40, 5, 3, 2),
(32, 27, 12, 4, 9),
(32, 24, 3, 5, 4),
(29, 41, 7, 6, 8),
(28, 27, 5, 7, 1),
(30, 5, 15, 8, 3),
(26, 13, 11, 9, 6),
(35, 4, 19, 10, 6),
(32, 28, 8, 11, 5),
(27, 10, 15, 12, 6),
(28, 2, 8, 13, 7),
(30, 5, 10, 14, 5),
(33, 8, 21, 15, 8);

CREATE VIEW v_jugador AS
SELECT j.nombre, j.apePaterno, j.apeMaterno, j.fechaNacimiento, partidos, goles, asistencias, e.nombre AS equipo, c.Nombre AS competicion, t.Nombre AS temporada
FROM jugador j
INNER JOIN estadistica es ON j.idJugador = es.idJugador
INNER JOIN temporada t ON es.idTemporada = t.idTemporada
INNER JOIN equipo e ON j.idEquipo = e.idEquipo
INNER JOIN competicion_equipo ce ON ce.idEquipo = e.idEquipo
INNER JOIN competicion c ON c.idCompeticion = ce.idCompeticion
ORDER BY j.idJugador;
SELECT * FROM v_jugador;
