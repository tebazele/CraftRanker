from datetime import datetime
from entities.databaseSessionManager import SessionManager
from entities.video import Video

dbSession = SessionManager()


for instance in dbSession.select(Video):
    print(instance.name)
# print(dbSession)
