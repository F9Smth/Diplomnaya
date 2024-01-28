import sqlite3

"""
Database class for interacting with a SQLite database.

Provides methods for executing SQL queries, committing transactions, 
creating/accessing tables, and collecting query statistics.

Designed to encapsulate all database access in one class.
"""


class Database:

    def __init__(self, database_file):
        """
        Initialize the Database object with the given database file.

        Args:
            database_file (str): Path to the database file. 
        """
        self.db = sqlite3.connect(database_file)

    def execute_sql(self, query):
       """
       Execute an SQL query on the database.

       Args:
           query (str): The SQL query to execute.

       Returns:
           sqlite3.Cursor: A cursor for the query results.
       """
       c = self.db.cursor()
       c.execute(query)
       self.db.commit()
       return c

    def close(self):
        """
        Close the connection to the database.
        """
        self.db.close()

    def create_statistics_table(self):
        """
        Create the statistics table in the database 
        if it does not already exist.
        """
        query = """
            CREATE TABLE IF NOT EXISTS statistics (
              query_id INTEGER PRIMARY KEY,
              query TEXT NOT NULL,
              execution_time INTEGER NOT NULL,
              memory_usage INTEGER NOT NULL,
              disk_usage INTEGER NOT NULL,
              num_rows INTEGER NOT NULL,
              num_bytes INTEGER NOT NULL
            );
        """
        self.execute_sql(query)

    def insert_statistics(
        self, query, execution_time, memory_usage, disk_usage, num_rows, num_bytes
    ):
        """
        Insert a new statistics record into the statistics table.

        Args:
            query (str): The SQL query that was executed
            execution_time (int): Execution time of the query
            memory_usage (int): Memory usage during execution
            disk_usage (int): Disk usage during execution 
            num_rows (int): Number of rows returned
            num_bytes (int): Size of the results in bytes
        """
        query_id = self.db.last_insert_rowid()
        self.execute_sql(
            "INSERT INTO statistics (query_id, query, execution_time, memory_usage, disk_usage, num_rows, num_bytes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                query_id,
                query,
                execution_time,
                memory_usage,
                disk_usage,
                num_rows,
                num_bytes,
            ),
        )

    def get_statistics(self):
        """
        Get all statistics records from the database.

        Returns:
            list: List of tuples containing the statistics records.
        """
        query = "SELECT * FROM statistics" 
        c = self.execute_sql(query)
        return c.fetchall()

    def delete_statistics(self):
        """
        Delete all statistics records from the database.
        """
        query = "DELETE FROM statistics"
        self.execute_sql(query)

    def __del__(self):
        """
        Close the database connection when object is destroyed.
        """
        self.close()