from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
engine = create_engine('sqlite:///instance/db.sqlite', echo=True)
meta = MetaData()

videos = Table('videos', meta,
               Column('videoId', Integer, primary_key=True),
               Column('youTubeId', String(255)),
               Column('name', String(255)),
               Column('thumbnail', String(4000)))

meta.create_all(engine)
