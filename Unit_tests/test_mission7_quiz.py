import unittest
from unittest.mock import patch, Mock, mock_open
from Missions.quiz_SQLite.quiz import QuizGame, given_number_of_questions


class TestQuizGame(unittest.TestCase):

    def setUp(self):
        # The setup method runs before every test method.
        # Here, we're setting the test database and SQL file paths.
        self.db_file = "Missions/quiz_SQLite/my.db"
        self.sql_file = "Missions/quiz_SQLite/Quiz_game.sql"

    @patch("sqlite3.connect")
    def test_create_connection_new_table(self, mock_connect):
        """
        Test if a new table is created when the 'questions' table doesn't already exist in the database.
        We mock the sqlite3.connect method to return a mock connection object.
        """
        mock_cursor = Mock()
        # Simulate a scenario where the 'questions' table doesn't exist
        mock_cursor.fetchone.return_value = None
        mock_connect.return_value.cursor.return_value = mock_cursor

        game = QuizGame(self.db_file, self.sql_file)
        game.create_connection()

        # Ensure the correct SQL commands are executed
        mock_cursor.execute.assert_called()
        mock_cursor.executescript.assert_called()

    @patch("sqlite3.connect")
    def test_create_connection_existing_table(self, mock_connect):
        """
        Test the behavior when the 'questions' table already exists in the database.
        We want to ensure that no new table is created in this case.
        """
        mock_cursor = Mock()
        # Simulate a scenario where the 'questions' table exists
        mock_cursor.fetchone.return_value = True
        mock_connect.return_value.cursor.return_value = mock_cursor

        game = QuizGame(self.db_file, self.sql_file)
        game.create_connection()

        # Ensure that the SQL script for table creation isn't executed
        mock_cursor.execute.assert_called()
        mock_cursor.executescript.assert_not_called()

    @patch.object(QuizGame, "create_connection")
    def test_fetch_random_questions(self, mock_create_connection):
        """
        Test fetching a specific number of random questions from the database.
        The create_connection method of the QuizGame class is mocked.
        """
        mock_cursor = Mock()
        mock_create_connection.return_value = (None, mock_cursor)

        game = QuizGame(self.db_file, self.sql_file)
        game.fetch_random_questions(num_questions=5)

        # Ensure that the correct SQL query is executed
        mock_cursor.execute.assert_called_with('SELECT * FROM questions ORDER BY RANDOM() LIMIT ?', (5,))

    @patch.object(QuizGame, "create_connection")
    def test_update_leaderboard(self, mock_create_connection):
        """
        Test if a player's name and score are correctly added to the leaderboard.
        The create_connection method is mocked to return a mock connection and cursor.
        """
        mock_cursor = Mock()
        mock_conn = Mock()
        mock_create_connection.return_value = (mock_conn, mock_cursor)

        game = QuizGame(self.db_file, self.sql_file)
        game.update_leaderboard("test_player", 5)

        # Ensure that the correct SQL command is executed and the changes are committed
        mock_cursor.execute.assert_called_with('INSERT INTO leaderboard (name, score) VALUES (?, ?)', ("test_player", 5))
        mock_conn.commit.assert_called()

    @patch.object(QuizGame, "create_connection")
    def test_display_leaderboard(self, mock_create_connection):
        """
        Test the method that fetches and displays the top 10 players from the leaderboard.
        """
        mock_cursor = Mock()
        mock_create_connection.return_value = (None, mock_cursor)

        game = QuizGame(self.db_file, self.sql_file)
        game.display_leaderboard()

        # Ensure that the correct SQL query is executed
        mock_cursor.execute.assert_called_with('SELECT name, score FROM leaderboard ORDER BY score DESC LIMIT 10')

    def test_check_answer_correct(self):
        """
        Test the scenario when the user provides a correct answer.
        We don't need to mock anything for this test as it only relies on internal logic.
        """
        game = QuizGame(self.db_file, self.sql_file)
        question = ("Q1", "What is 2+2?", "1", "2", "3", "4", 4)  # The correct option is 4

        result_msg, is_correct = game.check_answer(question, 4)

        # Ensure that the method returns the correct output
        self.assertEqual(result_msg, "Correct!")
        self.assertTrue(is_correct)

    def test_check_answer_incorrect(self):
        """
        Test the scenario when the user provides an incorrect answer.
        """
        game = QuizGame(self.db_file, self.sql_file)
        question = ("Q1", "What is 2+2?", "1", "2", "3", "4", 4)  # The correct option is 4

        result_msg, is_correct = game.check_answer(question, 2)

        # Ensure that the method returns the correct output
        self.assertEqual(result_msg, "Incorrect. |The correct answer was: 4")
        self.assertFalse(is_correct)

    def test_end_message(self):
        """
        Test the final message provided to the user that includes their score and the leaderboard.
        We're mocking the display_leaderboard method to simplify this test.
        """
        game = QuizGame(self.db_file, self.sql_file)

        # Mock the display_leaderboard method to return a dummy leaderboard
        game.display_leaderboard = Mock(return_value="Mocked Leaderboard")
        score_msg, leaderboard = game.end_message(7)

        # Ensure that the method returns the expected formatted message
        self.assertEqual(score_msg, "You scored: 7/10")
        self.assertEqual(leaderboard, "Mocked Leaderboard")

    @patch.object(QuizGame, "create_connection")
    @patch("builtins.open", mock_open(read_data="CREATE TABLE questions;"))
    def test_create_connection_with_sql_file(self, mock_create_connection):
        """
        Test the create_connection method's behavior when reading an actual SQL file.
        We're mocking both the file open function and the create_connection method.
        """
        mock_cursor = Mock()
        # Simulate a scenario where the 'questions' table doesn't exist
        mock_cursor.fetchone.return_value = None
        mock_create_connection.return_value = (None, mock_cursor)

        game = QuizGame(self.db_file, self.sql_file)
        game.create_connection()

        # Ensure that the SQL script from the file is executed
        mock_cursor.executescript.assert_called_with("CREATE TABLE questions;")

    @patch.object(QuizGame, "create_connection")
    def test_fetch_default_number_of_questions(self, mock_create_connection):
        """
        Test fetching the default number of questions when no specific number is provided.
        This checks if the constant `given_number_of_questions` is properly used.
        """
        mock_cursor = Mock()
        mock_create_connection.return_value = (None, mock_cursor)

        game = QuizGame(self.db_file, self.sql_file)
        game.fetch_random_questions()

        # Ensure that the correct SQL query is executed
        mock_cursor.execute.assert_called_with('SELECT * FROM questions ORDER BY RANDOM() LIMIT ?', (given_number_of_questions,))

if __name__ == '__main__':
    unittest.main()
