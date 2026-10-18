"""This modules creates a DatabaseManager Class"""
import sqlite3
import hashlib
import typing


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

        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS users('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'username TEXT NOT NULL UNIQUE,'
            'email TEXT NOT NULL UNIQUE,'
            'password TEXT NOT NULL,'
            'school TEXT NOT NULL)'
        )
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS friends('
            'user_id INTEGER,'
            'friend_id INTEGER,'
            'FOREIGN KEY (user_id) REFERENCES users(id),'
            'FOREIGN KEY (friend_id) REFERENCES users(id))'
        )
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS schedules('
            'user_id INTEGER,'
            'schedule TEXT NOT NULL,'
            'FOREIGN KEY (user_id) REFERENCES users(id))'
        )

        self.connection.commit()


    def user_exists(self, username: str) -> bool:
        """This method checks for user in table users

        :param username: User to check in table
        :type username: str
        :returns: Returns `True` if user exists and `False` if not.
        :rtype: bool
        """

        o = self.cur.execute(
            'SELECT * FROM users WHERE username = ?', (username,))

        return len(o.fetchall()) != 0

    def auth_user(self, username: str, password: str) -> bool:
        """Authenticates user by his username and password

        :param username: User in database
        :type username: str
        :param password: Password that hashed by `hashlib.sha256()` function
        :type password: str
        :returns: Returns `True` if login success and `False` if not.
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
        :param password: Password that hashed by `hashlib.sha256()` function
        :type password: str
        """

        self.cur.execute('INSERT INTO users(username, email, school, password)\
            VALUES(?, ?, ?, ?)',
            (username, email, school, password)
        )
        self.connection.commit()

    def get_username_by_id(self, uid: int | str) -> str:
        """Gets username by id if user exists

        :param uid: Unique id of user from `users` table
        :type uid: int | str
        :returns: Returns got username if user exists or empty string if not
        :rtype: str
        """

        o = self.cur.execute('SELECT username FROM users WHERE id = ?', (uid,))
        try:
            return str(list(o.fetchone())[0])
        except TypeError:
            return ''

    def get_username_by_email(self, email: str) -> str:
        """Gets users name by email if user exists

        :param email: Unique email of user from `users` table
        :type email: str
        :returns: Returns got username if user exists or empty string if not
        :rtype: str
        """

        o = self.cur.execute('SELECT username FROM users WHERE email = ?', (email,))
        try:
            return str(list(o.fetchone())[0])
        except TypeError:
            return ''

    def get_email_by_username(self, username: str) -> str:
        """Gets users email by username if user exists

        :param username: Users name from `users` table
        :type username: str
        :returns: Returns got email if user exists or empty string if not
        :rtype: str
        """

        o = self.cur.execute('SELECT email FROM users WHERE username = ?', (username,))
        try:
            return str(list(o.fetchone())[0])
        except TypeError:
            return ''

    def get_email_by_id(self, uid: int | str) -> str:
        """Gets users email by id if user exists

        :param uid: Users id from `users` table
        :type uid: int | str
        :returns: Returns got email if user exists or empty string if not
        :rtype: str
        """

        o = self.cur.execute('SELECT email FROM users WHERE id = ?', (uid,))
        try:
            return str(list(o.fetchone())[0])
        except TypeError:
            return ''

    def get_id_by_username(self, username: str) -> str:
        """Gets users id by username if user exists

        :param username: Users name from `users` table
        :type username: str
        :returns: Returns got id if user exists or empty string if not
        :rtype: str
        """

        o = self.cur.execute('SELECT id FROM users WHERE username = ?', (username,))
        try:
            return str(list(o.fetchone())[0])
        except TypeError:
            return ''

    def get_id_by_email(self, email: str) -> str:
        """Gets users id by email if user exists

        :param email: Users email from `users` table
        :type email: str
        :returns: Returns got id if user exists or empty string if not
        :rtype: str
        """

        o = self.cur.execute('SELECT id FROM users WHERE email = ?', (email,))
        try:
            return str(list(o.fetchone())[0])
        except TypeError:
            return ''

    def get_user_friends(self, user_id: int | str) -> list[str]:
        """Gets user friends ids

        :param user_id: User unique id
        :type user_id: int | str
        :returns: List of users friends ids
        :rtype: list[str]
        """

        o = self.cur.execute('SELECT friend_id FROM friends WHERE user_id = ?', (user_id,))
        try:
            return [str(i[0]) for i in o.fetchall()]
        except TypeError:
            return ['']

    def add_friends(self, user_id_1: str | int, user_id_2: str | int) -> None:
        """Add friends

        :param user_id_1: Id of first user
        :type user_id_1: str | int
        :param user_id_2: Id of second user
        :type user_id_2: str | int
        """

        if not self.check_friends(user_id_1, user_id_2):
            self.cur.execute(
                'INSERT INTO friends(user_id, friend_id) VALUES(?, ?), (?, ?)',
                (user_id_1, user_id_2, user_id_2, user_id_1)
            )
            self.connection.commit()

    def check_friends(self, user_id_1: str | int, user_id_2: str | int) -> bool:
        """Checks if users are friends
        
        :param user_id_1: Id of first user
        :type user_id_1: str | int
        :param user_id_2: Id of second user
        :type user_id_2: str | int
        :returns: Returns `True` if users are friends and `False` if not
        :rtype: bool
        """

        uf_1 = [i[0] for i in self.cur.execute(
            'SELECT friend_id FROM friends WHERE user_id = ?',
            (user_id_1,)
        ).fetchall()]
        uf_2 = [i[0] for i in self.cur.execute(
            'SELECT friend_id FROM friends WHERE user_id = ?',
            (user_id_2,)
        ).fetchall()]

        for f1 in uf_1:
            for f2 in uf_2:
                if f1 == user_id_2 or f2 == user_id_1:
                    return True

        return False

    def get_users(self) -> list[typing.Any]:
        """Gets the users table
        
        :returns: Returns got table as list
        :rtype: list[Any]
        """
        return self.cur.execute('SELECT * FROM users').fetchall()

    def close_connection(self) -> None:
        """Closes database connection"""
        self.connection.close()


if __name__  == "__main__":
    dm = DatabaseManager()
    if not dm.user_exists('Salmon228'):
        dm.register_user(
            'Salmon228',
            'e',
            'Школа №2070 ОП Энергия',
            hashlib.sha256('password'.encode()).hexdigest()
        )
    if not dm.user_exists('Oleg'):
        dm.register_user(
            'Oleg',
            'e',
            'Школа №2070 ОП Энергия',
            hashlib.sha256('qwerty'.encode()).hexdigest()
        )

    print(dm.get_users())

    dm.close_connection()
