import sqlite3

def init_db():
    conn = sqlite3.connect("competition.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            classroom TEXT,
            player TEXT,
            score INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_score(classroom, player, score):
    conn = sqlite3.connect("competition.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO scores (classroom, player, score) VALUES (?, ?, ?)",
        (classroom, player, score)
    )

    conn.commit()
    conn.close()


def get_scores(classroom):
    conn = sqlite3.connect("competition.db")
    c = conn.cursor()

    c.execute(
        "SELECT player, score FROM scores WHERE classroom=? ORDER BY score DESC",
        (classroom,)
    )

    data = c.fetchall()
    conn.close()
    return data
