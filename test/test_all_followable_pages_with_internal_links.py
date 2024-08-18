# tests/test_all_followable_pages_with_internal_links.py

import sqlite3
from audits.internal_links.all_followable_pages_with_internal_links import AllFollowablePagesWithInternalLinksAudit

def test_all_followable_pages_with_internal_links(setup_database):
    db_path = setup_database

    # Insert sample data into the database
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO tb_pages (url, dt_discovered, sitemaps, referring_pages, successful_page_fetch, status_code, robots_follow)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', ("https://example.com/page1", "20240817000000", None, None, True, 200, 1))
    cursor.execute('''
        INSERT INTO tb_pages (url, dt_discovered, sitemaps, referring_pages, successful_page_fetch, status_code, robots_follow)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', ("https://example.com/page2", "20240817000000", None, None, True, 200, 1))

    connection.commit()

    audit = AllFollowablePagesWithInternalLinksAudit(db_path)
    audit.run("https://example.com")

    # Corrected assertion
    assert audit.get_result() == False  # Should fail because there are no internal links
    assert "The following followable pages do not have any internal followable links:" in audit.get_issues()[0]

    cursor.close()
    connection.close()
