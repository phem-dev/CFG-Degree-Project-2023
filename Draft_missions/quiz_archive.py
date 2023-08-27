# for using MySQL (requires users MySQL password) #####################################################################
#######################################################################################################################
# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
#     port='3306',
#     database='quiz_db'
# )

# cursor = mydb.cursor()
#######################################################################################################################

# for Using pythons built-in SQLite ###################################################################################
#######################################################################################################################

import os
import sqlite3
from sqlite3 import Error


def create_connection(db_file, sql_file):
    """ create a database connection to a SQLite database """
    global mydb, cursor
    mydb = None
    try:
        mydb = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
        return None, None

    cursor = mydb.cursor()

    # Check if the 'questions' table exists in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='questions'")
    table_exists = cursor.fetchone()

    # If the table doesn't exist, then create it using the SQL script
    if not table_exists:
        # Read the SQL file
        with open(sql_file, 'r') as f:
            sql_script = f.read()

        # Execute the SQL script
        cursor.executescript(sql_script)
        mydb.commit()

    return mydb, cursor

#######################################################################################################################


def fetch_random_questions(num_questions):
    cursor.execute('SELECT * FROM questions ORDER BY RANDOM() LIMIT ?', (num_questions,))
    questions = cursor.fetchall()
    return questions

def update_leaderboard(player_name, score):
    # Store the player's score and name in the leaderboard table
    cursor.execute('INSERT INTO leaderboard (name, score) VALUES (?, ?)', (player_name, score))
    mydb.commit()

def display_leaderboard():
    cursor.execute('SELECT name, score FROM leaderboard ORDER BY score DESC LIMIT 10')
    leaderboard_data = cursor.fetchall()

    print("\nTop 10 Leaderboard:")
    for position, (name, score) in enumerate(leaderboard_data, start=1):
        print(f"{position}. {name}: {score}")


def main():
    global mydb, cursor
    mydb, cursor = create_connection('../Missions/Mission7_quiz_files/my.db', r"C:\Users\kirst\PycharmProjects\pythonProject3\quiz-multichoice_SQLite\Quiz_game.sql")

    if not mydb or not cursor:
        print("Failed to connect to database.")
        return

    print("Welcome to the Quiz Game!")
    player_name = input("Enter your name or character: ")

    score = 0
    num_questions_to_answer = 10  # Number of questions to answer

    questions = fetch_random_questions(num_questions_to_answer)

    for question in questions:
        print(question[1])  # Print the question

        options = question[2:6]
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")

        user_answer = int(input("Select your answer (1-4): ")) - 1

        if user_answer == question[6] - 1:
            print("Correct!\n")
            score += 1
        else:
            correct_option_index = question[6] - 1
            correct_option = options[correct_option_index]
            print(f"Incorrect. The correct answer was: {correct_option}\n")

    print(f"Your final score is: {score}/{num_questions_to_answer}")

    update_leaderboard(player_name, score)
    display_leaderboard()


if __name__ == "__main__":
    main()
    if mydb:  # Only close if the connection exists
        mydb.close()

