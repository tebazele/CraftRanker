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

    def removeAllVideos(self):
        num_of_rows_deleted = self.dbSession.query(Video).delete()
        # FIXME also remove auto sequenced Ids somehow so IDs start again at 1 when the video data is reinserted
        # print(num_of_rows_deleted)
        self.dbSession.commit()

    def getVideos(self):
        return self.dbSession.query(Video).all()
