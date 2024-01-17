from entities.databaseSessionManager import SessionManager
from entities.user import User
import bcrypt


class UserData():
    dbSession = SessionManager().session

    def addUserObjects(self, username, createdAt, fullName, password):
        print(password)
        username = username.lower()
        # encrypt passwords
        encryptedPassword = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt())

        newUser = User(username=username, createdAt=createdAt,
                       fullName=fullName, password=encryptedPassword)

        self.dbSession.add(newUser)
        self.dbSession.commit()
        print('new user created')
