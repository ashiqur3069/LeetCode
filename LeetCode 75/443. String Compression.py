class Solution(object):
    def compress(self, chars):
        ans = 0
        i = 0
        while i < len(chars):
            count = 0
            letter = chars[i]
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1
            chars[ans] = letter
            ans += 1
            if count > 1:
                for val in str(count):
                    chars[ans] = val
                    ans += 1
        return ans
