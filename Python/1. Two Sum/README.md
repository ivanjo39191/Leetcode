# 1. Two Sum

[Question](#question)  
[中文題目](#question_zh_hant)  
[解法](#answer1)  
[思路](#think1)  
[Big-O](#bigo)  
[代碼](#code)  


<a name="question"></a>
## Question
Given an array of integers, return indices of the two numbers such that they add up to a specific target.  
You may assume that each input would have exactly one solution, and you may not use the same element twice.  
Example:  

        Given nums = [2, 7, 11, 15], target = 9,
        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].


<a name="question_zh_hant"></a>
## 題目  
給定一個整數數組 nums 和一個目標值 target，請你在該數組中找出和為目標值的那 兩個 整數，並返回他們的數組下標。  
你可以假設每種輸入只會對應一個答案。但是，你不能重複利用這個數組中同樣的元素。  
範例:  

        Given nums = [2, 7, 11, 15], target = 9,
        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].

<a name="answer1"></a>
## 解法1  
這裡會使用到以下兩個方法:  
list.count()  
list.index()  
count() 方法用於統計某個元素在列表中出現的次數。  
count()方法語法：  
        list.count(obj)
index() 函數用於從列表中找出某個值第一個匹配項的索引位置。  
index()方法語法：  
        list . index ( x [, start [, end ]])  
<a name="think1"></a>
### 思路  
####解題關鍵:  
主要是想找到num2 = target - num1，是否也在list中，那麼就需要運用以下兩個方法：  
num2 in nums，返回True  
nums.index(num2)，查找num2的索引  
####解題詳解:  
首先計算 nums 的長度並存入變數  
宣告變數 j 為 -1，若沒找到 num2 可用是否大於0進行判斷  
使用for迴圈進行遍歷  
使用if判斷 num2 in nums  ，對 list 使用 in 的時間複雜度為 O(n)  
如果num2=num1,且nums中只出現了一次，說明找到是 num1 本身  
將此情況使用if判斷，再使用continue跳過  
如果不是找到 num1 本身，則將該值存入 j  
index(x,i+1)是從 num1 的序列後找 num2，避免重複查找  
判斷 j 是否大於0，大於0代表有找到 num2，將 i，j 值返回  
若無找到 num2 則返回空值  



<a name="bigo"></a>
### Big-O  
 時間複雜度 O(n^2)  
 空間複雜度 O(N)  


<a name="code"></a>
### 代碼  

        class Solution:
            def twoSum(self, nums: List[int], target: int) -> List[int]:
                lens = len(nums)
                j = -1
                for i in range(lens):
                    if (target-nums[i]) in nums:
                        if (nums.count(target-nums[i]) == 1) & (target-nums[i] == nums[i]):
                            continue
                        else:
                            j = nums.index(target-nums[i], i+1)
                            break
                if j > 0:
                    return [i,j]
                else:
                    return []
