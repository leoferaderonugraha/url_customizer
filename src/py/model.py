from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils.models import Timestamp
from sqlalchemy import Column, Text


Base = declarative_base(cls=Timestamp)


class CustomizedURL(Base):
    __tablename__ = 'customized_url'

    # Can be multiple same URL with different shortened version
    original_url: str = Column(Text, nullable=False)
    custom_url: str = Column(Text, primary_key=True)
