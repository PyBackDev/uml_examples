"""Пример взаимодействия классов - реализация."""

from abc import ABC, abstractmethod


class Connection(ABC):
    """Интерфейс взаимодействия с базой данных."""

    @abstractmethod
    def connect(self):
        """Подключение к базе данных."""

    @abstractmethod
    def disconnect(self):
        """Отключение от базы данных."""


class DatabaseConnection(Connection):
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

if __name__ == "__main__":
    postgres = PostgreSQLDatabase(
        connection_url="postgres://localhost:5432/mydb",
        username="admin",
        password="admin123",
    )
    postgres.connect()
    postgres.disconnect()
