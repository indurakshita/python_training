from bot.utils.send import send
from pydantic import BaseModel as base, EmailStr
from datetime import datetime, date
from sqlalchemy import (create_engine, Column, Integer,
                            String, DateTime, text)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite://")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Company(Base):
    __tablename__ = "appl"
    id = Column(Integer, primary_key=True)
    hr = Column(String)
    email = Column(String)
    company = Column(String)
    position = Column(String)
    date = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
         return f"{self.hr} - (Company => {self.company}) for (Position => {self.position}) on {self.date}"
         
Base.metadata.create_all(engine)

class CompData(base):
    hr: str
    to: EmailStr
    position: str
    company: str
    date: date = datetime.strftime(datetime.utcnow(), "%d-%b-%Y")
    
class Search:
    def __init__(self):
        self.obj = session.query(Company)
        self.history = session.query(Company).all()
        
    def search(self, obj, item):
        filt = {"hr": Company.hr, "date": Company.date,
               "company": Company.company,
               "position": Company.position
          }
        self.sess = self.obj.filter(filt[obj] == item)
        return self
    
    
        
def main():
    print("\tEmail Automata")
    comp = CompData(
            hr= input("Enter HR Name: ").title(),
            to = input("Enter recepient: "),
            position= input('Enter Position: ').title(),
            company= input("Enter Company: ").title()
          )
    
          
    if send(comp):
        comp = Company(
                        hr=comp.hr,
                        email=comp.to,
                        company=comp.company,
                        position=comp.position
                    )
        session.add(comp)
        session.commit()
               
if __name__ == "__main__":
    main()