import pytest
from sqlalchemy import text

from db import engine

def get_new_subject_id(connection):
    result = connection.execute(
        text("SELECT COALESCE(MAX(subject_id), 0) + 1 FROM subject")
    )
    return result.scalar()

def test_create_subject():
    with engine.begin() as connection:
        subject_id = get_new_subject_id(connection)

        try:
            connection.execute(
                text("""
                    INSERT INTO subject (subject_id, subject_title)
                    VALUES (:id, :title)
                """),
                {"id": subject_id, "title": "Test Subject"}
            )

            result = connection.execute(
                text("""
                    SELECT subject_title
                    FROM subject
                    WHERE subject_id = :id
                """),
                {"id": subject_id}
            )

            assert result.scalar() == "Test Subject"

        finally:
            connection.execute(
                text("DELETE FROM subject WHERE subject_id = :id"),
                {"id": subject_id}
            )

def test_update_subject():
    with engine.begin() as connection:
        subject_id = get_new_subject_id(connection)

        try:
            connection.execute(
                text("""
                    INSERT INTO subject (subject_id, subject_title)
                    VALUES (:id, :title)
                """),
                {"id": subject_id, "title": "Old Subject"}
            )

            connection.execute(
                text("""
                    UPDATE subject
                    SET subject_title = :title
                    WHERE subject_id = :id
                """),
                {"id": subject_id, "title": "New Subject"}
            )

            result = connection.execute(
                text("""
                    SELECT subject_title
                    FROM subject
                    WHERE subject_id = :id
                """),
                {"id": subject_id}
            )

            assert result.scalar() == "New Subject"

        finally:
            connection.execute(
                text("DELETE FROM subject WHERE subject_id = :id"),
                {"id": subject_id}
            )

def test_delete_subject():
    with engine.begin() as connection:
        subject_id = get_new_subject_id(connection)

        try:
            connection.execute(
                text("""
                    INSERT INTO subject (subject_id, subject_title)
                    VALUES (:id, :title)
                """),
                {"id": subject_id, "title": "Delete Subject"}
            )

            connection.execute(
                text("""
                    DELETE FROM subject
                    WHERE subject_id = :id
                """),
                {"id": subject_id}
            )

            result = connection.execute(
                text("""
                    SELECT COUNT(*)
                    FROM subject
                    WHERE subject_id = :id
                """),
                {"id": subject_id}
            )

            assert result.scalar() == 0

        finally:
            connection.execute(
                text("DELETE FROM subject WHERE subject_id = :id"),
                {"id": subject_id}
            )
