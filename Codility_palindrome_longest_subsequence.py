def longest(A):
    n = len(A)
    d = [[0]*n for _ in range(n)]
    for i in range(n-1,-1,-1):
        d[i][i] = 1
        for j in range(i+1, n):
            if A[i] == A[j]:
                d[i][j] = 2 + d[i+1][j-1]
            else:
                d[i][j] = max(d[i+1][j], d[i][j-1])
    return d[0][-1]

def solution(A):
    n = len(A)
    return n - longest(A)

# -----------------------------
# Python program to find Minimum number of 
# deletions to make a string palindrome

    def longestPalindromeSubseq(self, s: str) -> int:
        """
        Find the length of the longest palindromic subsequence in string s.
        A subsequence is a sequence that can be derived from another sequence 
        by deleting some or no elements without changing the order of the remaining elements.
      
        Args:
            s: Input string
          
        Returns:
            Length of the longest palindromic subsequence
        """
        n = len(s)
      
        # dp[i][j] represents the length of longest palindromic subsequence 
        # in substring s[i:j+1] (from index i to j inclusive)
        dp = [[0] * n for _ in range(n)]
      
        # Base case: single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1
      
        # Fill the dp table by increasing substring length
        # j represents the ending index of substring
        for j in range(1, n):
            # i represents the starting index of substring
            # Iterate from j-1 down to 0 to ensure we have computed smaller subproblems first
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    # If characters at both ends match, add 2 to the result of inner substring
                    # For substring of length 2, dp[i+1][j-1] would be 0 (empty substring)
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # If characters don't match, take maximum of:
                    # 1. Excluding character at index i: dp[i+1][j]
                    # 2. Excluding character at index j: dp[i][j-1]
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
      
        # Return the result for the entire string (from index 0 to n-1)
        return dp[0][n - 1]
# ------------------------------
# Function to find the length of the lps
def longestPalinSubseq(s):
    n = len(s)

    # Create two vectors: one for the current state (dp)
    # and one for the previous state (dpPrev)
    curr = [0] * n
    prev = [0] * n

    # Loop through the string in reverse (starting from the end)
    for i in range(n - 1, -1, -1):

        # Initialize the current state of dp
        curr[i] = 1

        # Loop through the characters ahead of i
        for j in range(i + 1, n):

            # If the characters at i and j are the same
            if s[i] == s[j]:

                # Add 2 to the length of the palindrome between them
                curr[j] = prev[j - 1] + 2
            else:

                # Take the maximum between excluding either i or j
                curr[j] = max(prev[j], curr[j - 1])

        # Update previous to the current state of dp
        prev = curr[:]

    return curr[n - 1]

# Function to calculate the minimum
# Element required to delete for
# Making string palindrome
def minDeletions(s):
    n = len(s)

    # Find the LPS 
    lps = longestPalinSubseq(s)

    return n - lps

A = "aebcbda"
print(solution(A))