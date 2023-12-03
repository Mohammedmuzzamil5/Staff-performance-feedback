import sqlite3

class PerformanceDB:
    def __init__(self):
        self.conn = sqlite3.connect('performance_data.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS performance_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                staff_name TEXT NOT NULL,
                achievement TEXT,
                goal TEXT,
                feedback TEXT
            )
        ''')
        self.conn.commit()

    def add_performance_entry(self, staff_name, achievement, goal, feedback):
        self.cursor.execute('''
            INSERT INTO performance_entries (staff_name, achievement, goal, feedback)
            VALUES (?, ?, ?, ?)
        ''', (staff_name, achievement, goal, feedback))
        self.conn.commit()

    def get_all_performance_entries(self):
        self.cursor.execute('SELECT * FROM performance_entries')
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()
