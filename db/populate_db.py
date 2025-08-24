import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DB_URL = os.getenv("DB_URL")
if not DB_URL:
    raise ValueError("DB_URL environment variable not set")
engine = create_engine(DB_URL)

SQL = """
DROP TABLE IF EXISTS messages;

CREATE TABLE messages (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    text VARCHAR(255) NOT NULL,
    username VARCHAR(100) NOT NULL,
    added TIMESTAMP NOT NULL
);

INSERT INTO messages (text, username, added) 
VALUES
    ('Hello, World!', 'Alice', '2025-08-01 12:52:21'),
    ('Flask is great!', 'Bob', '2025-08-02 13:45:08'),
    ('I love coding!', 'Charlie', '2025-08-03 00:30:00');
"""


def main():
    with engine.connect() as conn:
        conn.execute(text(SQL))
        conn.commit()
    print("Database populated with initial data.")


if __name__ == "__main__":
    main()
