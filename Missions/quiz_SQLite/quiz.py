import sqlite3


class QuizGame:
    def __init__(self, db_file, sql_file, number_of_questions=10):
        self.db_file = db_file
        self.sql_file = sql_file
        self.conn, self.cursor = self.create_connection()
        self.num_questions_to_answer = number_of_questions
        self.question_list = []
        self.score = 0
        self.result_msg = ""

    def create_connection(self):
        """Establish a connection to the SQLite database and set up tables if needed."""
        conn = sqlite3.connect(self.db_file)

        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='questions'")

        if not cursor.fetchone():
            with open(self.sql_file, 'r') as f:
                cursor.executescript(f.read())
            conn.commit()

        return conn, cursor

    def fetch_random_questions(self, num_questions=None):
        """Fetch a set of random questions from the database."""
        if num_questions is None:
            num_questions = self.num_questions_to_answer
        self.cursor.execute('SELECT * FROM questions ORDER BY RANDOM() LIMIT ?', (num_questions,))
        return self.cursor.fetchall()

    def update_leaderboard(self, player_name, score):
        """Insert the player's name and score into the leaderboard table."""
        self.cursor.execute('INSERT INTO leaderboard (name, score) VALUES (?, ?)', (player_name, score))
        self.conn.commit()

    def display_leaderboard(self):
        """Display the top 10 players from the leaderboard."""
        self.cursor.execute('SELECT name, score FROM leaderboard ORDER BY score DESC LIMIT 10')
        leaderboard_data = self.cursor.fetchall()

        leaderboard_str = "Top 10 Leaderboard:|"
        for position, (name, score) in enumerate(leaderboard_data, start=1):
            leaderboard_str += f"{position}. {name}: {score}|"
        return leaderboard_str

    def provide_question(self, question):
        """Return a question from the list of random questions and its options for the user."""
        options = question[2:6]
        question_str = question[1]
        # answer_list = "|||" + "||".join([f"{i + 1}. {option}" for i, option in enumerate(options)])

        return question_str, options

    def get_provided_question(self, question_number):
        question_data = self.fetch_random_questions()[question_number]
        return self.provide_question(question_data)


    # def run(self):
    #     """Main execution method for the quiz game."""
    #     score = 0
    #     questions = self.fetch_random_questions(self.num_questions_to_answer)
    #
    #     for question in questions:
    #         self.question_list.append(self.provide_question(question))
    #         print(self.provide_question(question))
    #         # user_answer = int(input("Your answer (1-4): ")) - 1
    #
    #         # result, point = self.check_answer(question, user_answer)
    #         # print(result)
    #         # score += point
    #
    #     # player_name = input("Enter your name for the leaderboard: ")
    #     return self.question_list, self.num_questions_to_answer, "Enter your name for the leaderboard: ", #  self.end_message(player_name, score)

    def check_answer(self, question, user_answer):
        """Check the user's answer and return the result."""
        options = question[2:6]  # Define options within the method

        if user_answer == question[6] - 1:
            self.result_msg = "Correct!"
            self.score += 1
        else:
            correct_option_index = question[6] - 1
            self.result_msg = f"Incorrect. The correct answer was: {options[correct_option_index]}"

        return self.result_msg, self.score

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()

    def end_message(self, player_name, score):
        self.update_leaderboard(player_name, score)
        self.close()
        return f"Your final score is: {score}/{self.num_questions_to_answer}", self.display_leaderboard()




# if __name__ == "__main__":
#     game = QuizGame("my.db", "Quiz_game.sql")
#     result = game.run()
#     print(result)
#     game.close()
