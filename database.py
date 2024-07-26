import sqlite3
import sys

""" Error constants """

OPERATION_SUCCESS = 1
INTEGRITY_ERROR = 0
USER_NOT_FOUND_ERROR = -1
UNKNOWN_ERROR = -2

def create_db()-> None:
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY
        )               
    ''')
    conn.commit()
    conn.close()
    
def add_user(username)-> bool:
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username) VALUES (?)', (username,))
        conn.commit()
        return OPERATION_SUCCESS
    except sqlite3.IntegrityError:
        return INTEGRITY_ERROR
    except Exception as e:
        print("!{e}!", file=sys.stderr)
        return UNKNOWN_ERROR
    finally:
        conn.close()
            
def get_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

def update_user(old_username, new_username)-> None:   
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('UPDATE users SET username = ? WHERE username = ?', (new_username, old_username))
        if cursor.rowcount == 0:
            return USER_NOT_FOUND_ERROR
        else:
            conn.commit()
            return OPERATION_SUCCESS
    except sqlite3.IntegrityError:
        return INTEGRITY_ERROR
    except:
        print("!{e}!", file=sys.stderr)
        return UNKNOWN_ERROR
    finally:
        conn.close()
    
def delete_user(username)-> None:
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE username = ?', (username,))
        if cursor.rowcount == 0:
            return USER_NOT_FOUND_ERROR
        else:
            conn.commit()
            return OPERATION_SUCCESS