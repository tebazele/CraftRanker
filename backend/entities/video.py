# entities/video.py
# Author: Jeanne Allen (https://github.com/tebazele)
# Defines the Video Information data model
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean


class Video(SQLAlchemy().Model):
    __tablename__ = 'Videos'
    __table_args__ = {'sqlite_autoincrement': True}

    videoId = Column(Integer, primary_key=True)
    youtubeId = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    series = Column(String(255), nullable=False)
    module = Column(Integer, nullable=False)
