# matilde/main.py

import sys
import os

# Append the parent directory of 'audits' to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from audits import PresenceOfRobotsTxtAudit #, SitemapInRobotsTxtAudit

def run_audits(website):
    audits = [
        PresenceOfRobotsTxtAudit(),
    ]

    results = {}
    for audit in audits:
        audit.run(website)
        results[audit.name] = {
            "passed": audit.get_result(),
            "issues": audit.get_issues(),
        }
    
    return results

if __name__ == "__main__":
    # Example website data
    website_data = {
        "robots.txt": True  # Or False, depending on whether robots.txt is present
    }
    
    results = run_audits(website_data)
    for audit_name, result in results.items():
        print(f"Audit: {audit_name}")
        print(f"Passed: {result['passed']}")
        if not result['passed']:
            print("Issues:")
            for issue in result['issues']:
                print(f" - {issue}")
