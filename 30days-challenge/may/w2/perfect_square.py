class Solution:
    def isPerfectSquare(self, n):
        guess = 1
        seen = {guess}
        while guess * guess != n:
            guess = (guess + (n // guess)) // 2
            if guess in seen:
                return False
            seen.add(guess)
        return True


if __name__ == '__main__':
    print(Solution().isPerfectSquare(16))
