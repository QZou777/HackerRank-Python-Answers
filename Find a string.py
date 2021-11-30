# HackerRank find a string
def count_substring(string, sub_string):
    sublength = len(sub_string)
    count = 0
    for i in range(len(string)):
        if string[i:i+sublength] == sub_string:
            count+=1
    return count
