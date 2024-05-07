import sqlite3
import hashlib


class DBclass:

    def __init__(self):
        self.users_table = 'users.sql'
        self.conn_users = None
        self.curr_users = None

        self._connect_to_DB()

    def _connect_to_DB(self):
        """

        :return: connects to database if exists. if not, creates the necessary tables
        """
        # creating users table
        self.conn_users = sqlite3.connect(self.users_table)
        self.curr_users = self.conn_users.cursor()
        sql = "CREATE TABLE IF NOT EXISTS users (NAME VARCHAR(50), SCORE INT)"
        self.curr_users.execute(sql)
        self.conn_users.commit()

    def user_exists(self, username: str):
        """

        :param username: gets a username
        :return: returns true if user exists in database
        """

        sql = "SELECT * FROM users WHERE NAME = ?"
        self.curr_users.execute(sql, (username,))
        return self.curr_users.fetchone()

    def add_user(self, username: str):
        """

        :param username: user's name
        :return: if user is not in database, adds the user to the database and sets its score to 0
        """
        toRet = False
        if not self.user_exists(username):
            sql = "INSERT INTO users VALUES (?,?)"
            self.curr_users.execute(sql,
                                      (username, 0))
            self.conn_users.commit()
            toRet = True

        return toRet

    # -----------------------------------------
    # Getters and setters for the users table
    # -----------------------------------------

    def set_user_name(self, old_name: str, new_name: str):
        """
        Set a new name for a given user.

        :param old_name: The old name of the user.
        :param new_name: The new name to set.
        """
        if self.user_exists(old_name):
            sql = "UPDATE users SET NAME = ? WHERE NAME = ?"
            self.curr_users.execute(sql, (new_name, old_name))
            self.conn_users.commit()

    def get_score(self, name: str):
        """

        :param name: The name of the user.
        :return: user's score
        """
        if self.user_exists(name):
            sql = "SELECT SCORE FROM users WHERE NAME = ?"
            self.curr_users.execute(sql, (name,))
            return self.curr_users.fetchone()[0]

    def add_score(self, name: str, score_to_add: int):
        """

        :param name: The name of the user.
        :param score_to_add: amount of score to add to user's score.
        """
        if self.user_exists(name):
            score_to_add += self.get_score(name)
            sql = "UPDATE users SET SCORE = ? WHERE NAME = ?"
            self.curr_users.execute(sql, (score_to_add, name))
            self.conn_users.commit()

if __name__ == '__main__':
    myDB = DBclass()
    myDB.add_user("lior")
    myDB.add_score("lior", 50)

