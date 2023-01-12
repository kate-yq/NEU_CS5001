# Quan, Yuan
# Nov 7, 2022

# this file contains the helper function needed

# the function check the time difference of 2 videos, in minutes
# and determine whether they are in similar length
# parameter: the length (str: "00:00:00") of 2 videos
# return: true if the 2 videos are in similar length
def len_percent(len1:str, len2:str):
    len_1 = len1.split(":")
    len_2 = len2.split(":")
    len_1_min = int(len_1[0])*60 + int(len_1[1]) + int(len_1[2])/60
    len_2_min = int(len_2[0])*60 + int(len_2[1]) + int(len_2[2])/60
    percentage = min(len_1_min,len_2_min)/max(len_1_min, len_2_min)
    return percentage >= 0.6