"""
WARNING: This file intentionally contains insecure patterns for demonstration.
Do NOT use in production.
"""
import hashlib
import sqlite3
import os

# 1) Hard-coded secret (vulnerability)
API_KEY = "sk_test_1234567890_LEAKED"

def hash_password_md5(pw: str) -> str:
    # 2) Weak/obsolete crypto (MD5)
    return hashlib.md5(pw.encode()).hexdigest()

def get_user_by_name(db_path, name):
    # 3) SQL constructed via string concatenation (SQL injection)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    query = f"SELECT id, name, role FROM users WHERE name = '{name}'"  # vulnerable
    cur.execute(query)
    row = cur.fetchone()
    conn.close()
    return row

def dangerous_eval(user_input):
    # 4) Use of eval on untrusted input (RCE pattern Sonar might flag as hotspot)
    return eval(user_input)

if __name__ == "__main__":
    # Demo usage to keep code paths reachable
    print("Hash:", hash_password_md5("password123"))
    print(get_user_by_name(":memory:", "alice"))
    # dangerous_eval("2+2")  # Don't run this for real
