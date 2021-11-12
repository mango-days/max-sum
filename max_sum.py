array1 = [2,3,7,10,12]
array2 = [1,5,7,8,9]

def sort (array1, array2, ans):
    index1=0
    index2=0
    while (index1<len(array1) and index2<len(array2)):
        if array1[index1]==array2[index2]: return (sort (array2[index2+1:], array1[index1+1:], ans+array1[index1]))
        else:   
            ans+=(array1[index1])
            index1+=1
            index2+=1
        if (index1==len(array1) or index2==len(array1)): return(ans)
        
print (max (max(sort(array1, array2, 0), sort(array2, array1, 0)), max(sum(array1), sum(array2))) )