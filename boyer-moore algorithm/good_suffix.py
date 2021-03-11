import z_algo

def reverse_z_array(pat):
    reverse_pat = pat[::-1] 
    z_array = z_algo.z_algo(reverse_pat)
    return z_array[::-1]

def good_suffix_array(pat):
    reverse_z = reverse_z_array(pat)
    good_suffix_array = [0] * (len(pat) + 1)
    for i in range(0, len(pat) - 1):
        j = len(pat) - reverse_z[i]
        good_suffix_array[j] = i

    return good_suffix_array

def good_suffix_shift(pat, mismatch, good_suffix_array):
    if good_suffix_array[mismatch+1] > 0:
        return len(pat) - good_suffix_array[mismatch+1]

pat = "aabacabacaba"
gsa = good_suffix_array(pat)
print("shift by "+str(good_suffix_shift(pat,8,gsa)))
