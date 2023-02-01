
import math
import sys
sys.setrecursionlimit(10**6)
def solution(numbers):
    answer = []
    
    # def digitTo2(n):
    #     output = ''
    #     while n>0:
    #         output = str(n%2) + output
    #         n = n //2
    #     return output
    def digitTo2(n):
        bin_num = ''
        while n >=2 :
            bin_num = str(n%2) + bin_num
            n = n//2
        bin_num = str(n) + bin_num
        return bin_num
    
    def BinToPohwabin(bin_num):
        pohwa_length = 2 ** (math.ceil(math.log(len(bin_num)) / math.log(2) )) - 1
        return '0' * (pohwa_length - len(bin_num)) + bin_num
    
    def calcLengthOfPohwaTree(bin_num):
        len_pohwa = 2 ** (math.floor(math.log(len(bin_num)) / math.log(2) + 1 ))-1
        bin_num  = '0' * (len_pohwa - len(bin_num)) + bin_num
        return bin_num
    def binarySearch(start, end, pohwa_num):
        if start >= end : 
            return pohwa_num[start]
        
        mid = (start+end) // 2
        left = binarySearch(start, mid-1, pohwa_num)
        right = binarySearch(mid+1, end, pohwa_num)
        
        if left is False or right is False :
            return False
        if pohwa_num[mid] == '0' and (left == '1' or right == '1'): 
            return False
        if left =='0' and right =='0' and pohwa_num[mid] == '0' :
            return '0'
        return '1'
    
    def checkBinaryTree(start, end, bin_num): 
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
        
        
    
    for num in numbers:
        bin_num = digitTo2(num)
        pohwa_num = calcLengthOfPohwaTree(bin_num)
        if binarySearch(0, len(pohwa_num)-1, pohwa_num) : 
            answer.append(1)
        else :
            answer.append(0)
    return answer