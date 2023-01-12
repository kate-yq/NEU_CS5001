# Quan, Yuan
# Nov 7, 2022

from Video import Video

# User class defines all users
# with fields of id(str), sex(str), origin(str), born year(int)
# everything other than id is optional when initializing

# has watch function to record the 5 latest watched videos, could be empty
# has upload function to record all upload history, could be empty


class User():

    # when initialize the user, only the user id(str) is required
    # sex(str), origin(str),and born year(int) are optional
    # self generate 2 empty list to store latest 5 watched videos and all uploaded videos
    def __init__(self, id: str, sex="", origin="", born_year=0):
        self.id = id
        self.sex = sex
        self.origin = origin
        self.born_year = born_year
        self.watch_history = []
        self.upload_history = []


    # when user watch a video, take the video as input, and append it to the watch_history list
    # if the list exceed 5 videos, remove form beggining to reduce to 5
    # so the list only contains latest 5 watching record
    # at the same time, the video's playing volume will increment by 1

    def watch(self, video: Video):
        video.played()
        self.watch_history.append(video)
        if len(self.watch_history) > 5:
            self.watch_history.pop(0)


    # when user upload a video, he creates the name, id, category, language, and length;
    # create the Video, and append it to the upload_history list
    # return the video if useful in later stage
    def upload(self, name, id, category, language, length):
        video = Video(self.id, name, id, category, language, length)
        self.upload_history.append(video)
        return video


    # this function calculate the score (out of 10) of the similarity to the input user
    # same sex - 2 marks; same origin - 3 marks; 
    # age diff >= 15 - 0 marks, 12~15 - 1 mark, 8~12 - 2 marks,
    #  5~8 - 3 marks, 2~5 - 4 marks, 0~2 - 5 marks
    # parameter: the designated user
    # return the score

    def similarity(self, user):
        score = 0
        if self.sex!="" and user.sex!="":
            if self.sex == user.sex:
                score += 2
        if self.origin!="" and user.origin!="":
            if self.origin == user.origin:
                score += 3
        if self.born_year!=0 and user.born_year!=0:
            if abs(self.born_year-user.born_year) < 2:
                score+=5
            elif abs(self.born_year-user.born_year) < 5:
                score+=4
            elif abs(self.born_year-user.born_year) < 8:
                score+=3
            elif abs(self.born_year-user.born_year) < 12:
                score+=2
            elif abs(self.born_year-user.born_year) < 15:
                score+=1
        return score


    # Override the less-than operator __lt__ to make Video class work with max heap
    def __lt__(self, other):
        return self.born_year > other.born_year