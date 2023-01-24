import sys
import math
sys.setrecursionlimit(10**6)
def solution(numbers):
    answer = []
    
    def makeBinaryNumber(n):
        bin_num = ''
        while n >=2 :
            bin_num = str(n%2) + bin_num
            n = n//2
        bin_num = str(n) + bin_num
        return bin_num
    
    def calcLengthOfPohwaTree(length_bin_num):
        
        return 2 ** (math.floor(math.log(length_bin_num) / math.log(2) + 1 ))-1
        
        
        
    def checkBinaryTree(start, end, bin_num): 
        # print('start', start, 'end', end)
        if start == end  : 
            return bin_num[start] 
        
        mid = (start+end)//2
        left = checkBinaryTree(start, mid-1, bin_num) 
        if bin_num[mid] == '0' and left == '1' or not left : 
            return False
        right = checkBinaryTree(mid+1, end, bin_num)
        if bin_num[mid] == '0' and right == '1' or not right : 
            return False
        if left == '0' and right == '0' and bin_num[mid] == '0': return '0'
        return '1'
            
    for n in numbers :
        bin_num = makeBinaryNumber(n)
        len_pohwa = calcLengthOfPohwaTree(len(bin_num))
        
        bin_num  = '0' * (len_pohwa - len(bin_num)) + bin_num
        
        # print('n', n, 'bin_num', bin_num)
        # print('len_pohwa', len_pohwa)
        if checkBinaryTree(0, len_pohwa-1, bin_num) : 
            answer.append(1)
        else :
            answer.append(0)
    
    print('answer', answer)
    return answer