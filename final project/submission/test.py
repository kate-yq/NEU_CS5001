# Quan, Yuan
# Nov 7, 2022

from User import User
from Video import Video
import utils
import recommendation


def test_utils():
    def test_utils_len_percent():
        assert utils.len_percent("01:00:01", "00:36:01") == True
        assert utils.len_percent("00:10:00", "00:05:59") == False
    test_utils_len_percent()


def test_User():
    user1 = User("001", "F", "US", 1995)
    user2 = User("002", "M", "China", 2000)
    user3 = User("003")
    video1 = user3.upload("check out my puppy", "01", "pet", "english", "00:10:05")
    video2 = user2.upload("vlog-travel in SF", "02", "travel", "english", "00:07:05")
    video3 = user3.upload("love song", "03", "music", "french", "00:04:13")
    video4 = user2.upload("vlog-cook with lamb", "04", "cook", "chinese", "00:20:45")
    video5 = user3.upload("rap", "05", "music", "french", "00:01:29")
    video6 = user3.upload("one day in SJ", "06", "travel", "english", "00:07:05")

    def test_user_upload():
        assert len(user1.upload_history) == 0
        assert len(user2.upload_history) == 2 
        assert user2.upload_history.__contains__(video2)
        assert len(user3.upload_history) == 4
        assert user3.upload_history.__contains__(video1)
        assert not user3.upload_history.__contains__(video2)
    test_user_upload()

    def test_user_watch():
        user1.watch(video1)
        user1.watch(video2)
        user1.watch(video3)
        assert len(user1.watch_history)==3
        user1.watch(video4)
        user1.watch(video5)
        assert len(user1.watch_history)==5
        user1.watch(video6)
        assert len(user1.watch_history)==5
        assert user1.watch_history.__contains__(video6)
        assert not user1.watch_history.__contains__(video1)
    test_user_watch()

    def test_user_similarity():
        assert user1.similarity(user1) == 10
        assert user1.similarity(user2) == 3
        assert user1.similarity(user3) == 0
        assert user2.similarity(user3) == 0
    test_user_similarity()


def test_Video():
    user = User("000")
    video1 = Video("001", "check out my puppy", "01", "pet", "english", "00:10:05")
    video2 = Video("001", "vlog-travel in SF", "02", "travel", "english", "00:07:05")
    video3 = Video("002", "love song", "03", "music", "french", "00:14:13")
    video4 = Video("001", "rap", "04", "music", "french", "00:05:29")

    def test_video_played():
        video1.played(1000)
        assert video1.play_volume == 1000
        user.watch(video1)
        assert video1.play_volume == 1001
    test_video_played()

    def test_video_similarity():
        assert video1.similarity(video1) == 10
        assert video1.similarity(video2) == 5
        assert video1.similarity(video3) == 1
        assert video3.similarity(video4) == 6
    test_video_similarity()


def test_recommendation():
    def test_outcome():
        user = User("test_user")
        video1 = Video("001", "check out my puppy", "01", "pet", "english", "00:10:05")
        video2 = Video("001", "vlog-travel in SF", "02", "travel", "english", "00:07:05")
        video3 = Video("002", "love song", "03", "music", "french", "00:14:13")
        recommedVideos = [video1, video2, video3]
        exp = f"test_user has not watch any videos yet. \n\nthe top 3 videos recommended for this user are: \ncheck out my puppy, \nvlog-travel in SF, \nlove song."
        assert recommendation.outcome(user, recommedVideos) == exp
    test_outcome()

    def test_user_factory():
        recommendation.user_factory("user_lib.csv")
        assert len(recommendation.USERMAP) == 25
    test_user_factory()

    def test_video_factory():
        recommendation.video_factory("video_lib.csv")
        assert len(recommendation.VIDEOMAP) == 23
    test_video_factory()

    def test_build_watching_history():
        recommendation.build_watching_history("watching_lib.csv")
        assert len(recommendation.USERMAP["usr_1"].watch_history) == 5
    test_build_watching_history()


def main():
    test_utils()
    test_User()
    test_Video()
    test_recommendation()
    print("All test passed!")

if __name__=="__main__":
    main()