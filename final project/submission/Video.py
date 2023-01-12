# Quan, Yuan
# Nov 7, 2022

import utils

# this class defines all videos
# every video is created by a user, so it is initialized by user.upload
# the inputs by uploader are user.self(User), name(str), id(str) category(str), language(str) and length(str"00:00:00")
# play volume will be automatically calculate when watched by some users

class Video():
    def __init__(self, userID:str, name: str, id:str, category:str, language:str, length:str):
        self.uploaderID = userID
        self.name = name
        self.id = id
        self.category = category
        self.language = language
        self.length = length
        self.play_volume = 0


    # this function changes the play volumn of the video
    # each time video is played, the volume will increse by 1
    # for easy test construction, if input any int, then the volumew will increse by corresponding int

    def played(self, volume = 1):
        self.play_volume += volume


    # this function calculate the score (out of 10) of the similarity to the input video
    # same category - 5 marks; created by the same user - 3 marks; 
    # same language - 1 mark; shorter length is 60% or more of longer length - 1 mark
    # parameter: the designated video
    # return the score

    def similarity(self,video):
        score = 0
        if self.category == video.category:
            score += 5
        if self.uploaderID == video.uploaderID:
            score += 3
        if self.language == video.language:
            score += 1
        if utils.len_percent(self.length, video.length):
            score += 1
        return score

    # Override the less-than operator __lt__ to make Video class work with max heap
    # compared by play_volume
    def __lt__(self, other):
        return self.play_volume > other.play_volume
