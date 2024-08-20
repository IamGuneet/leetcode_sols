class Solution {
    public int stoneGameII(int[] piles) {
        int n = piles.length;
        int[] suffixSum = new int[n];
        suffixSum[n - 1] = piles[n - 1];

        // Calculate the suffix sums (from the end of the array)
        for (int i = n - 2; i >= 0; i--) {
            suffixSum[i] = piles[i] + suffixSum[i + 1];
        }

        // DP table to store the maximum stones the current player can get
        int[][] dp = new int[n][n + 1];

        // Solve the game using dynamic programming
        return helper(0, 1, suffixSum, dp);
    }

    private int helper(int i, int M, int[] suffixSum, int[][] dp) {
        int n = suffixSum.length;

        // Base case: If we are at the end, return 0 (no stones left)
        if (i == n) return 0;

        // If the number of remaining piles is less than or equal to 2*M, take all
        if (2 * M >= n - i) return suffixSum[i];

        // If the answer is already calculated, return it
        if (dp[i][M] > 0) return dp[i][M];

        // Otherwise, calculate the optimal answer
        int minOpponentStones = Integer.MAX_VALUE;
        for (int x = 1; x <= 2 * M; x++) {
            minOpponentStones = Math.min(minOpponentStones, helper(i + x, Math.max(M, x), suffixSum, dp));
        }

        // The best Alice can do is the remaining stones minus the best Bob can do
        dp[i][M] = suffixSum[i] - minOpponentStones;
        return dp[i][M];
    }
}

