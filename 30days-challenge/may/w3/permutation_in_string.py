from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_counts = Counter(s1)
        for idx in range(len(s2)):
            c = s2[idx]
            if c in s1:
                counts = Counter(s2[idx:idx+len(s1)])
                if counts == s1_counts:
                    return True
        return False


if __name__ == '__main__':
    print(Solution().checkInclusion('ab', 'eidbaooo'))
    print(Solution().checkInclusion('ab', 'eidboaoo'))
