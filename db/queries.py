import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DB_URL = os.getenv("DB_URL")
if not DB_URL:
    raise ValueError("DB_URL environment variable not set")
engine = create_engine(DB_URL)


def get_messages():
    with engine.connect() as conn:
        return conn.execute(text("SELECT * FROM messages")).mappings().all()


def get_message_by_id(message_id):
    with engine.connect() as conn:
        return (
            conn.execute(
                text("""
                     SELECT * FROM messages 
                     WHERE id = :id
                     """),
                {"id": message_id},
            )
            .mappings()
            .first()
        )


def add_message(message_text, username, added):
    with engine.begin() as conn:
        conn.execute(
            text(
                """
                INSERT INTO messages (text, username, added)
                VALUES (:text, :username, :added)
                """
            ),
            {"text": message_text, "username": username, "added": added},
        )


def delete_message_from_db(message_id):
    with engine.begin() as conn:
        conn.execute(
            text(
                """
                DELETE FROM messages
                WHERE id = :id
                """
            ),
            {"id": message_id},
        )
