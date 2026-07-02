from backend.db.base import Base
from backend.db.session import engine
from backend.models.user import User


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")