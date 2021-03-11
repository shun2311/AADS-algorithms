
#preprocess to get R(x) values
def generate_bad_char_table(pat):
    bad_char_table = []

    for i in range(26):
        bad_char_table.append([None]*len(pat))

    for i in range(len(pat)-1,-1,-1):
        index = ord(pat[i])-97
        bad_char_table[index][i]=i

        if i!=len(pat)-1:
            right = i + 1
            while right<len(pat) and bad_char_table[index][right] is None:
                bad_char_table[index][right] = i
                right+=1

    return bad_char_table  
    