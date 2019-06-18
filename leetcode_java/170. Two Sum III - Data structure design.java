import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class TwoSum {
    private Map<Integer, Integer> map;
    private List<Integer> nums = new ArrayList<>();
    /** Initialize your data structure here. */
    public TwoSum() {
        map = new HashMap<>();
    }
    
    /** Add the number to an internal data structure.. */
    public void add(int number) {
        nums.add(number);
        map.put(number, nums.size() - 1);
    }
    
    /** Find if there exists any pair of numbers which sum is equal to the value. */
    public boolean find(int value) {
        for(int i = 0; i < nums.size(); i++){
            int tar = value - nums.get(i);
            if(map.containsKey(tar) && map.get(tar) > i) return true;
        }
        return false;
    }
}


// 执行用时 :171 ms, 在所有 Java 提交中击败了100.00%的用户
// 内存消耗 :48.1 MB, 在所有 Java 提交中击败了100.00%的用户

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum obj = new TwoSum();
 * obj.add(number);
 * boolean param_2 = obj.find(value);
 */