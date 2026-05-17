# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

# Example 1:

# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
# Example 2:

# Input: s = "0000"
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
             # 00000
        #valid ip has 3 dots
        #each segment is not over length 3
        #each segment has to begin with 1 or 2 cannot be 0
        #each segment not over 255
        res = []

        subset = []

        def backtrack(index, dots, path):
            if index == len(s) and dots == 4:
                res.append(path[:-1])
                return
            
            if index >= len(s) or dots > 3 :
                return
            
            for i in range(index, min(index+3, len(s))):
                segment = s[index: i + 1] #this is the section
                if len(segment) > 1 and segment[0] == '0': #leading zero not valid
                    break
                
                if int(segment) <= 255: #valid
                    backtrack(i +1, dots +1 , path+ segment + ".")
        backtrack(0,0,"")
        return res

