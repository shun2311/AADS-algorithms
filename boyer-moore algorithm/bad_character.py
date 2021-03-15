
#preprocess to get R(x) values
def generate_bad_char_matrix(pat):
    bad_char_table = []
    size = 26
    for i in range(size):
        bad_char_table.append([-1]*len(pat))

    for i in range(len(pat)-1,-1,-1):
        index = ord(pat[i])-97
        bad_char_table[index][i]=i

        if i!=len(pat)-1:
            right = i + 1
            while right<len(pat) and bad_char_table[index][right] == -1:
                bad_char_table[index][right] = i
                right+=1

    return bad_char_table  
    