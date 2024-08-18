import sqlite3
import os

def get_all_found_pages(db_path):
    """Fetch all pages found in the database."""
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT url FROM tb_pages")
        pages = cursor.fetchall()
        found_pages = [page[0] for page in pages]
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
        found_pages = []
    finally:
        cursor.close()
        connection.close()

    return found_pages

def cleanup_database(db_path):
    """Delete the database file."""
    try:
        os.remove(db_path)
        print(f"Database file '{db_path}' deleted successfully.")
    except OSError as e:
        print(f"Error deleting database file: {e}")

