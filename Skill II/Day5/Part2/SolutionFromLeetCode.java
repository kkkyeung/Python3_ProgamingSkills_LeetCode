class Solution {
    public List<Integer> addToArrayForm(int[] A, int K) {
        int N = A.length;
        int cur = K;
        List<Integer> ans = new ArrayList();

        int i = N;
        while (--i >= 0 || cur > 0) {
            if (i >= 0)
                cur += A[i];
            ans.add(cur % 10);
            cur /= 10;
        }

        Collections.reverse(ans);
        return ans;
    }
}

// Runtime: 4 ms, faster than 89.25% of Java online submissions for Add to Array-Form of Integer.
// Memory Usage: 43.6 MB, less than 96.33% of Java online submissions for Add to Array-Form of Integer.