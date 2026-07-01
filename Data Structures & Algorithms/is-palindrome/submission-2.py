class Solution:
    def isPalindrome(self, s: str) -> bool:
        sn = ""
        for i in s:
            if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                sn += i.lower()
        if sn == sn[::-1]:
            print(sn,sn[::-1])
            return True
        return False