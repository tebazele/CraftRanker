from entities.databaseSessionManager import SessionManager
from entities.video import Video
from models.defaultMethodResult import DefaultMethodResult
# from sqlalchemy import query
import json


class VideoData():
    # connect to database
    dbSession = SessionManager().session

    # find the correct table -- model to Video model

    def addVideoObjects(self, youtubeId, name, series, module):
        newVideo = Video(
            youtubeId=youtubeId, name=name, series=series, module=module)

        self.dbSession.add(newVideo)
        self.dbSession.commit()
        print('new video created')

    def removeVideoObject(self, videoId):
        video1 = self.dbSession.query(Video).get(videoId)
        self.dbSession.delete(video1)
        self.dbSession.flush()
        self.dbSession.commit()

    def getVideos(self):
        return self.dbSession.query(Video).all()
