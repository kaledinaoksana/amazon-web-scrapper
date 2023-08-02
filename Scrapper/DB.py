
from settings import SQL

from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager

class DBwork:
    
    Base = declarative_base()

    class AmazonBook(Base):
        __tablename__ = 'AmazonBooks'

        ID = Column(Integer, primary_key=True, autoincrement=True)
        Title = Column(String)
        Price = Column(String)
        Score = Column(String)

    # CONNECTION
    def conn_db():
        connection_string = 'DRIVER={'+SQL.DRIVER+'};SERVER='+SQL.SERVER+';DATABASE='+SQL.DB+';UID='+SQL.USER+';PWD='+SQL.PSW+';'
        engine = create_engine(f"mssql+pyodbc:///?odbc_connect={connection_string}")
        return engine

    # CREATE TABLE
    def create_table(engine):
        DBwork.Base.metadata.create_all(engine)
        return

    # CREATE SESSION
    def create_session(engine):
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    # ADD
    def add_object(session,obj):
        session.add(obj)
        session.commit()
        return
    
    # DELETE
    def delete_object(obj):
        session.delete(obj)
        session.commit()
        return
    
    # close session
    @contextmanager
    def session_scope(engine):
        """Provide a transactional scope around a series of operations."""
        session = DBwork.create_session(engine)
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

