# tests/conftest.py

import pytest
import sqlite3
import os

@pytest.fixture(scope="function")
def setup_database():
    """Fixture to set up a test database."""
    db_path = "test_db_websites.db"
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Create a simple tb_pages table for testing
    cursor.execute('''
        CREATE TABLE tb_pages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE NOT NULL,
            dt_discovered TEXT,
            sitemaps TEXT,
            referring_pages TEXT,
            successful_page_fetch BOOLEAN,
            status_code INTEGER,
            dt_last_crawl TEXT,
            robots_index BOOLEAN DEFAULT NULL,
            robots_follow BOOLEAN DEFAULT NULL
        )
    ''')

    connection.commit()
    yield db_path  # Provide the test database path to the tests

    # Cleanup after tests
    cursor.close()
    connection.close()
    os.remove(db_path)
