import z_algo

def match_prefix(pat):
    z_array = z_algo.z_algo(pat)
    mp_array = [0] * (len(pat) + 1)
    for i in range(len(pat)-1, -1, -1):
        if z_array[i] + i == len(pat):
            mp_array[i] = z_array[i]
        else:
            mp_array[i] = mp_array[i+1]
    return mp_array

#pat = "acababacaba"
#print(match_prefix(pat))
#print(len(pat))