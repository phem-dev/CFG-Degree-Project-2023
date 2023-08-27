import sqlite3

given_number_of_questions = 10

class QuizGame:
    def __init__(self, db_file, sql_file, number_of_questions=given_number_of_questions):
        """
        Initialize the QuizGame object.

        :param db_file: Path to the SQLite database file.
        :param sql_file: Path to the SQL file containing setup scripts.
        :param number_of_questions: Number of questions for the quiz. Default is 10.
        """
        self.correct = None  # Keeps track of whether the last answer was correct or not
        self.db_file = db_file
        self.sql_file = sql_file
        self.conn, self.cursor = self.create_connection()  # Establish a connection to the database
        self.num_questions_to_answer = number_of_questions
        self.question_list = []  # List to store fetched questions
        self.score = 0  # Player's current score
        self.result_msg = ""  # Message displaying result of the last answered question

    def create_connection(self):
        """Establish a connection to the SQLite database and set up tables if needed."""
        conn = sqlite3.connect(self.db_file)

        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='questions'")

        # If table 'questions' doesn't exist, create it using the SQL file
        if not cursor.fetchone():
            with open(self.sql_file, 'r') as f:
                cursor.executescript(f.read())
            conn.commit()

        return conn, cursor

    def fetch_random_questions(self, num_questions=given_number_of_questions):
        """
        Fetch a set of random questions from the database.

        :param num_questions: Number of questions to fetch. Default is 10.
        :return: A list of questions from the database.
        """
        if num_questions is None:
            num_questions = self.num_questions_to_answer
        self.cursor.execute('SELECT * FROM questions ORDER BY RANDOM() LIMIT ?', (num_questions,))
        return self.cursor.fetchall()

    def update_leaderboard(self, player_name, score):
        """
        Insert the player's name and score into the leaderboard table.

        :param player_name: The name of the player.
        :param score: The score of the player.
        """
        self.cursor.execute('INSERT INTO leaderboard (name, score) VALUES (?, ?)', (player_name, score))
        self.conn.commit()

    def display_leaderboard(self):
        """
        Display the top 10 players from the leaderboard.

        :return: A formatted string of the top 10 players and their scores.
        """
        self.cursor.execute('SELECT name, score FROM leaderboard ORDER BY score DESC LIMIT 10')
        leaderboard_data = self.cursor.fetchall()

        leaderboard_str = "Top 10 Leaderboard:|"
        for position, (name, score) in enumerate(leaderboard_data, start=1):
            leaderboard_str += f"{position}. {name}: {score}|"
        return leaderboard_str

    def check_answer(self, question, user_answer):
        """
        Check the user's answer and return the result.

        :param question: The question tuple from the database.
        :param user_answer: The user's selected answer.
        :return: A tuple containing a result message and a boolean indicating if the answer was correct.
        """
        options = question[2:6]  # Extract options from the question tuple

        if user_answer == question[6]:
            self.result_msg = "Correct!"
            self.correct = True
        else:
            correct_option_index = question[6] - 1
            self.result_msg = f"Incorrect. |The correct answer was: {options[correct_option_index]}"
            self.correct = False

        return self.result_msg, self.correct

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()

    def end_message(self, player_name, score):
        """
        Display the end message with the player's score and the leaderboard.

        :param score: The score of the player.
        :return: A tuple containing the player's score message and the leaderboard.

        Args:
            player_name: this is not used here but given as an argument in the integration
         """
        return f"You scored: {score}/{self.num_questions_to_answer}", self.display_leaderboard()
