from .config import SQL_URI, SQL_DEBUG
from greenlet import getcurrent
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine(
    SQL_URI,
    echo=SQL_DEBUG,
)
session = scoped_session(
    sessionmaker(autocommit=False, autoflush=True, bind=None),
    scopefunc=getcurrent,
)
session.configure(bind=engine)


class Transaction:
    def __enter__(self):
        self.session = session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()

        self.session.close()
