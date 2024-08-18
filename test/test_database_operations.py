# tests/test_database_operations.py

import sqlite3
import pytest

def test_insert_and_fetch(setup_database):
    db_path = setup_database
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Insert a test URL
    test_url = "https://example.com"
    cursor.execute('''
        INSERT INTO tb_pages (url, dt_discovered, sitemaps, referring_pages, successful_page_fetch, status_code)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (test_url, "20240817000000", None, None, False, 200))

    connection.commit()

    # Fetch the inserted URL
    cursor.execute("SELECT url FROM tb_pages WHERE url = ?", (test_url,))
    result = cursor.fetchone()
    assert result[0] == test_url

    cursor.close()
    connection.close()
