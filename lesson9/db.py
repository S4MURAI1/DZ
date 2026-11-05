from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg2://postgres:128mb108RAP@localhost:5432/QA"

engine = create_engine(DATABASE_URL)

def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Подключение успешно:", result.scalar())

if __name__ == "__main__":
    test_connection()