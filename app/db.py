import json

from datetime import ( datetime )
from flask import ( current_app, g )
from sqlalchemy import ( Boolean, DateTime, Engine, String, create_engine )
from sqlalchemy.orm import ( DeclarativeBase, Mapped, mapped_column )

class Base(DeclarativeBase):
  pass

class TodoModel(Base):
  __tablename__ = "todos"
  
  id:Mapped[int] = mapped_column(
    primary_key=True,
    nullable=False,
    autoincrement=True
  )
  description:Mapped[str] = mapped_column(
    String(255),
    nullable=False
  )
  is_completed:Mapped[bool] = mapped_column(
    Boolean,
    default=False,
    nullable=False
  )
  created_at:Mapped[datetime] = mapped_column(
    DateTime,
    default=datetime.utcnow
  )
  updated_at:Mapped[datetime] = mapped_column(
    DateTime,
    nullable=True,
  )
  
  def __repr__(self):
    _todo = {
      "id": self.id,
      "description": self.description,
      "created_at": self.__readable_date(self.created_at),
      "is_completed": self.is_completed,
      "updated_at": self.__readable_date(self.updated_at)
    }
    
    _todo_json = json.dumps(_todo)
    return str(_todo_json)
  
  def __readable_date(self, date:datetime|None):
    _date_format = "%d-%b-%Y, %I:%M %p"
    _readable_date = None
    
    if date is None:
      return _readable_date
    
    _readable_date = date.strftime(_date_format)
    return _readable_date
  
def initialize_database() -> None:
  engine = get_engine()
  Base.metadata.create_all(bind=engine)
  return

def get_engine()->Engine:
  if 'db_engine' not in g:
    engine:Engine = create_engine(
      "sqlite:///" + current_app.config["DATABASE_URL"], echo=True
    )
    g.db_engine = engine
  
  return g.db_engine
  
  
  