-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

CREATE TABLE player (id serial primary key,
						name text);

CREATE TABLE match (id serial primary key,
					winner int references player(id),
					loser int references player(id));

-- Get of view of the wins by each player
CREATE VIEW wins_by_player AS
	SELECT player.id, player.name, count(match.winner) as wins
	FROM player LEFT JOIN match
	ON player.id = match.winner
	GROUP BY player.id;

-- Get of view of the loses by each player
CREATE VIEW loses_by_player AS
	SELECT player.id, player.name, count(match.loser) as loses
	FROM player LEFT JOIN match
	ON player.id = match.loser
	GROUP BY player.id;

-- Join the two views together to make a single standings view of wins, loses and total matches
--- (note: matches = wins + loses)
CREATE VIEW standings AS
	SELECT wins_by_player.id, wins_by_player.name, wins_by_player.wins, loses_by_player.loses, wins+loses as matches
	FROM wins_by_player JOIN loses_by_player
	ON wins_by_player.id = loses_by_player.id
	ORDER BY wins DESC;




