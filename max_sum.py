array1 = [2,3,7,10,12]
array2 = [1,5,7,8,9]

def max_sum(array1, array2):
    ans= 0
    index1=0
    index2=0
    sum1=0
    sum2=0
    while (index1<len(array1) and index2<len(array2)):
        if array1[index1]==array2[index2]: 
            ans+= max(sum1,sum2) + array1[index1]
            sum1=0
            sum2=0
            index1+=1
            index2+=1
        elif array1[index1]<array2[index2]:
            sum1+=(array1[index1])
            index1+=1
        else : 
            sum2+=(array2[index2])
            index2+=1
    while index1 < len(array1):
        sum1 += array1[index1]
        index1 += 1
    while index2 < len(array2):
        sum2 += array2[index2]
        index2 += 1
    ans += max(sum1, sum2)
    return ans
    
print(max_sum(array1, array2))
