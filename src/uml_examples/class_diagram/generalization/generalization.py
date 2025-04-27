"""Пример взаимодействия классов - наследование."""


class DatabaseConnection:
    """Класс взаимодействия с базой данных."""

    def __init__(self, connection_url: str, username: str, password: str):
        self.connection_url = connection_url
        self.username = username
        self.password = password

    def connect(self):
        """Подключение к базе данных."""
        print(
            f"Connecting to BD at {self.connection_url} as {self.username}"
        )

    def disconnect(self):
        """Отключение от базы данных."""
        print(f"Disconnecting from BD at {self.connection_url}")



class PostgreSQLDatabase(DatabaseConnection):
    """Класс для работы с базой данных PostgreSQL."""



class MySQLDatabase(DatabaseConnection):
    """Класс для работы с базой данных MySQL."""


if __name__ == "__main__":
    # PostgreSQL
    postgres = PostgreSQLDatabase(
        connection_url="postgres://localhost:5432/mydb",
        username="admin",
        password="admin123",
    )
    postgres.connect()
    postgres.disconnect()

    # MySQL
    mysql = MySQLDatabase(
        connection_url="mysql://localhost:3306/mydb",
        username="root",
        password="mysql123",
    )
    mysql.connect()
    mysql.disconnect()
