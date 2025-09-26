import sqlite3
from pathlib import Path

class Database:
    def __init__(self):
        self.db_file = 'music_downloader.db'
        self.create_tables()
    
    def create_tables(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        # Tabla de usuarios
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            download_path TEXT
        )
        ''')
        
        # Tabla de descargas
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS downloads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            video_id TEXT NOT NULL,
            title TEXT NOT NULL,
            download_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_user(self, username, password):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                         (username, password))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()
    
    def verify_user(self, username, password):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM users WHERE username = ? AND password = ?',
                      (username, password))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    
    def update_download_path(self, user_id, path):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET download_path = ? WHERE id = ?',
                      (path, user_id))
        conn.commit()
        conn.close()
    
    def get_download_path(self, user_id):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('SELECT download_path FROM users WHERE id = ?', (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    
    def add_download(self, user_id, video_id, title):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO downloads (user_id, video_id, title)
        VALUES (?, ?, ?)
        ''', (user_id, video_id, title))
        conn.commit()
        conn.close()
    
    def get_user_downloads(self, user_id):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''
        SELECT title, download_date FROM downloads
        WHERE user_id = ?
        ORDER BY download_date DESC
        ''', (user_id,))
        results = cursor.fetchall()
        conn.close()
        return results