# Quan Yuan
# Nov 17 lab

FILENAME = "classroom_agreement_phrases.txt"

# this function reads in all phrases in FILENAME and genrate a list of phrases
# return: a list of phrases
def read_phrases():
    file = open(FILENAME, 'r')
    lines = file.readlines()
    phrases = []
    for line in lines:
        if line.strip()!="":
            phrases.append(line.strip())
    return phrases


# this function takes in a list of phrases, and sort the words in it by frequency
# parameter: a list of phrases
# return: a sorted list of words from high-frequency to low-frequency
def sort_by_words(phrases):
    all_words = []
    for phrase in phrases:
        words = phrase.lower().split()
        for word in words:
            all_words.append(word)
    return freq_sort(all_words)


# this function takes in a list of phrases, and sort the phrases by frequency
# parameter: a list of phrases
# return: a sorted list of phrases from high-frequency to low-frequency
def sort_by_phrases(phrases):
    all_phrases = []
    for phrase in phrases:
        words = phrase.lower().split()
        correct_phrase = ""
        for word in words:
            correct_phrase = correct_phrase + word + " "
        correct_phrase = correct_phrase[:-1]
        all_phrases.append(correct_phrase)
    return freq_sort(all_phrases)


# this is a helper funtion, it takes in a list of str and sort by frequency
# parameter: a list of str
# return: a list of str from high-frequency to low frequency
def freq_sort(str_list):
    freq_map = {}
    for element in str_list:
        if freq_map.get(element)==None:
            freq_map[element] = 1
        else:
            freq_map[element] = freq_map.get(element)+1
    ans = []
    for i in sorted(freq_map.items(), key=lambda freq: freq[1], reverse=True):
        ans.append(i[0])
    return ans


# this function takes in a list and print in readable format
# parameter: a list of str
# print: use "," to separate elements
def print_list(str_list):
    for i in range(len(str_list)-1):
        print(str_list[i], end=", ")
    print(str_list[-1])


def main():
    phrases = read_phrases()
    print("sort by words' frequencies:")
    print_list(sort_by_words(phrases))
    print("sort by phrases' frequencies:")
    print_list(sort_by_phrases(phrases))


if __name__=="__main__":
    main()