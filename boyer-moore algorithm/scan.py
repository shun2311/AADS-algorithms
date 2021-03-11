#basic right to left scan that returns the index of the
#mismatch letter or returns the start index if there is no mismatch
def right_to_left(start,end,string,pat):
    for i in range(end, start-1, -1):
        if string[i]!=pat[i-start]:
            return i-start
    return 0
