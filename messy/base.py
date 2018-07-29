from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


engine = create_engine("mysql+pymysql://root:@db/messy?charset=utf8mb4")
Session = sessionmaker(bind=engine)

Base = declarative_base()


@contextmanager
def scoped_session():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

