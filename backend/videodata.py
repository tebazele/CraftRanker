from services.videoinsert import VideoData

# from sqlalchemy import create_engine
videos = [
    {
        # 'videoId': 1,
        'youtubeId': 'https://youtu.be/OI5BA60PhQI',
        'name': 'Intro to Etsy Essentials',
        'series': 'Etsy Essentials',
        'module': 1
    },
    {
        # 'videoId': 2,
        'youtubeId': 'https://youtu.be/lYK3m0RsdH8',
        'name': 'Your Shop Name & Tagline',
        'series': 'Etsy Essentials',
        'module': 1
    },

]

videoModule = VideoData()


def addVideos():
    for v in videos:
        # print(v["videoId"])
        # vidId = v["videoId"]
        ytId = v["youtubeId"]
        n = v["name"]
        s = v["series"]
        m = v["module"]
        videoModule.addVideoObjects(ytId, n, s, m)


addVideos()


# def removeVideo():
#     videoModule.removeVideoObject(2)


# removeVideo()
