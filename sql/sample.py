from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database connection and create the engine
engine = create_engine("sqlite:///applications.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)


Base.metadata.create_all(engine)


def create_user(username, email):
    new_user = User(username=username, email=email)
    session.add(new_user)
    session.commit()
    print("User created successfully")


create_user(username="john_doe", email="john@example.com")


def update_user_email(username, new_email):
    user = session.query(User).filter_by(username=username).first()
    
    if user:
        user.email = new_email
        session.commit()
        print("User updated successfully")
    else:
        print("User not found")

# Example usage
update_user_email(username="john_doe", new_email="new_email@example.com")
