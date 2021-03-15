import scan
import bad_character
import good_suffix
import match_prefix

def good_suffix_shift(pat, mismatch, good_suffix_array, match_prefix_array):
    if good_suffix_array[mismatch+1] > 0:
        return len(pat) - good_suffix_array[mismatch+1]
    else:
        return len(pat) - match_prefix_array[mismatch+1]

def boyer_moore_algo(string, pat):
    start = 0
    end = len(pat)-1
    all_match = []
    bc_array = bad_character.generate_bad_char_matrix(pat)
    gs_array = good_suffix.good_suffix_array(pat)
    mp_array = match_prefix.match_prefix(pat)

    while end<len(string):
        mismatch = scan.right_to_left(start, end, string, pat)
        char_index = ord(string[mismatch])-97
        if mismatch == start - 1:
            shift_to = len(pat) - mp_array[1]
            all_match.append(mismatch)
        else:
            bc_shift = max(1, mismatch - bc_array[char_index][mismatch])
            gs_shift = good_suffix_shift(pat, mismatch, gs_array, mp_array)
            shift_to = max(bc_shift, gs_shift)
        start += shift_to
        end += shift_to

string =  "aabcbababsaskc"
pattern = "cababab"
boyer_moore_algo(string, pattern)
