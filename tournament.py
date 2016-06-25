#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connects to the PostgreSQL database.

    Args:
      database_name: the database name to make a connection to

    Returns:
      db: a database connection
      cursor : a database cursor
    """
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Error trying to connect to {} database.".format(database_name))


def deleteMatches():
    """Remove all the match records from the database."""
    DB, curs = connect()
    
    curs.execute("DELETE FROM match")  # Clear all rows in match table
    
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB, curs = connect()
    
    curs.execute("DELETE FROM player")  # Clear all rows in player table
    
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB, curs = connect()
    
    curs.execute("SELECT count(*) FROM player")
    count = curs.fetchone()  # Only one value to fetch in the table
    
    DB.close()
    
    return count[0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB, curs = connect()
    
    query = "INSERT INTO player (name) VALUES (%s);"
    parameter = (name,)  # use parameter to avoid SQL injection attach
    curs.execute(query, parameter)

    DB.commit()
    DB.close()
    
    
def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB, curs = connect()
    
    curs.execute("SELECT id, name, wins, matches FROM standings")
    records = curs.fetchall()

    DB.close()
    
    return records


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB, curs = connect()
    
    query = "INSERT INTO match (winner, loser) VALUES (%s, %s)"
    parameters = (winner, loser)
    curs.execute(query, parameters)

    DB.commit()
    DB.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pairings = []
    opponent1 = ()
    opponent2 = ()

    standings = playerStandings()
    for player in standings:  # loop through the standings
        pairing = ()
        if len(opponent1) == 0:
            # no first opponent yet, so set it
            opponent1 = player[0], player[1]
        else:  # got a first opponent, so set the second opponent
            opponent2 = player[0], player[1]
            # join the two tuples together to form the pairing
            pairing = opponent1 + opponent2
            pairings.append(pairing)  # add the pairing to the pairings list
            opponent1, opponent2 = (), ()  # reset opponents to blank
            
    return pairings
    