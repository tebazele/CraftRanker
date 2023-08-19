# entities/video.py
# Author: Jeanne Allen (https://github.com/tebazele)
# Defines the Video Information data model
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean


class Video(SQLAlchemy().Model):
    __tablename__ = 'Videos'

    videoId = Column(Integer, primary_key=True)
    youtubeId = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    thumbnail = Column(String(4000), nullable=False)
