# Quan, Yuan
# Nov 7, 2022

from User import User
from Video import Video
import heapq
from heapq import heappop

# this program construct all user information and video information
# then takes the input users form a given file
# write the top 3 recommended videos to the user into the same file

# global dictionary to mapping userID with users, and videoID with videos
USERMAP = {}     # userID : User
VIDEOMAP = {}    # videoID : Video
AMOUNT = 3       # the desired amount for recommendation


# ----------------******** Initialization ********----------------

# this function takes in the file name of the csv file storing all users information
# and create all users then add then to USERMAP
def user_factory(filename: str):
    # csv: ID, sex, region, born_year, remark
    with open(filename, 'r') as user_lib:
        header = user_lib.readline()
        users = user_lib.readlines()
    for user in users:
        info = user.strip().split(",")
        if info[3] == "":
            new_user = User(info[0], info[1], info[2])
            USERMAP[info[0]] = new_user
        else:
            new_user = User(info[0], info[1], info[2], int(info[3]))
            USERMAP[info[0]] = new_user


# this function takes in the file name of the csv file storing all videos information
# and create all videos then add then to VIDEOMAP
def video_factory(filename: str):
    # csv: videoID, userID, name, category, language, length, play volumn
    with open(filename, 'r') as user_lib:
        header = user_lib.readline()
        videos = user_lib.readlines()
    for video in videos:
        info = video.strip().split(",")
        user = USERMAP[info[1]]
        video = user.upload(info[2], info[0], info[3], info[4], info[5])
        video.played(int(info[6]))
        VIDEOMAP[info[0]] = video


# this function in the file name of the csv file storing the watching actions of users
# and update the corresponding watching history of the user
def build_watching_history(filename):
    # userID, videoID, videoID ...
    with open(filename, 'r') as watching_lib:
        watchings = watching_lib.readlines()
    for watching in watchings:
        action = watching.strip().split(",")
        user = USERMAP[action[0]]
        for i in range(1, len(action)):
            user.watch(VIDEOMAP[action[i]])

# ----------------******** helper function ********----------------

# this function takes in a list of video and then rank all videos in libarary based on similarity score
# the similarity score of a video will be the highest of the video compared to the list of videos
# then return the rank as a list / priority queue
# threshold: similarity>=4
def rank_by_video_similarity(video):
    max_heap = []
    for other in VIDEOMAP.values():
        if video.similarity(other) >= 4:
            max_heap.append((video.similarity(other), other))
    heapq.heapify(max_heap)
    return max_heap


# this function takes in a user and then rank all users in libarary based on similarity score
# then return the rank as a list / priority queue
# threshold: similarity>=4
def rank_by_user_similarity(user):
    max_heap = []
    for other in USERMAP.values():
        if user.similarity(other) >= 4:
            max_heap.append((user.similarity(other), other))
    heapq.heapify(max_heap)
    return max_heap


# this function rank all videos by their playing volume
# return the rank as a list / priority queue
def rank_by_play_volume():
    max_heap = []
    for video in VIDEOMAP.values():
        max_heap.append(video)
    heapq.heapify(max_heap)
    return max_heap


# this function takes in a user and a list of recommended videos
# return the information as follows:
# "the most recent videos watched by userxxx are name1, name2, name3, name4, name5"
# "The top AMOUNT recommended for this user are name1, name2, name3,.."
def outcome(user, recommedVideos: list):
    message = ""
    if len(user.watch_history) == 0:
        message = f"{user.id} has not watch any videos yet. \n"
    elif len(user.watch_history) == 1:
        message = f"the most recent video watched by {user.id} is: \n{user.watch_history[0].name}, \n"
    else:
        message = f"the most recent videos watched by {user.id} are: \n"
        for video in user.watch_history:
            message += f"{video.name}, \n"
    message += f"\nthe top {AMOUNT} videos recommended for this user are: \n"
    for i in range(len(recommedVideos)-1):
        message += f"{recommedVideos[i].name}, \n"
    message += f"{recommedVideos[-1].name}."
    return message


# ----------------******** Recommending function ********----------------

# this function takes in a list of videos, with at most length of 5
# and return AMOUNT videos in the VIDEOMAP which is most similar to the watching history
# parameter: a list of video, with possible length between 1 and 5
# return: a list of AMOUNT recommended videoIDs
def recommend_on_videolist(watching_history: list):
    result = []
    for video in watching_history[::-1]:
        by_video = rank_by_video_similarity(video)
        while (len(result) < AMOUNT) & (len(by_video)>0):
            video = heappop(by_video)[1]
            if (video not in watching_history) & (video not in result):
                result.append(video)
        if len(result) == AMOUNT:
            return result
    return result


# this function takes in a designated user, and a list
# and return AMOUNT videos by visiting the watching history of its most similar users
# if there is no more similar users, as the rest user's similarity<4
# recommend by videos' playing volumn
# parameter: user: User and a list of Videos
# return: a list of AMOUNT videoIDs
def recommend_on_user(user, result):
    by_usr = rank_by_user_similarity(user)
    while len(by_usr) > 0:
        simuser = heappop(by_usr)[1]
        if (simuser != user) & (len(simuser.watch_history) > 0):
            for video in simuser.watch_history[::-1]:
                if video not in result:
                    result.append(video)
        if len(result) >= AMOUNT:
            return result[:AMOUNT]

    by_volume = rank_by_play_volume()
    while len(result) < AMOUNT:
        video = heappop(by_volume)
        if video not in result:
            result.append(video)
    return result


# ----------------******** Overall logic function ********----------------

# this function organizes all previous functions logically
# parameter: a user ID(str)
# if the user has wartching history, then recommend by its watching history
# if not enough, then recommend by usr similarity then playing volume
# return: print the recommending message

def recommend(usrID):
    if usrID not in USERMAP.keys():
        raise ValueError(f"Do not exist user {usrID}")
    user = USERMAP[usrID]
    recom_list = []
    if len(user.watch_history) > 0:
        recom_list = recommend_on_videolist(user.watch_history)
    if len(recom_list) < AMOUNT:
        recom_list = recommend_on_user(user, recom_list)
    print(outcome(user, recom_list))


def main():
    # read in all info and build the system
    user_factory("user_lib.csv")
    video_factory("video_lib.csv")
    build_watching_history("watching_lib.csv")

    # ask for a usr to recommend
    usr = input(
        "please input the user ID to which you want to recommend videos: (usr_1~25)")
    recommend(usr)


if __name__ == "__main__":
    main()
