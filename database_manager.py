"""This modules creates a DatabaseManager Class"""
import sqlite3
import hashlib


class DatabaseManager:
    """This class provides a database manager that can get and add entries to selected database."""
    def __init__(self, database: str="school_map.db"):
        """This class provides a database manager that can get and add entries to selected database.
        
        :param database: Path to a database file. Database should contain at least 3 tables:\
            users, friends and schedules.
        :type database: str 
        """
        self.connection = sqlite3.connect(database)
        self.cur = self.connection.cursor()

    def user_exists(self, username: str) -> bool:
        """This method checks for user in table users
        
        :param username: User to check in table
        :type username: str
        :returns: Returns True if user exists and False if not.
        :rtype: bool
        """

        o = self.cur.execute(
            'SELECT * FROM users WHERE username = ?', (username,))

        return len(o.fetchall()) != 0

    def auth_user(self, username: str, password: str) -> bool:
        """Authenticates user by his username and password
        
        :param username: User in database
        :type username: str
        :param password: Password that hashed by sha256 function
        :type password: str
        :returns: Returns True if login success and False if not.
        :rtype: bool
        """

        o = self.cur.execute(
            'SELECT * FROM users WHERE username = ? and password = ?',
            (username, password)
        )

        return len(o.fetchall()) != 0

    def register_user(self, username: str, email: str, school: str, password: str) -> None:
        """Authenticates user by his username and password
                
        :param username: User in database
        :type username: str
        :param email: User email
        :type email: str
        :param school: User school
        :type school: str
        :param password: Password that hashed by sha256 function
        :type password: str
        """

        self.cur.execute('INSERT INTO users(username, email, school, password)\
            VALUES(?, ?, ?, ?)',
            (username, email, school, password)
        )
        self.connection.commit()

    def close_connection(self) -> None:
        """Closes database connection"""
        self.connection.close()


if __name__  == "__main__":
    dm = DatabaseManager()
    if not dm.user_exists('Salmon228'):
        dm.register_user(
            'Salmon228',
            'salmon228@inbox.ru',
            'Школа №2070 ОП Энергия',
            hashlib.sha256('password'.encode()).hexdigest()
        )
    else:
        print(dm.auth_user('Error', hashlib.sha256('password'.encode()).hexdigest()))

    dm.close_connection()
