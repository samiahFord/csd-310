#Samiah Ford    Module 7    04-20-2023
import mysql.connector
from mysql.connector import errorcode

config = {
    "user" : "movies_user",
    "password" : "popcorn",
    "host": "127.0.0.1",
    "database" : "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    #Select all from studio table
    cursor.execute("SELECT * FROM studio")
    print("-- DISPLAYING Studio RECORDS --\n")
    studios = cursor.fetchall()

    for studio in studios:
        print(f'Studio ID :  {studio[0]}\n')
        print(f'Studio Name : {studio[1]}\n\n')

    print('\n')
    #select all from genre table
    cursor.execute("SELECT * FROM genre")
    print("-- DISPLAYING Genre RECORDS --\n")
    genres = cursor.fetchall()

    for genre in genres:
        print(f'Genre ID :  {genre[0]}\n')
        print(f'Genre Name : {genre[1]}\n\n')
    print('\n')
    
    #select movie name where runtime is less than 2 hours
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120 ")
    print("-- DISPLAYING Short Film RECORDS --\n")
    films = cursor.fetchall()

    for film in films:
        print(f'Film Name :  {film[0]}\n')
        print(f'Runtime : {film[1]}\n\n')
    print('\n')

    #select film names and directors ordered by directors
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    print("-- DISPLAYING Director RECORDS in Order --\n")
    films = cursor.fetchall()

    for film in films:
        print(f'Film Name :  {film[0]}\n')
        print(f'Director : {film[1]}\n\n')
    print('\n')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("     The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("     The specified database does not exist")

    else:
        print(err)

finally:
        db.close()