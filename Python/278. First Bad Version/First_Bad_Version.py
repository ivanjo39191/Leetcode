#概念
#使用二進制搜索法
#如果搜尋結果小於中間項則從左側搜尋
#反之大於中間項則由右側搜尋

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def find_bad_version(a,b):
            if(a>=b):
                return a
            mid = (a+b)/2
            if isBadVersion(mid):
                return find_bad_version(a,mid)
            else:
                return find_bad_version(mid+1,b)
        return find_bad_version(1,n)
                
