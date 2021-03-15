def z_algo(string):
    L=0
    R=0
    pointer=0
    z_array=[]
    for i in range(len(string)):
        if i == 0:
            z_array.append(len(string))
        #case 1
        elif i >= R:
            count = 0
            L=i
            R=i
            while R < len(string) and string[pointer] == string[R]:
                count += 1
                pointer += 1
                R += 1 
            z_array.append(count)
            pointer=0
        #case 2
        else:
            k = i-L
            #case 2a
            if z_array[k] < R-i:
                z_array.append(z_array[k])
            #case 2b
            elif z_array[k] > R-i:
                z_array.append(R-i)
            #case 2c
            else:
                L = i
                count = z_array[k]
                while R < len(string) and string[R] == string[R-i]:
                    R+=1
                    count += 1
                z_array.append(count)
    return z_array