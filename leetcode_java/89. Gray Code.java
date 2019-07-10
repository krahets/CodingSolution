class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> res = new ArrayList<Integer>() {{ add(0); }};
        for (int i = 0; i < n; i++) {
            int head = 1 << i;
            for (int j = res.size() - 1; j >= 0; j--)
                res.add(head + res.get(j));
        }
        return res;
    }
}