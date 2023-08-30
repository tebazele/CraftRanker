# entities/video.py
# Author: Jeanne Allen (https://github.com/tebazele)
# Defines the Video Information data model
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
import json


class Video(SQLAlchemy().Model):
    __tablename__ = 'Videos'
    __table_args__ = {'sqlite_autoincrement': True}

    videoId = Column(Integer, primary_key=True)
    youtubeId = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    series = Column(String(255), nullable=False)
    module = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Video(youtubeId='%s', name='%s', series='%s', module='%d')" % (self.youtubeId, self.name, self.series, self.module)

    def get_as_dict(self):
        # NOTE this is a python debugger
        # import ipdb
        # ipdb.set_trace()
        return {
            'videoId': self.videoId,
            'youtubeId': self.youtubeId,
            'name': self.name,
            'series': self.series,
            'module': self.module,
        }
