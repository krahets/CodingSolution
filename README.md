# CodingSolution
This repository includes coding solutions of Leetcode and 剑指offer using Python and Java.

## LeetCode
The solutions of leetcode are updated daily, while using [Python](./leetcode_python) and [Java](./leetcode_java).

---

### 1.two-sum
> 
>> 标签：数组，哈希表Hash

---

- 建立HashMap，遍历数组`nums`，`key`存储`nums[i]`，`value`存储`i`；
- 遍历过程中，判断HashMap里是否有`target - nums[i]`的`key`值，若有直接返回两个数字index。

```python []
class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            if str(target - nums[i]) in dic:
                return [dic[str(target - nums[i])], i]
            dic[str(nums[i])] = i
```
```java []
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length;i++) {
            int x = nums[i];
            if(map.containsKey(target - x)){
                return new int[] { map.get(target-x), i};
            }
            map.put(x, i);
        }
        return null;
    }
}
```

---

### 2. Add Two Numbers
> 
>> 标签：链表

---

- 模拟整个做加法的过程，`carry`记录进位，需要注意两点：
  - 由于两链表长度可能不同，因此在做加法时，要将超出短链表的值填`0`再计算；
  - 当`l1`，`l2`都遍历完后，还需要判断是否有进位，如果有需要再添一位`1`。

```python []
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(0)
        res = head
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            tmp = num1 + num2 + carry
            carry = 1 if tmp >= 10 else 0
            head.next = ListNode(tmp % 10)
            head = head.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry: head.next = ListNode(1)
        return res.next
```
```java []
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode res = head;
        int carry = 0;
        while(l1 != null || l2!= null){
            int num1 = l1 != null ? l1.val : 0;
            int num2 = l2 != null ? l2.val : 0;
            int tmp = num1 + num2 + carry;
            carry = tmp / 10;
            head.next = new ListNode(tmp % 10);
            head = head.next;
            if(l1 != null) l1 = l1.next;
            if(l2 != null) l2 = l2.next;
        }
        if(carry == 1) head.next = new ListNode(1);
        return res.next;
    }
}
```

---

### 3. Longest Substring Without Repeating Characters
> 
>> 标签：双指针，哈希表Hash，字符串

---

- 设定左右双指针`l`和`r`，遍历字符串；
- 哈希表存储某字符`s[i]`最新在字符串中出现的位置`index + 1`，`key, value`对应`s[i], i`；
- 左指针在遍历过程中：
  - 若`s[i]`不在HashMap中，则跳过；
  - 否则，`l`指针设定为`l`和`dic[s[r]]`的最大值，即修改之后，保证新字符串中没有重复字符。
  - 每次更新长度最大值`res`。

```python []
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        l, res = 0, 0
        for r in range(len(s)):
            if s[r] in dic:
                l = max(dic[s[r]], l)
            dic[s[r]] = r + 1
            res = max(res, r - l + 1)
        return res
```
```java []
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 0;
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0, j = 0; j < s.length(); j++) {
            if (map.containsKey(s.charAt(j))) {
                i = Math.max(map.get(s.charAt(j)), i);
            }
            map.put(s.charAt(j), j + 1);
            res = Math.max(res, j - i + 1);
        }
        return res;
    }
}
```

---

### 5. Longest Palindromic Substring
> 
>> 标签：字符串，双指针

---

- 遍历`s`，以每个`char`以及两个`char`中点为中心，计算以此点为中心的最长回文串；
  - 例如： 字符串`abcba` 共有5（字母） + 4（两字母间） = 9个中心点；
  - 因此，长度为`N`的string共有`2N-1`个中心。
- 我们的目标就是统计以这`2N-1`个点为中心的最长回文串`s1,s2,..,s2N-1`，并从中挑出全局最长回文串。
- 保留最大长度回文串`index`，记为`left`和`right`；
- 完成遍历后返回以`left`和`right`为边界的substring。


```python []
class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        for i in range(len(s)):
            odd = self.mid_expand(s, i, i)
            even = self.mid_expand(s, i, i+1)
            m = max(odd, even)
            if m > right - left:
                left = i - (m - 1) // 2
                right = i + m // 2
        return s[left:right+1]

    def mid_expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
```
```java []
class Solution {
    public String longestPalindrome(String s) {
        if(s.length() == 0) return "";
        int left = 0, right = 0;
        for (int i = 0; i < s.length(); i++) {
            int odd = midExpand(s, i, i);
            int even = midExpand(s, i, i + 1);
            int m = Math.max(odd, even);
            if (m > right - left) {
                left = i - (m - 1) / 2;
                right = i + m / 2;
            }
        }
        return s.substring(left, right + 1);
    }

    private int midExpand(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }
}
```

---

### 7. Reverse Integer
> 
>> 标签：位运算

---

- 思路为对当前数取对10的余数，再一项项填入res尾部，即可完成int翻转。
- 难点在于如何处理边界情况，int取值范围为`[-2^31, 2^31 - 1]`，如果翻转数字溢出，则立即`return 0`。
  - `python`存储数字理论上是无限长度，因此每次计算完后判断`res`与`of`的大小即可；
  - `java`数字计算会溢出，因此要判断`res`和`of / 10`的大小关系（即确定再添一位一定会溢出）。
- python负数取余操作与java不同，由于python的`//`操作是向下取整，导致正负数取余操作结果不一致，因此python需要将原数字转为正数操作。

```python
class Solution:
    def reverse(self, x: int) -> int:
        y, res = abs(x), 0
        of = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10
            if res > of: return 0
            y //= 10
        return res if x > 0 else -res
```

```java
class Solution {
    public int reverse(int x) {
        int res = 0;
        int of = ((1 << 31) - 1) / 10;
        while (x != 0) {
            if (Math.abs(res) > ((1 << 31) - 1) / 10) return 0;
            res = res * 10 + x % 10;
            x /= 10;
        }
        return res;
    }
}
```

---


### 8. String to Integer (atoi)
> 
>> 标签：字符串

---

1. 过滤空格；
2. 判断是否为正负号并存储；
3. 得到int数字；
4. 处理溢出；
5. 根据正负号返回。

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        i, res, neg, over = 0, 0, False, (1 << 31) - 1
        while i < len(s) and s[i] == ' ': # ignore space first
            i += 1
        if i < len(s) and (s[i] == '-' or s[i] == '+'): # save '-'
            neg = s[i] == '-'
            i += 1
        while i < len(s) and '0' <= s[i] <= '9': # generate number
            res = res * 10 + int(s[i])
            i += 1
        if res > over: # handle the overflow
            res = over + 1 if neg else over
        return -res if neg else res
```

---

### 9. Palindrome Number
> 
>> 标签：运算机制

---

- 首先，考虑`双指针法`，但`int`类型无法遍历每一位，转化为`str`需要额外空间，不符合题意；
- 其次，考虑`数字反转`，若反转后数字和原数字一样则为回文；
- 本解采用半倒置，即只取数字后一半并反转：
  - 由于return的判断机制，`x % 10 == 0`要直接返回false；
  - `x < 0`直接返回false。

```python []
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or not x % 10 and x: return False
        r = 0
        while x > r:
            x, rem = x // 10, x % 10
            r = r * 10 + rem
        return x == r or x == r // 10
```
```java []
class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0 || x % 10 == 0 && x != 0) return false;
        int y = 0;
        while(x > y){
            y = y * 10 + x % 10;
            x = x / 10;
        }
        return x == y || x == y / 10;
    }
}
```

---

### 12. Integer to Roman
> 
>> 标签：字符串

---

- 将整数转化为roman字符串，总体思路是先处理高位字符，舍去高位后再处理低位字符。如`1437`，先将`1000`的字符加入，再处理`437`，将`400`字符加入，再处理`37`……
- 有两种特例需要处理`9xx`，`4xx`，但总体上还是可以约化为先处理高位再处理低位的问题，如`1900`，先加入`1000`，再加入特例`900`……
- 开辟两个数组分别存储数字和对应字符，对`num`处理算出当前位需要几个字符，`k++`遍历下个字符，直到`num = 0`时返回。

```python []
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        values = [1000, 900, 500, 400,
                  100, 90, 50, 40,
                  10, 9, 5, 4,
                  1]
        symbols = ['M', 'CM', 'D', 'CD',
                   'C', 'XC', 'L', 'XL',
                   'X', 'IX', 'V', 'IV',
                   'I']
        i = 0
        while num > 0:
            count = num // values[i]
            res += "".join([symbols[i] for _ in range(count)])
            num -= count * values[i]
            i += 1
        return res
```
```java []
class Solution {
    private static final int[] values = {
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1};
    private static final String[] symbols = {
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"};
    public String intToRoman(int num) {
        StringBuilder res = new StringBuilder();
        int k = 0;
        while(num > 0){
            int count = num / values[k];
            for(int i = 0; i< count;i++){
                res.append(symbols[k]);
                num -= values[k];
            }
            k++;
        }
        return res.toString();
    }
}
```

---

### 13. Roman to Integer
> 
>> 标签：字符串，哈希表Hash

---

- 整体思路是用`Hash`存储`字符key`和`数字value`的关系，然后遍历roman字符串，在Hash表中取得对应数字加到结果中，遍历完成后返回；
- `Python`可以用字典做；`Java`可以用HashMap做，本题解两语言细节方法不同：
  - `Python`代码将两个字母的判断优先级放的更高，这样是为了优先处理`40`、`90`等由两个`char`表示的数字；
  - `Java`代码在遍历过程中记录上个字符，判断当前字符和上个字符关系再进行操作。


```python []
class Solution:
    def romanToInt(self, s: str) -> int:
        dic =  {'M':1000, 'CM': 900, 'D': 500, 'CD': 400, 
                'C':100, 'XC':90, 'L':50, 'XL':40,
                'X':10, 'IX': 9, 'V':5, 'IV':4,
                'I':1}
        i = res = 0
        while i < len(s):
            if i+1 < len(s) and s[i] + s[i+1] in dic:
                res += dic[s[i] + s[i+1]]
                i += 2
            elif s[i] in dic:
                res += dic[s[i]]
                i += 1
        return res
```
```java []
class Solution {
    private Map<Character, Integer> roman = new HashMap<Character, Integer>() {
        {
            put('M', 1000);
            put('D', 500);
            put('C', 100);
            put('L', 50);
            put('X', 10);
            put('V', 5);
            put('I', 1);
        }
    };

    public int romanToInt(String s) {
        int res = 0, pre = 0;
        for(Character c : s.toCharArray()){
            int cur = roman.get(c);
            res += cur > pre ? cur - 2 * pre : cur;
            pre = cur;
        }
        return res;
    }
}
```

---

### 20. Valid Parentheses
> 
>> 标签：栈，哈希表Hash

---

- 借助栈先入后出的特点，正好符合此题目的要求。
- 建立Map构建左右括号对应关系。
- 遍历`str`将`char`依次入栈，每次判断是否是正确对应括号，如果是则出栈，最终如果`stack`为空则是valid的。

```python []
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')'}
        stack = []
        for i in range(len(s)):
            if stack and stack[-1] in dic.keys() and s[i] == dic[stack[-1]]:
                stack.pop()
            else:
                stack.append(s[i])
        return not stack
```
```java []
class Solution {
    private static final Map<Character,Character> map = new HashMap<Character,Character>(){{
        put('{','}'); put('[',']'); put('(',')');
    }};
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for(Character c : s.toCharArray()){
            if(!stack.isEmpty() && map.containsKey(stack.peek()) && map.get(stack.peek()) == c){
                stack.pop();
            } else {
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}
```

---

### 21. Merge Two Sorted Lists
> 
>> 标签：双指针，链表

---

- 建立一个辅助`node`作为链表头部；
- 设两指针`l1`，`l2`分别指向两链表头部，根据指针`node`值大小改变`next`指向，交替前进；
- 最后将`l1`、`l2`剩余尾部加入，返回即可。


```python []
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        res = head
        while l1 and l2:
            if l1.val <= l2.val: head.next, l1 = l1, l1.next
            else: head.next, l2 = l2, l2.next
            head = head.next
        head.next = l1 if not l2 else l2
        return res.next
```
```java []
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode res = head;
        while (l1 != null && l2 != null) {
            if(l1.val <= l2.val){
                head.next = l1;
                l1 = l1.next;
            }
            else{
                head.next = l2;
                l2 = l2.next;
            }
            head = head.next;
        }
        head.next = l2 == null ? l1 : l2;
        return res.next;
    }
}
```

---

### 23. Merge k Sorted Lists
> 
>> 标签：链表，归并，分治

---

- 在`21题合并两个list`的基础上，将`k`个链表两两合并，再对剩下`k/2`个链表两两合并……直到合并为一个链表。
- 本质上是归并排序的merge过程，时间复杂度`O(n k logk)`。

```python []
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        while len(lists) > 1:
            tmp = []
            for i in range(0, len(lists), 2):
                r = None if i == len(lists) - 1 else lists[i+1]
                tmp.append(self.merge(lists[i], r))
            lists = tmp
        return lists[0] if lists else None

    def merge(self, h1, h2):
        res = head = ListNode(0)
        while h1 and h2:
            if h1.val <= h2.val:
                head.next = h1
                h1 = h1.next
            else:
                head.next = h2
                h2 = h2.next
            head = head.next
        head.next = h1 if not h2 else h2
        return res.next
```
```java []
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        List<ListNode> listss = Arrays.asList(lists);
        while (listss.size() > 1) {
            List<ListNode> tmp = new ArrayList<>();
            for (int i = 0; i < listss.size(); i += 2) {
                ListNode r = i == listss.size() - 1 ? null : listss.get(i + 1);
                tmp.add(merge(listss.get(i), r));
            }
            listss = tmp;
        }
        return listss.size() == 0 ? null : listss.get(0);
    }

    private ListNode merge(ListNode h1, ListNode h2) {
        ListNode head = new ListNode(0);
        ListNode res = head;
        while (h1 != null && h2 != null) {
            if (h1.val <= h2.val) {
                head.next = h1;
                h1 = h1.next;
            } else {
                head.next = h2;
                h2 = h2.next;
            }
            head = head.next;
        }
        head.next = h2 == null ? h1 : h2;
        return res.next;
    }
}
```

---

### 24. Swap Nodes in Pairs
> 
>> 标签：链表，递归

---

- 遍历链表，一一修改指针，有`迭代`和`递归`两种做法。

```Python []
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode(0)
        res = pre
        while head and head.next:
            nex = head.next.next
            pre.next = head.next
            pre = head
            head.next.next = head
            head = nex
        pre.next = head
        return res.next
```
```Python []
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        nex = head.next
        head.next = self.swapPairs(nex.next)
        nex.next = head
        return nex
```
```Java []
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode pre = new ListNode(0);
        ListNode res = pre;
        while(head != null && head.next != null){
            ListNode nex = head.next.next;
            pre.next = head.next;
            pre = head;
            head.next.next = head;
            head = nex;
        }
        pre.next = head;
        return res.next;
    }
}
```

---

### 28. Implement strStr()
> 
>> 标签：字符串

---

- 暴力法，复杂度O(MN)

```python []
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        l_h, l_n = len(haystack), len(needle)
        for i in range(l_h + 1):
            for j in range(l_n + 1):
                if j == l_n: return i
                if i + j == l_h: return -1
                if haystack[i+j] != needle[j]: break

    def strStr1(self, haystack, needle):
        return haystack.find(needle)
```
```java []
class Solution {
    public int strStr(String haystack, String needle) {
        if (needle == "") return 0;
        for (int i = 0;; i++) {
            for (int j = 0;; j++) {
                if (j == needle.length()) return i;
                if (i + j == haystack.length()) return -1;
                if (haystack.charAt(i + j) != needle.charAt(j)) break;
            }
        }
    }
}
```

---

### 35. Search Insert Position
> 
>> 标签：数组，二分法

---

- `寻找插入点`使用二分法，但与`寻找某数字`不同的是，需要考虑一些边界条件：
  - 当插入数字和`nums`中某数字相等时，插入到左边还是右边？`本题要求插到左边`；
  - 插入数字在`nums`第一个数字左边，或在最后一个数字右边；
- 推荐记住其中的几个关键点写法。


```python []
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target: left = mid + 1 # insert left side
            else: right = mid - 1
        return left
```
```java []
class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return left;
    }
}
```

---

### 53. Maximum Subarray
> 
>> 标签：动态规划，数组

---

- 动态规划典型题：遍历数组，记录`max(nums[i-1] + nums[i], nums[i])`，即判断后面`subarray`是否舍去前面的加和；
- 最后return加和中最大值。

```python []
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
        return max(nums)
```
```java []
class Solution {
    public int maxSubArray(int[] nums) {
        int res = Integer.MIN_VALUE;
        for(int i = 1; i < nums.length; i++){
            nums[i] = Math.max(nums[i], nums[i] + nums[i - 1]);
            res = Math.max(res, nums[i]);
        }
        return res;
    }
}
```

---

### 54. Spiral Matrix
> 
>> 标签：数组

---

- 此方法不使用额外空间`O(1)`，时间复杂度`O(MN)`：
  - `i`,`j`记录目前走到的位置；
  - `h`, `l`记录剩余矩阵的高度、宽度；
  - 沿着右下左上的顺序走，每走完一条直线将对应`高度/宽度-1`；
  - 若剩余矩阵`高度or宽度==0`，代表已经走完`break`。


```python []
class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        if not matrix: return []
        res = []
        h, l = len(matrix), len(matrix[0])
        i, j = 0, -1
        while True:
            for _ in range(l):
                j += 1
                res.append(matrix[i][j])
            h -= 1
            if not h: break
            for _ in range(h):
                i += 1
                res.append(matrix[i][j])
            l -= 1
            if not l: break
            for _ in range(l):
                j -= 1
                res.append(matrix[i][j])
            h -= 1
            if not h: break
            for _ in range(h):
                i -= 1
                res.append(matrix[i][j])
            l -= 1
            if not l: break
        return res
```
```java []
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
        if (matrix.length == 0) return res;
        int h = matrix.length, l = matrix[0].length;
        int i = 0, j = -1;
        while (true) {
            for (int k = 0; k < l; k++)
                res.add(matrix[i][++j]);
            if (--h == 0) break;
            for (int k = 0; k < h; k++)
                res.add(matrix[++i][j]);
            if (--l == 0) break;
            for (int k = 0; k < l; k++)
                res.add(matrix[i][--j]);
            if (--h == 0) break;
            for (int k = 0; k < h; k++)
                res.add(matrix[--i][j]);
            if (--l == 0) break;
        }
        return res;
    }
}
```


---

### 62. Unique Paths
> 
>> 标签：动态规划，数组

---

- 设 `m×n` 方格有 `f(m,n)` 个不同解，则先让机器人向右走一步 or 向左走一步，可以推出 `f(m,n) = f(m-1,n) + f(m,n-1)`。
- 创建 `m+1×n+1` 的矩阵，根据以上规则计算对角线方格的值：
  - 要加一行一列，是为了解决`f(0,0) = f(-1,0) + f(0,-1)`出现的边界问题；
  - 将 'f(0,1)'置`1`是为了给迭代启动值（ `m×n` 地图第一行和第一列值都应为1）。
- 时间复杂度`O(MN)`，空间复杂度`O(MN)`。

```Python []
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]
        matrix[0][1] = 1
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[-1][-1]
```
```Java []
class Solution {
    public int uniquePaths(int m, int n) {
        int[][] matrix = new int[m + 1][n + 1];
        matrix[0][1] = 1;
        for (int i = 1; i < matrix.length; i++) {
            for (int j = 1; j < matrix[0].length; j++) {
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1];
            }
        }
        return matrix[m][n];
    }
}
```

---

### 63. Unique Paths II
> 
>> 标签：动态规划，数组

---

- 和`62题`动态规划思路类似，不同的是，需要对障碍物做处理：`f(m,n) = f(m-1,n)+f(m,n-1)` if `map(m)(n) != 1` else `f(m,n) = 0`；
- 此处理的含义是`f(m,n)`对`f(m+1,n)`和`f(m,n+1)`的贡献归零，这样就可以把所有经过障碍物的路线排除掉。


```python []
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        matrix = [[0 for _ in range(len(obstacleGrid[0])+1)]
                  for _ in range(len(obstacleGrid)+1)]
        matrix[0][1] = 1
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j - 1] \
                    if obstacleGrid[i-1][j-1] != 1 else 0
        return matrix[-1][-1]
```
```java []
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid.length == 0) return 0;
        int[][] matrix = new int[obstacleGrid.length + 1][obstacleGrid[0].length + 1];
        matrix[0][1] = 1;
        for (int i = 1; i < matrix.length; i++) {
            for (int j = 1; j < matrix[0].length; j++) {
                matrix[i][j] = obstacleGrid[i - 1][j - 1] != 1 ? matrix[i - 1][j] + matrix[i][j - 1] : 0;
            }
        }
        return matrix[obstacleGrid.length + 1][obstacleGrid[0].length + 1];
    }
}
```

---

### 65. Valid Number
> 
>> 标签：自动机，哈希表Hash

---

- 画出`状态转移表`，结构为`states[n]`存储`n`个状态；
- `states[i]`为一个HashTable，表示从此状态允许跳转到的状态。
- 主循环中遍历字符串，通过状态转移表判断结构是否成立：
  - 若中途遇到无法跳转的状态，直接返回`False`；
  - 若成功遍历完字符串，要判断结束状态是否在允许的结束状态内，本题为`[2, 3, 7, 8]`。

```python []
class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            { 'b': 0, 's': 1, 'd': 2, '.': 4 }, # 0. start
            { 'd': 2, '.': 4 } ,                # 1. 'sign' before 'e'
            { 'd': 2, '.': 3, 'e': 5, 'b': 8 }, # 2. 'digit' before 'dot'
            { 'd': 3, 'e': 5, 'b': 8 },         # 3. 'dot' with 'digit'
            { 'd': 3 },                         # 4. no 'digit' before 'dot'
            { 's': 6, 'd': 7 },                 # 5. 'e'
            { 'd': 7 },                         # 6. 'sign' after 'e'
            { 'd': 7, 'b': 8 },                 # 7. 'digit' after 'e'
            { 'b': 8 }                          # 8. end with
        ]
        p = 0
        for c in s:
            if '0' <= c <= '9': typ = 'd'
            elif c == ' ': typ = 'b'
            elif c == '.': typ = '.'
            elif c == 'e': typ = 'e'
            elif c in "+-": typ = 's'
            else: typ = '?'
            if typ not in states[p]: return False
            p = states[p][typ]
        return p in [2, 3, 7, 8]
```

---

### 66. Plus One
> 
>> 标签：

---

- 遍历`digits`，判断每位是否为`9`，若不是则`+1`并返回，否则将此位置`0`；
- 对于`digits`里全为`9`的情况，需要扩展list，并将首位置为`1`。

```python []
class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits[0] = 1
        digits.append(0)
        return digits
```
```java []
class Solution {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            if(digits[i] != 9){
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        digits = new int[digits.length + 1];
        digits[0] = 1;
        return digits;
    }
}
```

---

### 70. Climbing Stairs
> 
>> 标签：动态规划

---

- 设爬 `n `个台阶有 `f(n)` 种可能：
  - 假设先爬`1`阶，剩下` n-1` 阶有` f(n-1)` 种可能；
  - 假设先爬`2`阶，剩下 `n-2 `阶有 `f(n-2)` 种可能，
  - 因此爬`n`阶可以转化为两种爬`n-1`阶问题之和：`f(n) = f(n-1) + f(n-2)`；
- 不难看出，这就是`斐波那契数列`公式，此题可转化为求斐波那契数列第`n`项。


```Python []
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n-1):
            a, b = a + b, a
        return a
```
```Java []
class Solution {
    public int climbStairs(int n) {
        int a = 1, b = 1;
        for(int i = 0; i < n - 1; i++){
            int tmp = a;
            a = a + b;
            b = tmp;
        }
        return a;
    }
}
```

---

### 98. Validate Binary Search Tree
> 
>> 标签：二叉搜索树BST,中序遍历

---

- 二叉搜索树的中序遍历是一个已排序`List`，我们可以根据此性质对树进行中序遍历并判断：
- 设置一个全局变量`tmp`，记录中序遍历上一个值，始终比较当前值和上一个值大小，若`当前值<=上一个值`则`返回false`；
- 当找到不符搜索树性质情况时，一路`返回false`，以下python和java使用两种写法，但原理上是等价的。

```python []
class Solution:
    def __init__(self):
        self.tmp = -float('inf')
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        if not self.isValidBST(root.left): return False
        if self.tmp >= root.val: return False
        self.tmp = root.val
        if not self.isValidBST(root.right): return False
        return True
```
```java []
class Solution {
    long tmp = Long.MIN_VALUE;
    public boolean isValidBST(TreeNode root) {
        if(root == null) return true;
        if (isValidBST(root.left)) {
            if (tmp < root.val) {
                tmp = root.val;
                return isValidBST(root.right);
            }
        }
        return false;
   }
}
```

---

### 104. Maximum Depth of Binary Tree
> 
>> 标签：递归、深度优先搜索DFS

---

- `递归公式：`树深度 = max(左子树深度，右子树深度) + 1
- `终止条件：`越过叶子节点，return 0

```python []
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```
```java []
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
```

---

### 108. Convert Sorted Array to Binary Search Tree
> 
>> 标签：平衡二叉树BBT，二叉搜索树BST

---

- 将一个排序array转化为平衡二叉搜索树：
  - `平衡二叉树`：对于每个根节点，`左右子树高度差 <= 1`；
  - `二叉搜索树`：对于每个节点，其`左子树值<此节点值`，`右子树>此节点值`。
- 要满足以上两个特点，我们自然想到以`array中点值`作为根节点值，并递归重建，这样就可以同时保证以上两个条件。


```python []
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
```
```java []
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return toBST(nums, 0, nums.length - 1);
    }

    private TreeNode toBST(int[] nums, int left, int right) {
        if(left > right) return null;
        int mid = (left + right) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = toBST(nums, left, mid - 1);
        root.right = toBST(nums, mid + 1, right);
        return root;
    }
}
```

---

### 109. Convert Sorted List to Binary Search Tree
> 
>> 标签：二叉搜索树BST，深度优先搜索DFS，回溯法

---

- 做过数组还原平衡二叉搜索树（推荐先做`题号108`），我们知道，在`array`中每次取中点作为根节点，左右分别构建左右子树，递归直至根节点为空。
- 链表的特性导致我们无法像数组那样通过下标访问各个元素。若想按照`108题`的做法，就需要设置两个指针`p1` `p2`，`p1`每走一步`p2`走两步，这样`p2`结束时`p1`就在中点。但这样会导致每次递归都需要重复遍历链表，效率较低。
- 我们考虑是否可以让建立节点的顺序匹配链表元素顺序？这样每次建立节点时，只需要获取链表下一个元素即可。
- 使用递归模拟`中序遍历`过程，建立节点的顺序即与链表元素顺序一一对应，`bottom-up`建立树，最终返回根节点。
- 递归前需要统计链表长度`n`，整体算法复杂度`O(N)`。


```python []
class Solution:
    def __init__(self):
        self.head = None
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        n, self.head = 0, head
        while head:
            head = head.next
            n += 1
        return self.to_bst(0, n - 1)
    def to_bst(self, left, right):
        if left > right: return
        m = (left + right) // 2
        left_child = self.to_bst(left, m - 1)
        father = TreeNode(self.head.val)
        self.head = self.head.next
        father.left = left_child
        father.right = self.to_bst(m + 1, right)
        return father
```
```java []
class Solution {
    private ListNode node;
    public TreeNode sortedListToBST(ListNode head) {
        int n = 0;
        node = head;
        while(head != null){
            head = head.next;
            n++;
        }
        return toBST(0, n-1);
    }
    private TreeNode toBST(int left, int right){
        if(left > right) return null;
        int m = (left + right) / 2;
        TreeNode left_child = toBST(left, m-1);
        TreeNode father = new TreeNode(node.val);
        node = node.next;
        father.left = left_child;
        father.right = toBST(m+1, right);
        return father;
    }
}
```

---

### 110. Balanced Binary Tree
> 
>> 标签：平衡二叉树BBT，递归

---

#### Bottom-up 提前阻断法（复杂度 `O(N)`）

- 在对`root`做`dfs`时，会从下至上获得每个`root`的左右子树高度，当我们发现有一例`左右子树高度差 ＞1`的情况时`return -1`，代表此树不是平衡树，后面的高度计算都没有意义了，之后一路`return -1`，不再做后面的`DFS`。

```Python []
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.depth(root) != -1

    def depth(self, root):
        if not root: return 0
        left = self.depth(root.left)
        if left == -1: return -1
        right = self.depth(root.right)
        if right == -1: return -1
        return max(left,right) + 1 if abs(left - right) < 2 else -1
```
```Java []
class Solution {
    public boolean isBalanced(TreeNode root) {
        return depth(root) != -1;
    }

    private int depth(TreeNode root) {
        if (root == null) return 0;
        int left = depth(root.left);
        if(left == -1) return -1;
        int right = depth(root.right);
        if(right == -1) return -1;
        return Math.abs(left - right) < 2 ? Math.max(left, right) + 1 : -1;
    }
}
```

#### Brute force 暴力法（复杂度`O(N^2`）

- 构造一个获取当前节点最大深度的方法 `depth()`，通过比较左右子树最大深度差来判断是否是二叉平衡树；
- 以每个节点为根节点，递归判断，所有节点满足平衡二叉树性质则返回 `True`；
- 本方法在计算节点深度时产生大量重复计算，时间复杂度 `O(N^2)`。


```Python []
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
```
```Java []
class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) return true;
        return Math.abs(depth(root.left) - depth(root.right)) <= 1 && isBalanced(root.left) && isBalanced(root.right);
    }

    private int depth(TreeNode root) {
        if (root == null) return 0;
        return Math.max(depth(root.left), depth(root.right)) + 1;
    }
}
```

---

### 111. Minimum Depth of Binary Tree
> 
>> 标签：二叉树，递归

---

- 这道题和`maximum depth`题正好相反，是求`根节点`到`叶子节点`的最小深度，为确保统计的是`根节点`到`叶子节点`的深度，需要注意：
  - 当前节点`左右子树`有一个为空时，返回的应是`非空子树`的最小深度，而不是`空子树`深度0；若返回0相当于把当前节点认为成`叶子节点`，与此节点有`非空子树`矛盾。
  - 当`左右子树`都不为空时，和`maximum depth`题一样，返回左右子树深度的最小值。
  - 当`左右子树`都为空时，只有1个根节点深度为1（根节点与叶子节点重合）。


```python []
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left: return self.minDepth(root.right) + 1
        if not root.right: return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
```
```java []
class Solution {
    public int minDepth(TreeNode root) {
        if(root == null) return 0;
        if(root.left == null) return minDepth(root.right) + 1;
        if(root.right == null) return minDepth(root.left) + 1;
        return Math.min(minDepth(root.left),minDepth(root.right)) + 1;
    }
}
```

---

### 124. Binary Tree Maximum Path Sum
> 
>> 标签：二叉树，递归

---

- 根据题意，最大路径和可能出现在：
  - 左子树中
  - 右子树中
  - 包含根节点与左右子树
- 我们的思路是递归从bottom向top`return`的过程中，记录`左子树和右子树中路径更大的那个`，并向父节点提供`当前节点和子树组成的最大值`。
- 递归设计：
  - 返回值：`(root.val) + max(left, right)` 即此节点与左右子树最大值之和，较差的解直接被舍弃，不会再被用到。
    - 需要注意的是，若计算结果`tmp <= 0`，意味着对根节点有`负贡献`，不会在任何情况选这条路（父节点中止），因此返回`0`。
  - 递归终止条件：越过叶子节点，返回`0`；
  - 记录最大值：当前节点`最大值 = root.val + left + right`。
- 最终返回所有路径中的全局最大值即可。
  

```python []
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = float('-inf')
        self.max_path(root)
        return self.max
        
    def max_path(self, root):
        if not root: return 0
        left = self.max_path(root.left)
        right = self.max_path(root.right)
        self.max = max(left + right + root.val, self.max)
        tmp = max(left, right) + root.val
        return tmp if tmp > 0 else 0
```
```java []
class Solution {
    private int max = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        maxPath(root);
        return max;
    }
    private int maxPath(TreeNode root){
        if(root == null) return 0;
        int left = maxPath(root.left);
        int right = maxPath(root.right);
        max = Math.max(root.val + left + right, max);
        int tmp = Math.max(left, right) + root.val;
        return tmp > 0 ? tmp : 0;
    }
}
```

---

### 125. Valid Palindrome
> 
>> 标签：字符串，双指针

---

- 设置左、右`双指针`，向中间判断；
- 跳过`非数字字母`的字符；
- 将字母全部转化为`小写体`，之后判断。
- `java`用了库函数，`python`纯自己实现（运行时间不太理想）。

```python []
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        case = abs(ord('a') - ord('A'))
        while left < right:
            while left < right and self.not_letters_digits(s[left]): left += 1
            while left < right and self.not_letters_digits(s[right]): right -= 1 
            s_l = ord(s[left]) - case if s[left] >= 'a' else ord(s[left])
            s_r = ord(s[right]) - case if s[right] >= 'a' else ord(s[right])
            if s_l != s_r: return False
            left += 1
            right -= 1
        return True
    
    def not_letters_digits(self, c):
        return not 'A' <= c <= 'Z' and not 'a' <= c <= 'z' and not '0' <= c <= '9'
```
```java []
class Solution {
    public boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        while(i < j){
            while(i < j && !Character.isLetterOrDigit(s.charAt(i))) i++;
            while(i < j && !Character.isLetterOrDigit(s.charAt(j))) j--;
            if(Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j))) return false;
            i++; j--;
        }
        return true;
    }
}
```

---

### 133. Clone Graph
> 
>> 标签：图，深度优先遍历DFS

---

- 从给定节点开始，使用DFS遍历整个图，建立`node`节点的复制`copy`节点；
- 递归遍历`node.neighbors`，建立`copy`节点的各个`neighbor`；
- 每次建立`copy`时，将节点添加进HashMap：
  - `key = node`，`value = copy`
- `终止条件：`每次dfs首先判断HashMap中是否已经存在此`node`节点，若存在则直接return此HashMap中的`copy`节点。


```python []
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.dic = {} # store all the copy nodes: dic[node] = copy
        return self.dfs(node)

    def dfs(self, node):
        if node not in self.dic:
            self.dic[node] = copy = Node(node.val, []) # get copy of the node 'node' and add it into the dictionary.
            for nei in node.neighbors: # recursive: get the neighbors of the node 'copy'.
                copy.neighbors.append(self.dfs(nei)) 
        return self.dic[node] # return the node 'copy'.
```
```java []
class Solution {
    private Map<Node, Node> map;
    public Node cloneGraph(Node node) {
        map = new HashMap<>();
        return dfs(node);        
    }
    private Node dfs(Node node) {
        if(!map.containsKey(node)){
            Node copy = new Node(node.val, new ArrayList<Node>());
            map.put(node, copy);
            for(Node nei : node.neighbors){
                copy.neighbors.add(dfs(nei));
            }
        }
        return map.get(node);
    }
}
```

---

### 136. Single Number
> 
>> 标签：数组，位运算

---

- 通过题目已知信息，需要`O(N)`时间复杂度和`O(1)`空间复杂度，即遍历一遍`arr`就需要得出答案，考虑：
  - 最多遍历一次`arr`就要得到答案；
  - 两个相同的数字经过此运算为`0`；
  - 满足`交换律`，即打乱`arr`元素排列顺序不改变答案。
- 因此，想到`异或xor`操作，异或有以下两个性质：
  - `a ^ a = 0`
  - `0 ^ a = a`
- 从而遍历`arr`后，留下来的数字即为只出现一次的数字。

```python []
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
```
```java []
class Solution {
    public int singleNumber(int[] nums) {
        int res = 0;
        for(int num : nums){
            res ^= num;
        }
        return res;
    }
}
```

---

### 137. Single Number II
> 
>> 标签：数组，位运算

---

- 这道题是`136题`拓展，`136题`中我们用到了`异或运算`，其实异或运算的另一个含义是“二进制下不考虑进位的加法”：0+0 = 0， 1+1=0……
- 我们联想到，是否可以通过某种运算`$`，使`a $ a $ a` = 0，`0 $ a = a`，即创建“三进制下不考虑进位的加法”，这样将整个`arr`遍历加和，留下来的就是那个只出现一次的数字（其余各位都出现了`3x`次，一定为`0`）。
- 看到下面一堆与、或、非、异或运算应该很懵吧……下面一条条分析：
  - `ones`记录至目前元素，各位元素出现`1`次的位置；
  - `twos`记录至目前元素，各位元素出现`2`次的位置；
  - `threes`记录至目前元素，各位元素出现`3`次的位置
每轮完成时，当`threes`里某位为`1`时（代表此位出现了3次），需要将`ones` `twos`的对应位清零。

```python []
class Solution:
    def singleNumber(self, nums: [int]) -> int:
        ones, twos, threes = 0, 0, 0
        for num in nums:
            twos |= ones & num # ones & num 提取两个数都为1的位，与twos作或操作保留出现2次的位
            ones ^= num  # 当 ones 和 num 同时为 1 or 0 时，ones = 0，因为同时为1已经加到twos里了，这里不做count
            threes = ones & twos # 当ones和twos对应位都为1时，说明此位出现了3次
            ones &= ~threes # three为1的位，将one和two对应位归零
            twos &= ~threes
        return ones
```
```java []
class Solution {
    public int singleNumber(int[] nums) {
        int ones = 0, twos = 0, threes = 0;
        for(int num : nums){
            twos |= ones & num;
            ones ^= num;
            threes = ones & twos;
            ones &= ~threes;
            twos &= ~threes;
        }
        return ones;
    }
}
```

---

### 138. Copy List with Random Pointer
> 
>> 标签：链表，多指针

---

1. 复制与合并：假设原链表为`ABCDE……`，从前到后复制得到`A'B'C'D'E'……`，合并得到`AA'BB'CC'DD'EE'……`。此步骤是为了从空间上构建`random`对应关系；
2. 设置复制链表的random项：`A.next.random = A.random.next`；
3. 将两列表分离，返回deepcopy链表表头。


```python []
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        pre, cur = Node(0, None, None), head
        while cur: # copy and merge.
            nex = cur.next
            pre.next = cur
            cur.next = Node(cur.val, None, None)
            pre = cur.next
            cur = nex
        cur = head
        while cur: # set the 'random' nodes.
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        cur, res = head, head.next
        while cur.next: # divide the two linked lists.
            nex = cur.next
            cur.next = nex.next
            cur = nex
        return res
```
```java []
class Solution {
    public Node copyRandomList(Node head) {
        if(head == null) return null;
        Node pre = new Node(0, null, null), cur = head, nex = cur.next;
        while(cur != null){
            nex = cur.next;
            pre.next = cur;
            cur.next = new Node(cur.val, null, null);
            pre = cur.next;
            cur = nex;
        }
        cur = head;
        while(cur != null){
            cur.next.random = cur.random != null ? cur.random.next : null;
            cur = cur.next.next;
        }
        cur = head;
        Node res = head.next;
        while(cur.next != null){
            nex = cur.next;
            cur.next = nex.next;
            cur = nex;
        }
        return res;
    }
}
```

---

### 150. Evaluate Reverse Polish Notation
> 
>> 标签：字符串，栈

---

- 解析`逆波兰式（后缀表达式）`；同理还有前缀表达式、中缀表达式。
- 利用栈先进后出的特性遍历逆波兰式，当遇到计算符号时pop前两个字符进行计算，将计算结果push进stack；遇到数字时直接push进stack。


```python []
class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        symbol = ['+', '-', '*', '/']
        stack = []
        for t in tokens:
            if t in symbol:
                stack.append(self.eval(stack.pop(-2), stack.pop(), t))
            else:
                stack.append(int(t))
        return stack[-1]


    def eval(self, x, y, symbol):
        if symbol == '+': return x + y
        if symbol == '-': return x - y
        if symbol == '*': return x * y
        if symbol == '/': return int(x / y)
```
```java []
class Solution {
    private static final Set<String> SYMBOLS = new HashSet<>(Arrays.asList("+","-","*","/"));
    
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for(String t : tokens){
            if(SYMBOLS.contains(t)){
                int y = stack.pop();
                int x = stack.pop();
                stack.push(eval(x, y, t));
            } else {
                stack.push(Integer.parseInt(t));
            }
        }
        return stack.peek();
    }

    private int eval(int x, int y, String symbol){
        switch(symbol){
            case "+": return x + y;
            case "-": return x - y;
            case "*": return x * y;
            default:  return x / y;
        }
    }
}
```

---

### 151. Reverse Words in a String
> 
>> 标签：字符串，双指针

---

- 先处理字符串，将首尾空格都删除；
1. 倒序遍历字符串，当第一次遇到空格时，添加`s[i + 1: j]`（即添加一个完整单词）；
2. 然后，将直至下一个单词中间的空格跳过，并记录下一个单词尾部`j`；
3. 继续遍历，直至下一次遇到第一个空格，回到`1.`步骤；
- 由于`s`首部没有空格，因此最后需要将第一个单词加入，再return。
- python可一行实现。

```python []
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        res = ""
        i, j = len(s) - 1, len(s)
        while i > 0:
            if s[i] == ' ':
                res += s[i + 1: j] + ' '
                while s[i] == ' ': i -= 1
                j = i + 1
            i -= 1
        return res + s[:j]
```
```python []
    def reverseWords1(self, s: str) -> str:
        return " ".join(s.split()[::-1])
```
```java []
class Solution {
    public String reverseWords(String s) {
        StringBuffer res = new StringBuffer();
        s = s.trim(); // delete leading or trailing spaces.
        int i = s.length() - 1, j = s.length();
        while (i > 0) {
            if (s.charAt(i) == ' ') {
                res.append(s.substring(i + 1, j));
                res.append(' ');
                while (s.charAt(i) == ' ') i--; // ignore extra spaces between words.
                j = i + 1;
            }
            i--;
        }
        return res.append(s.substring(0, j)).toString();
    }
}
```

---

### 152. Maximum Product Subarray
> 
>> 标签：动态规划，数组

---

- 此题与53题类似，不同处是53题的运算是加法，本题是乘法。
  - 对于加法，在遍历数组中始终取`max(ma + nums[i], nums[i])`即可，因为无论`nums[i]`的正负如何，
  - 对与乘法，在遍历数组中，若`nums[i]`是负数，那么当前最大值`ma * nums[i]`会变成当前最小值（负数），因此不能简单的只记录最大值。
- 本题的解题思路是同时记录当前最大值和最小值`ma, mi`：
  - 当`nums[i]`是正数时，`ma, mi * nums[i]`仍然是最大值，最小值；
  - 当`nums[i]`是负数时，`ma, mi * nums[i]`将变成最小值， 最大值；
  - 因此，当`nums[i] < 0`时，我们交换`ma, mi`。
- 在遍历`nums`过程中，每次更新`res`获取全局最大值。

```python []
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mi = ma = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0: mi, ma = ma, mi
            ma = max(ma * nums[i], nums[i])
            mi = min(mi * nums[i], nums[i])
            res = max(res, ma)
        return res 
```
```java []
class Solution {
    public int maxProduct(int[] nums) {
        int max = nums[0], min = nums[0], res = nums[0];
        for(int i = 1; i < nums.length; i++){
            if(nums[i] < 0){
                int tmp = max;
                max = min;
                min = tmp;
            }
            max = Math.max(nums[i], max * nums[i]);
            min = Math.min(nums[i], min * nums[i]);
            res = Math.max(max, res);
        }
        return res;
    }
}
```

---

### 153. Find Minimum in Rotated Sorted Array
> 
>> 标签：数组，二分法

---

- 旋转排序数组`nums`可以被拆分为2个排序数组`nums1`, `nums2`，并且`nums1`中所有元素比`nums2`大（因为`nums`中没有重复值）；
- 因此，考虑二分法寻找值`nums[i]`，满足`nums[i] < nums[i-1]` and `nums[i] < nums[i+1]`
- 设置`left`, `right`指针在nums数组两端，`mid`为中点：
  - 当`nums[mid] > nums[right]`时，一定满足`mid < i <= right`，因此`left = mid + 1`；
  - 当`nums[mid] < nums[right]`时，一定满足`left< i <= mid`，因此`right = mid`；
  - 当`nums[mid] == nums[right]`时，说明数组长度`len(num) == 1`（因为计算mid向下取整）；当`left = right`也满足，但本题`left == right`时跳出循环。


```python []
class Solution:
    def findMin(self, nums: [int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: left = mid + 1
            else: right = mid
        return nums[left]
```
```java []
class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;
        while(left < right){
            int mid = (left + right) / 2;
            if(nums[mid] > nums[right]) left = mid + 1;
            else right = mid;
        }
        return nums[left];
    }
}
```

---

### 154. Find Minimum in Rotated Sorted Array II
> 
>> 标签：二分法，数组

---

- 旋转排序数组`nums`可以被拆分为2个排序数组`nums1`, `nums2`，并且`nums1`所有元素>=`nums2`所有元素；
- 因此，考虑二分法寻找值`nums[i]`；
- 设置`left`, `right`指针在nums数组两端，`mid`为中点：
  - 当`nums[mid] > nums[right]`时，一定满足`mid < i <= right`，因此`left = mid + 1`；
  - 当`nums[mid] < nums[right]`时，一定满足`left < i <= mid`，因此`right = mid`；
  - 当`nums[mid] == nums[right]`时，是此题对比`153`题的难点（原因是此题中数组的元素`可重复`，相等就难以判断最小值的指针区间）；先说结果：采用`right = right - 1`，下面证明：
    - 首先，此操作`不会使数组越界`，因为`right > left > 0`；
    - 其次，此操作`不会使最小值丢失`，证明：假设'nums[right]'是最小值，有两种情况：
        - 若`nums[right]`是唯一最小值：那就不可能满足判断条件`nums[mid] == nums[right]`，因为`left != right`且`mid = left + right // 2  < right`（向下取整）；
        - 若有其他元素和`nums[right]`同为最小值：还有最小值存在于`[left, right -1]`间，不会丢失最小值。
- 以上是理论分析，可以用以下数组辅助思考：
  - `[1, 2, 3]`
  - `[1, 1, 0, 1]`
  - `[1, 0, 1, 1, 1]`
  - `[1, 1, 1, 1]`

```python []
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: left = mid + 1
            elif nums[mid] < nums[right]: right = mid
            else: right = right - 1 # key
        return nums[left]
```
```java []
class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] > nums[right]) left = mid + 1;
            else if (nums[mid] < nums[right]) right = mid;
            else right = right - 1;
        }
        return nums[left];
    }
}
```

---

### 155. Min Stack
> 
>> 标签：栈，设计

---

- 借用一个辅助栈`min_stack`，每当push新值进来时，如果小于等于`min_stack`栈顶值则一起push到`min_stack`；
- pop时判断是否是最小值，如果是则`min_stack`一起pop，这样可以保证`min_stack栈顶始终是`stack`中的最小值。
- 时间空间复杂度都为`O(N)`。


```python []
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]: 
            self.min_stack.append(x)
    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
```
```java []
class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> min_stack;
    /** initialize your data structure here. */
    public MinStack() {
        stack = new Stack<>();
        min_stack = new Stack<>();
    }
    
    public void push(int x) {
        stack.push(x);
        if(min_stack.isEmpty() || x <= min_stack.peek())
            min_stack.push(x);
    }
    
    public void pop() {
        if(stack.pop().equals(min_stack.peek()))
            min_stack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return min_stack.peek();
    }
}
```

---

### 156. Binary Tree Upside Down
> 
>> 标签：树，迭代

---

- 根据题目描述，树中任何节点的右子节点若存在一定有左子节点，因此思路是向左遍历树进行转化；
- 规律是：左子节点变父节点；父节点变右子节点；右子节点变父节点。
- 对于某节点`root`，修改`root.left`，`root.right`之前，需要将三者都存下来：
  - `root.left`是下一轮递归的主节点；
  - `root`是下一轮递归`root`的`root.right`；
  - `root.right`是下一轮递归`root`的`root.left`。
- 返回parent。



```python []
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        parent = parent_right = None
        while root:
            root_left = root.left
            root.left = parent_right
            parent_right = root.right
            root.right = parent
            parent = root
            root = root_left
        return parent
```
```java []
class Solution {
    public TreeNode upsideDownBinaryTree(TreeNode root) {
        TreeNode parent = null, parent_right = null;
        while(root != null){
            TreeNode root_left = root.left;
            root.left = parent_right;
            parent_right = root.right;
            root.right = parent;
            parent = root;
            root = root_left;
        }
        return parent;
    }
}
```

---

### 159. Longest Substring with At Most Two Distinct Characters
> 
>> 标签：字符串，双指针

---

- 设置两指针`i`, `j`指向str头部：
  - `j`向右移动，`dic[j]`统计目前`[i:j]`间`s[j]`出现次数，`dist`统计不同字符的数量；
  - `j`移动一格后，若`dist > 2`，移动左指针`i`，直到`[i:j]`间不同字符数量`<=2`；
  - `j`每移动一格，需统计一次最大字串长度`res = max(res, j - i + 1)`。

```python []
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dic = {}
        i, dist, res = 0, 0, 0
        for j in range(len(s)):
            if s[j] in dic and dic[s[j]]:
                dic[s[j]] += 1
            else:
                dic[s[j]] = 1
                dist += 1
            while dist > 2:
                dic[s[i]] -= 1
                if not dic[s[i]]: dist -= 1
                i += 1
            res = max(res, j - i + 1)
        return res
```
```java []
class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        int[] count = new int[256];
        int i = 0, numDistinct = 0, maxLen = 0;
        for (int j = 0; j < s.length(); j++) {
            if (count[s.charAt(j)] == 0) numDistinct++;
            count[s.charAt(j)]++;
            while (numDistinct > 2) {
                count[s.charAt(i)]--;
                if (count[s.charAt(i)] == 0) numDistinct--;
                i++;
            }
            maxLen = Math.max(maxLen, j - i + 1);
        }
        return maxLen;
    }
}
```

---

### 161. One Edit Distance
> 
>> 标签：字符串、指针

---

1. `s`和`t`长度之差大于`1`，返回`False`，先通过交换`s`,`t`保证`len(s) < len(t)`；
2. 第一段匹配方法相同，找到第一个不同的`char`，第一段后如果已经走完`s`，则直接返回，有以下两种情况：
    1. 若`长度之差=0`，说明为两相同string，返回`False`；
    2. 若`长度之差=1`，说明只有最末位不同，返回`True`。
3. 第二段匹配需要根据长度之差做不同处理：
    1. 若`长度之差=0`，则`s`,`t`的index同时+1（同时越过此不同字符），继续比较；
    2. 若`长度之差=1`，则s的index不变，t的index+1（越过需要插入的字符），继续比较；
5. 如果能够匹配完整个`s`，返回`True`，否则说明有两个及以上不同字符or插入点，返回`False`。

```python []
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        i, dif = 0, len(t) - len(s)
        if dif < 0: s, t, dif = t, s, -dif
        if dif > 1: return False # 1.
        while i < len(s) and s[i] == t[i]: i += 1 # 2.
        if i == len(s): return bool(dif)
        if not dif: i += 1 # 3.1
        while i < len(s) and s[i] == t[i + dif]: i += 1 # 3.
        return i == len(s) #5.
```
```java []
class Solution {
    public boolean isOneEditDistance(String s, String t) {
        int dif = t.length() - s.length(), i = 0;
        if (dif < 0) return isOneEditDistance(t, s);
        if (dif > 1) return false;
        while (i < s.length() && s.charAt(i) == t.charAt(i)) i++;
        if (i == s.length()) return dif > 0;
        if (dif == 0) i++;
        while (i < s.length() && s.charAt(i) == t.charAt(i + dif)) i++;
        return i == s.length();
    }
}
```

---

### 163. Missing Ranges
> 
>> 标签：数组，双指针

---

- 使用双指针`low`、`num`，遍历`nums`添加对应范围即可；
- 需要先向`nums`尾部添加`upper + 1`。

```python []
class Solution:
    def findMissingRanges(self, nums: [int], lower: int, upper: int) -> [str]:
        res = []
        low = lower - 1
        nums.append(upper + 1)
        for num in nums:
            dif = num - low
            if dif == 2: res.append(str(low+1))
            elif dif > 2: res.append(str(low+1) + "->" + str(num-1))
            low = num
        return res
```
```java []
class Solution {
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        List<String> res = new ArrayList<>();
        long pre = (long)lower - 1; // prevent 'int' overflow
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] - pre == 2) res.add(String.valueOf(pre + 1));
            else if (nums[i] - pre > 2) res.add((pre + 1) + "->" + (nums[i] - 1));
            pre = nums[i]; // 'int' to 'long'
        }
        if (upper - pre == 1) res.add(String.valueOf(pre + 1));
        else if (upper - pre > 1) res.add((pre + 1) + "->" + upper);
        return res;
    }
}
```

---

### 170. Two Sum III - Data structure design
> 
>> 标签：哈希表Hash

---

- HashMap法：时间复杂度`O(N)`，空间复杂度`O(N)`；
- `add`：在将数字添加进`nums`数组的同时，将数字作为`key`存入`map`，`map`的`value`存此数字在数组的位置；
- `find`：在搜索是否有加和时，遍历整个数组`nums`，判断`value - nums[i]`是否在`map`中：
  - 若在，还需要判断`map[value - nums[i]] == i`，这个是为了排除是否是数组中同一个元素的加和（题意是必须两个不同元素的加和）；因为如果add了两个相同的数字，那么`map[value - nums[i]]`一定大于`i`，因为在`add`操作中每次会刷新此数字的最新index。
  - 若不在，就继续遍历，直至遍历完`nums`。


```python []
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.dic = {}
    

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums.append(number)
        self.dic[number] = len(self.nums) - 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for i in range(len(self.nums)):
            tar = value - self.nums[i]
            if tar in self.dic and self.dic[tar] != i: return True
        return False
```
```java []
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
```

---

### 186. Reverse Words in a String II
> 
>> 标签：字符串

---

- 题意要求空间复杂度O(1)，因此必须要在原数组上直接修改；
- 设倒序操作为`T`，`str = a b c`，则有：
  - `c b a = ( aT bT cT )T`
- 因此，我们只需要将`a`,`b`,`c`分别倒置，再将整个str倒置，即可得到`c b a`。

```python []
class Solution:
    def reverseWords(self, s: [str]) -> None:
        """
        Do not return anything, modify str in-place instead.
        """
        i = 0
        for j in range(len(s)): # aT bT c
            if s[j] != ' ': continue
            self.reverse(s, i, j)
            i = j + 1
        self.reverse(s, i, len(s)) # aT bT cT
        self.reverse(s, 0, len(s)) # c b a
    def reverse(self, s, i, j):
        for k in range(i, (i + j) // 2):
            g = j - 1 - k + i
            s[k], s[g] = s[g], s[k]
```
```java []
class Solution {
    public void reverseWords(char[] str) {
        int i = 0;
        for(int j = 0; j < str.length; j++){ // aTbTc
            if(str[j] != ' ') continue;
            reverse(str, i, j);
            i = j + 1;
        }
        reverse(str, i, str.length); // aTbTcT
        reverse(str, 0, str.length); // cba
    }
    private void reverse(char[] str, int i, int j){
        for(int k = i; k < (i + j) / 2; k++){
            char tmp = str[k];
            int g = j - 1 - k + i;
            str[k] = str[g];
            str[g] = tmp;
        }
    }
}
```

---

### 557. Reverse Words in a String III
> 
>> 标签：字符串，双指针

---

- `left`, `right`双指针通过空格定位每个单词，并翻转每个单词；
- Python可一行。

```python []
class Solution:
    def reverseWords(self, s: str) -> str:
        l = []
        i, left, right = 0, 0, -2
        while i < len(s) + 1:
            if i == len(s) or s[i] == ' ':
                left, right = right + 1, i - 1
                for j in range(right, left, -1):
                    l.append(s[j])
                l.append(' ')
            i += 1
        return "".join(l[:-1])
```
```python[]
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(i[::-1] for i in s.split())
```
```java []
class Solution557 {
    public String reverseWords(String s) {
        String[] strs = s.split(" ");
        StringBuffer res = new StringBuffer("");
        for(String str : strs){
            StringBuffer tmp = new StringBuffer(str);
            res.append(" ");
            res.append(tmp.reverse().toString());
        }
        return res.toString().trim();    
    }
}
```

---

### 
> 
>> 标签：

---



---


## Sword Offer
All 66 problems of 剑指offer are solved using [Python](./swordoffer_python), and the following is the details of [剑指offer全题目解析](https://blog.csdn.net/weixin_42736373/article/details/88934930). To `Ctri + F` the topic of the problems is recommended.

---

### 二维数组的查找
> 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
>> 标签：数组。

---

##### 行列排除法

- 从右上角or左下角开始查找，以左下角开始查找为例，若当前值<目标值，则目标值一定在当前值所在列的右侧，因此列+1；反之将行-1。相当于循环一次就可以排除一列or一行。
- 对于m行n列矩阵，暴力查找时间复杂度O(mn)，以下方法O(m+n)。 

```python
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array)-1
        col = 0
        while row>=0 and col<len(array[0]):
            if target == array[row][col]:
                return True
            elif target > array[row][col]:
                col+=1
            else:
                row-=1
        return False
```

---

### 替换空格
> 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
>> 标签：字符串。

---

- 先遍历确定' '个数，然后从后向前插入（相对于从前向后插入，此方法下每个字符只用被修改一次），对于第count个空格和第count+1空格之间的字符，需要向后移位2*count。

| 1   |   2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  |
| --- | :---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| h   |       | e   | l   | l   |     | o   | w   |     |     |     |     |
| h   |   %   | 2   | 0   | e   | l   | l   | %   | 2   | 0   | o   | w   |

```python
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        l = list(s)
        count = 0
        for k in l:
            if k == ' ':
                count+=1
                l.extend(['1','1'])
        for i in range(len(s)-1,-1,-1):
            if l[i]!=' ':
                l[i+2*count]=l[i]
            else:
                count-=1 
                l[i+2*count]='%'
                l[i+2*count+1]='2'
                l[i+2*count+2]='0'
        return ''.join(l)
```

---

### 从尾到头打印链表
> 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
>> 标签：链表，递归

---

根据题意，使用递归完成。

```python
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        return self.printListFromTailToHead(listNode.next) + [listNode.val] if listNode else []
```

------

### 重建二叉树
> 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
>> 标签：二叉树，深度优先搜索DFS。
------

- 前序遍历： 根节点 | 左子树 | 右子树: [1 | 2 4 5 | 3 6 7]， 中序遍历： 左子树 | 根节点 | 右子树: [4 2 5 | 1 | 6 3 7]

- 因此，可用中序遍历中根节点位置将前序遍历化为三段。对左子树和右子树分别可以进行相同的划分，例如：左子树前序遍历[2 | 4 | 5]和中序遍历[4 | 2 | 5]，递归即可生成树。

- 以下代码中，pre.pop(0)代表此递归对应树的前序遍历，中序遍历list用于辅助确定当前节点的值。

```python
class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if not tin: return
        root = TreeNode(pre.pop(0))
        for i in range(len(tin)):
            if root.val == tin[i]: break
        root.left = self.reConstructBinaryTree(pre, tin[:i])
        root.right = self.reConstructBinaryTree(pre, tin[i+1:])
        return root
```

------

### 用两个栈实现队列
> 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
>> 标签：栈，队列。

------

- 根据题意，需要用两个栈来模拟队列的push和pop，其他例如获取队列内容等不需要考虑。

- 因此，push则向que最后添加node，pop则是将asi中的元素pop，其中asi可理解为que的reverse list。值得注意的是，当asi和que同时为空时应直接返回None。

```python
class Solution:
    def __init__(self):
        self.que, self.asi = [], []
    def push(self, node):
        # write code here
        self.que.append(node)
    def pop(self):
        # return xx
        if not self.asi:
            if not self.que: return
            while self.que:
                self.asi.append(self.que.pop())
        return self.asi.pop()
```

---

### 旋转数组的最小数字
> 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
>> 标签：数组，双指针，二分法。

---

##### 二分法+按顺序搜索

- 旋转排序数组`nums`可以被拆分为2个排序数组`nums1`, `nums2`，并且`nums1`所有元素>=`nums2`所有元素；
- 因此，考虑二分法寻找值`nums[i]`；
- 设置`left`, `right`指针在nums数组两端，`mid`为中点：
  - 当`nums[mid] > nums[right]`时，一定满足`mid < i <= right`，因此`left = mid + 1`；
  - 当`nums[mid] < nums[right]`时，一定满足`left < i <= mid`，因此`right = mid`；
  - 当`nums[mid] == nums[right]`时，是此题对比`153`题的难点（原因是此题中数组的元素`可重复`，相等就难以判断最小值的指针区间）；先说结果：采用`right = right - 1`，下面证明：
    - 首先，此操作`不会使数组越界`，因为`right > left > 0`；
    - 其次，此操作`不会使最小值丢失`，证明：假设'nums[right]'是最小值，有两种情况：
        - 若`nums[right]`是唯一最小值：那就不可能满足判断条件`nums[mid] == nums[right]`，因为`left != right`且`mid = left + right // 2  < right`（向下取整）；
        - 若有其他元素和`nums[right]`同为最小值：还有最小值存在于`[left, right -1]`间，不会丢失最小值。
- 以上是理论分析，可以用以下数组辅助思考：
  - `[1, 2, 3]`
  - `[1, 1, 0, 1]`
  - `[1, 0, 1, 1, 1]`
  - `[1, 1, 1, 1]`

```python
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, nums):
        # write code here
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: left = mid + 1
            elif nums[mid] < nums[right]: right = mid
            else: right = right - 1 # key
        return nums[left]
```

------

### 斐波那契数列
> 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
>> 标签：迭代。

---

```python
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, a + b
        return b if n > 0 else 0
```

------

### 跳台阶
> 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
>> 标签：动态规划。

---

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

##### 动态规划，斐波那契数列

发现台阶跳法规律，f(n)=f(n-1)+f(n-2)，是斐波那契数列（详细解析同理于矩形覆盖）。

```python
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return number
        a=0
        b=1
        for _ in range(number):
            a,b = b,a+b
        return b
```

------

### 变态跳台阶
> 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
>> 标签：找规律。

---

看起来很变态，其实和跳台阶思路差不多，先找f(n)和f(n-1)....f(1)的关系，再由前面的项相加即可，对于n级台阶：

| 先跳 | 后面可能性 |
| ---- | ---------- |
| 1    | f(n-1)     |
| 2    | f(n-2)     |
| ...  | ...        |
| n-1  | 1          |
| n    | 1          |

如果用迭代做，重复计算太多了，因此考虑继续分解：

| f(x) | =                                          |
| ---- | ------------------------------------------ |
| f(0) | = 1                                        |
| f(1) | = 1                                        |
| f(2) | = f(0) + f(1)                              |
| f(3) | = f(0) + f(1) + f(2) = 2[f(0)+f(1)]        |
| f(4) | = f(0) + f(1) + f(2) + f(3) = 4[f(0)+f(1)] |
| ...  | = ...                                      |
| f(n) | = 2f(n-1) = 2^n-2 * [f(0)+f(1)]            |

因此， f(n) = 2^n-1.

```python
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 2 ** (number - 1) # or pow(2, number - 1)
```

------

### 矩形覆盖
> 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
>> 标签：动态规划。

---

##### 其实是斐波那契数列

设n个矩形有f(n)种放法，则将一个矩形如下放置，剩下矩形有f(n-1)种放法。

| 1   | 2   | ... | n   |
| --- | --- | --- | --- |
| √   |     |     |     |
| √   |     |     |     |

则将一个矩形如下放置，剩下矩形有f(n-2)种放法，因为还有一个矩形必须放在×的位置，即有两个矩形固定。

| 1   | 2   | ... | n   |
| --- | --- | --- | --- |
| √   | √   |     |     |
| ×   | ×   |     |     |

因此，f(n)=f(n-1)+f(n-2)，是斐波那契数列。

```python
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0 or number == 1:
            return number
        a=0
        b=1
        for _ in range(number):
            a,b = b,a+b
        return b
```

------

### 二进制数中1的个数
> 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
>> 标签：位运算。

---

```python
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        n &= 0xffffffff
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
```

###### 以下理解不知正确与否：

- python存取一个数，长度是无限制的（和java等不同，int是32位的）。当存储负数时，python会符号位前也有无限个1。例如，java中-1是以补码0xffffffff，但在python中0xffffffff前还有fffff……，因此对于负数无法直接求1的个数，会陷入死循环。

- 对于负数，需要做预先处理，即n &= 0xffffffff，这个即是n与0xffffffff求交，输出负数n的无符号形式（负号前面的1全部变为0，因此变成了正数，负号的1变为此正数的最高位）

```python
print(hex(1)) #0x1
print(hex(-1)) #-0x1 = 0xffffffff（补码，二进制第一位是符号位，前面还有无限个1）
print(hex(1& 0xffffffff)) #0x1 = 0x00000001
print(hex(-1& 0xffffffff)) #0xffffffff，相当于把前面无限个1变为0，从符号位至最后一位保持不变，但符号位的1被提出到与其他位等价。
print(-1& 0xffffffff) #4294967295 = 2^32-1 = -1的无符号形式
```
---

### 数值的整数次方
> 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
>> 标签：快速幂法。

---

##### 快速幂法：

- 原始情况下， b ^ e = b * b * ... * b，可以分解成e个b的乘积，需要做e-1次乘法运算，效率很低。
- 然而我们发现 b ^ e = b ^ (1 + 2 + 4 + ... + 2n)，所有的e都可以分解成此数列，其本质上是一个数的二进制表示，如3 = 0011 = 1 + 2, 5 = 0101 = 1 + 4, 9 = 1001 = 1 + 8..
- 这样我们存储 b ^ 1, b ^ 2 , b ^ 4 ... （即 base = base * base），通过 exp & 1 == 0 （判断exp最右位是否为1）来判断数字此位是否需要相乘，最终把相乘结果输出即可。

```python
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        res, exp = 1, abs(exponent)
        while exp != 0:
            if exp & 1 != 0: res *= base
            base *= base
            exp >>= 1
        return res if exponent > 0 else 1/res
```
---

### 调整数组顺序使奇数位于偶数前面
> 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
>> 标签：数组，位运算。

---

空间换时间，借用两个辅助数组分别填入奇数偶数并返回，时间空间复杂度均为O(N)。
```python
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd, even = [], []
        for a in array:
            odd.append(a) if a & 1 else even.append(a)
        return odd + even
```

---

### 链表中倒数第k个结点
> 输入一个链表，输出该链表中倒数第k个结点。
>> 标签：链表，双指针。

---

声明两个指针n1, n2，指针n1先向前走k1步，找到链表第k+1个node，然后指针n1，n2一起走，当n2走过最后一个node时（指向None），n1即是倒数第k个node
```python
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        node1, node2 = head, head
        for _ in range(k):
            if not node1: return
            node1 = node1.next
        while node1:
            node1, node2 = node1.next, node2.next
        return node2
```
---

### 反转链表
> 输入一个链表，反转链表后，输出新链表的表头。
>> 标签：链表，三指针。

---

遍历链表，每次记录上次遍历点pre，三个指针交替向前行进。

```python
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        cur, pre = pHead, None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre
```

---

### 合并两个排序链表
> 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
>> 标签：链表，双指针。

---

借用一个链表头tmp，按照大小依次将head1，head2链表加入排序，最后将剩余部分加到链表尾部，返回tmp.next
```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        tmp = ListNode(0)
        head = tmp
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                tmp.next, pHead1 = pHead1, pHead1.next
            else:
                tmp.next, pHead2 = pHead2, pHead2.next
            tmp = tmp.next
        tmp.next = pHead2 if not pHead1 else pHead1
        return head.next
```

---

### 树的子结构
> 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
>> 标签：二叉树、递归、深度优先搜索。

---

- 先找到子树根节点value = 父树根节点value的节点；
- 判断以此节点为根节点时，是否是子结构（r2为空则代表是子结构）；
- 遍历pRoot1，方可确定是否为子结构。

```python
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2: return False
        return self.is_subtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def is_subtree(self, r1, r2):
        if not r2: return True
        if not r1 or r1.val != r2.val: return False
        return self.is_subtree(r1.left, r2.left) and self.is_subtree(r1.right, r2.right)
```
---

### 二叉树的镜像
> 操作给定的二叉树，将其变换为源二叉树的镜像。
>> 标签：二叉树，递归，深度优先搜索。

---

镜像则是将整个树从上至下将每个根节点的左右子节点互换，因此使用递归即可。
```python
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root: return
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root
```
---

### 顺时针打印矩阵
> 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
>> 标签：记忆化。

---

旋转法：弹出并打印矩阵第一行内容，矩阵逆时针旋转90°，弹出并打印矩阵第一行内容……
需要将逆时针旋转矩阵的公式推导出来。

```python
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = matrix.pop(0)
        while matrix:
            matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0])-1, -1, -1)]
            res += matrix.pop(0)
        return res
```

设定边界法:

```python
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix: return []
        res = []
        h, l = len(matrix), len(matrix[0])
        i, j = 0, -1
        while True:
            for _ in range(l):
                j += 1
                res.append(matrix[i][j])
            h -= 1
            if not h: break
            for _ in range(h):
                i += 1
                res.append(matrix[i][j])
            l -= 1
            if not l: break
            for _ in range(l):
                j -= 1
                res.append(matrix[i][j])
            h -= 1
            if not h: break
            for _ in range(h):
                i -= 1
                res.append(matrix[i][j])
            l -= 1
            if not l: break
        return res
```

---

### 包含min函数的栈
> 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
>> 标签：栈，设计。

---

- 题目要求min函数的时间复杂度O(1)，所以需要在push，pop这些方法中动态更新栈最小值的情况；

- 构造辅助m_stack，当push的值小于等于目前最小值的时候，就将此值入m_stack，相当于给stack中按照栈底到栈顶的顺序给最小值打上标记。值得注意的是，条件是小于等于，这样才可以处理最小值有两个及以上的情况。当出栈时，若出栈元素等于最小值，m_stack则将此元素标记取消；

- min函数则返回m_stack栈顶元素即可。

```python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.m_stack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.m_stack or self.m_stack[-1] >= node:
            self.m_stack.append(node)
    def pop(self):
        # write code here
        if self.stack.pop() == self.m_stack[-1]:
            self.m_stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.m_stack[-1]
```

---

### 栈的压入、弹出序列
> 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）。
>> 标签：栈，模拟。

------

- 这道题主要需理解题目的意思。题目意思是来了一串数据，在不违背栈先入后出的原则下随意push和pop，然后问push序列和pop序列是否可行。

- 例如对于数据流1,2,3,4,5，先push三个数据[1,2,3]，然后pop两个数据[3, 2]，然后push两个数据[4,5]，再pop三个数据[5,4,1]，因此总的push和pop顺序就是[1,2,3,4,5]和[3,2,5,4,1]。但像[2,5,3,4,1]就不可能，因为若先pop5，那么3就不可能在4前pop。

- 解题思路是创建一个栈，模拟这个过程，根据模拟成功结果返回。

```python
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        imi = [pushV.pop(0)]
        while imi:
            cur = popV.pop(0)
            while imi[-1] != cur:
                if not pushV: return False
                imi.append(pushV.pop(0))
            imi.pop()
        return True
```

------

### 从上往下打印二叉树
> 从上往下打印出二叉树的每个节点，同层节点从左至右打印。
>> 标签：二叉树，广度优先遍历BFS。

------

按层打印使用迭代。思路是tmp存储每层节点，通过此层节点获取下层节点（同时保存val至res），并循环直到tmp为空。

```python
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root: return []
        res, tmp = [], [root]
        while tmp:
            t = tmp.pop(0)
            res.append(t.val)
            if t.left: tmp.append(t.left)
            if t.right: tmp.append(t.right)
        return res
```

------

### 二叉搜索树的后序遍历序列
> 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
>> 标签：二叉搜索树BST，深度优先搜索DFS，后序遍历。

------

- 二叉搜索树的性质是左子树节点都比根节点值小，右子树节点都比根节点值大。
- 根据这个定义，考虑后序遍历序列可以划分为[左子树（小）| 右子树（大）| 根节点]，通过对每棵子树拆分，可以判定是否满足二叉搜索树的性质。
- 递归遍历整个树，若发现某子树不满足此规律则返回False。

```python
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        return self.verify(sequence) if sequence else False
    def verify(self, sequence):
        if not sequence: return True
        for i in range(len(sequence)):
            if sequence[i] >= sequence[-1]: break
        for j in range(i, len(sequence)-1):
            if sequence[j] <= sequence[-1]: return False
        return self.verify(sequence[:i]) and self.verify(sequence[i+1:-1])
```

------

### 二叉树中和为某一值的路径
> 输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
>> 标签：二叉树，深度优先搜索DFS，记忆化。

------

- 先序遍历递归，过程中累计target值并记录path；

- 若到达叶子节点，且刚好累计到target值，则将路径添加到res里；

- 递归返回到父节点时，path要弹出当前节点。

```python
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        self.res, self.path = [], []
        self.search(root, expectNumber)
        return self.res
    def search(self, root, target):
        if not root or target < 0: return
        target -= root.val
        self.path.append(root.val)
        if not (root.left or root.right or target):
            self.res.append(list(self.path))
        self.search(root.left, target)
        self.search(root.right, target)
        self.path.pop()
```

------

### 复杂链表的复制
> 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）。
>> 标签：链表。

------

此链表复杂在有random项，即在复制时不止需要考虑next的顺序问题，还要找到每个节点random的对应节点。

三步法：
- 链表[h1, h2, ...]，复制链表[g1, g2, ...]，并将其交叉合并为[h1, g1, h2, g2, ...]，获得关系h1.random.next = h1.next.random；
- 根据以上关系，将random属性一一对应起来；
- 将合并链表拆分为两个单独链表，获得[g1,g2,...]并返回。

```python
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, head):
        # write code here
        if not head: return
        h = head
        while h:
            tmp = RandomListNode(h.label)
            nex = h.next
            h.next, h, tmp.next = tmp, nex, nex
        h = head
        while h.next.next:
            if h.random: h.next.random = h.random.next
            h = h.next.next
        h, res = head, head.next
        while h.next:
            tmp = h.next
            h.next, h = h.next.next, tmp
        return res
```

------

### 二叉搜索树与双向链表
> 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
>> 标签：二叉搜索树BST，中序遍历。

------

- 二叉搜索树的中序遍历即是排序list；
- 使用递归中序遍历，在递归过程中记录上一个节点pre，修改pre.right和root.left的指针指向；
- 返回中序遍历的第一个节点。

```python
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        self.pre = TreeNode(0)
        res = self.pre
        self.traversal(pRootOfTree)
        if res.right: res.right.left = None
        return res.right
    def traversal(self, root):
        if not root: return
        self.traversal(root.left)
        self.pre.right = root
        root.left = self.pre
        self.pre = root
        self.traversal(root.right)
```

------

### 字符串的排列
> 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
>> 标签：字符串，递归，排序。

------

- 使用递归解决，固定第1个字符，求后面n-1字符的组合。例如abc固定a，有bc和cb两种组合。
- 将第1个字符和后面n-1个字符分别交换，再递归。例如abc有bac，cba两种变化。
- 对于相同字符不做交换（因为交换后情况重复）。例如aab，则只用求aab和baa两种情况下组合。

```python
# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        self.res, self.sort = [], list(ss)
        self.sort_dic(0, len(ss))
        self.res.sort()
        return self.res
    def sort_dic(self, s, e):
        if e - s == 1: self.res.append(''.join(self.sort))
        same = {}
        for i in range(s, e):
            if self.sort[i] in same: continue
            same[self.sort[i]] = 1
            self.sort[s], self.sort[i] = self.sort[i], self.sort[s]
            self.sort_dic(s+1, e)
            self.sort[s], self.sort[i] = self.sort[i], self.sort[s]
```

------

### 数组中出现次数超过一半的数字
> 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
>> 标签：数组，哈希表Hash。

------

- 循环找出list中不同的2个数字删除，若有数字占数组长度一半以上，则留下的一定是此数字（最坏情况下，此数字也不可能被全部删除）；
- 利用此推断，模拟删除，复杂度O(N)；
- 得到留下的数字，再遍历一遍list，确认此数字数量超过list长度一半，复杂度O(N)。
- 也可以用HashMap做，时间空间复杂度都为O(N)。

```python
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        tmp = list(numbers) # copy the list
        i = 1
        while i < len(tmp):
            if tmp[0] == tmp[i]:
                i += 1
            else:
                del tmp[0], tmp[i-1]
                i = 1
        if not tmp: return 0
        count = 0
        for num in numbers:
            if num == tmp[0]: count += 2
        return tmp[0] if count > len(numbers) else 0
```

------

### 最小的K个数
> 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
>> 标签：数组，排序，堆。

------

- 使用`heapq + 负数`模拟大顶堆：
  - 先向大顶堆添加`tinput`数组前`k`个数；
  - 后面的数，若`n < heap[0]（堆顶）`，从堆`pop()`最大值，并将`n`值`push（）`入堆；
  - 最后，将堆中值都`pop()`出`res`，并倒置`res`返回。

```python
import heapq
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not k or k > len(tinput): return []
        heap, res = [], []
        for n in tinput:
            if len(heap) < k:
                heapq.heappush(heap, -n)
            elif -n > heap[0]:
                heapq.heappush(heap, -n)
                heapq.heappop(heap)
        while heap:
            res.append(-heapq.heappop(heap))
        res.reverse()
        return res
```

------

### 连续子数组的最大和
> HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
>> 标签：数组，动态规划。

------

- 使用动态规划，遍历一遍list，记录累加值；
- 当遍历到第i项时，舍弃前面累积的条件为上次累计值为负值；
- 例如：array = [1, -2, 3, 10, -4, 7, 2, -5]， tmp = [1, -1, **3**, 13, 9, 16, 18, 13]，舍弃前面累计值-1，直接选取array对应值3。

```python
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        tmp = [array[0]]
        for i in range(1, len(array)):
            tmp += [array[i]] if tmp[i-1] < 0 else [array[i] + tmp[i-1]]
        return max(tmp)
```

------

### 整数中1出现的次数（从1到n整数中1出现的次数）
> 求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
>> 标签：找规律。

------

| range | num                     |
| ----- | ----------------------- |
| 0-9   | 1                       |
| 0-99  | 10+10 = 1 * 10 + 10     |
| 0-999 | 200 + 100 = 20*10 + 100 |

- 根据以上规律可以推出各数位对应1出现次数的关系，例如1136 = 1000 + 100 + 30 + 6，分别算出各项1出现的次数相加即可；
- 需要区分的是当前数位是否为1。若为1，则需要加上低位的数字。例如136，百位1对应的1出现次数为20(0-99) + 37(100-136) = 57。

```python
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        total, deno, count, end = 0, 1, 0, 0
        while n != 0:
            num = n % (deno * 10)
            n -= num
            if num > deno:
                count += total * num / deno + deno
            elif num == deno:
                count += total + 1 + end
            total = total*10 + deno
            end += num
            deno *= 10
        return int(count)
```

------

### 把数组排成最小的数
> 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
>> 标签：思维拓展。

------

- 这道题如果换成[2,1,3,5,8,4]，让排序出最小组合，是不是就很简单了？但对于题目中[32,3,321]，仅仅考虑数字之间大小难以解决。但仔细想想，本质上，题目是要寻找列表中每个元素的“大小关系”，对整个list进行排序。
- 对于[2,1,3,5,8,4]来说，2 > 1 因此2应该在1右边，这是十进制的特性决定的。对于[32,3,321]，我们把每个列表元素当作整体看待，元素的“大小”比较等价于`"32" + "3" = “323” < “332” = "3" + "32"`，即比较两元素在两种拼接方案后的大小。
- 自写一个比较函数`compare()`，然后选择一种效率高的排序方法将整个list按照此规则进行排序即可。

```python
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        self.quick_sort(numbers, 0, len(numbers)-1)
        return "".join([str(num) for num in numbers])

    def quick_sort(self, arr, l, r):
        if l > r: return
        base, i, j = arr[l], l, r
        while i != j:
            while self.compare(arr[j], base) and i < j: j -= 1
            while self.compare(base, arr[i]) and i < j: i += 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[l], arr[i] = arr[i], arr[l]
        self.quick_sort(arr, l, i-1)
        self.quick_sort(arr, i+1, r)

    def compare(self, a, b):
        str1, str2 = str(a) + str(b), str(b) + str(a)
        return 0 if str1 < str2 else 1
```

------

### 丑数
> 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
>> 标签：多指针。

------

- 任何一个丑数n可以写作 n = 2x or 3y or 5z，即其中至少有2，3，5因子中的其中一个；

- 找到了丑数数列生成规律，在丑数数列中res设置三个指针t2, t3, t5，每次比较三指针生成的下个数字大小，取最小值为下个丑数；

- 某些生成轮会有指针生成值重合现象，此时生成值相同的指针都需要+=1，例如下情况：下个丑数为6，res[t2] * 2 = res[t3] * 2 = 6，则两指针都要+=1。

  | 1   | 2   | 3   | 4   | 5   | <u>**6**</u> |
  | --- | --- | --- | --- | --- | ------------ |
  |     |     | t2  |     |     |              |
  |     | t3  |     |     |     |              |
  |     | t5  |     |     |     |              |

```python
# -*- coding:utf-8 -*-class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 7: return index
        t2 = t3 = t5 = 0
        res = [1]
        for i in range(1,index):
            r2, r3, r5 = res[t2] * 2, res[t3] * 3, res[t5] * 5
            res.append(min([r2, r3, r5])) 
            if res[i] == r2: t2 += 1
            if res[i] == r3: t3 += 1
            if res[i] == r5: t5 += 1
        return res[-1]
```

------

### 第一个只出现一次的字符
> 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）。
>> 标签：哈希表Hash。

------

- 题目中没有说list中有几个只出现一次的字符，因此不能用异或等运算性质解决；
- 建立一个Hash table，长度为字母'A'至'Z'的ASCII码之差；
- 先遍历一遍list，在`HashMap`中记录每个字符的出现次数；
- 再遍历list，在`HashMap`中按list顺序查询字符出现数量，返回第一个数量为1的字符。

```python
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s): 
        # write code here
        dic = {}
        for c in s:
            if c in dic: dic[c] += 1
            else: dic[c] = 1
        for i in range(len(s)):
            if dic[s[i]] == 1: return i
        return -1
```

------

### 数组中的逆序对
> 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
>> 标签：二分法，归并排序，回溯算法。

------

- 使用冒泡/插入排序可以记录排序过程中的操作数量，此操作数量即为逆序对数量，但复杂度为O(N^2)；

- 使用归并排序可以将复杂度降至O(N log2 N)，需要解决的是如何在归并排序中统计逆序对数量；

- 归并排序下list像递归二叉树一样被展开，从下至上依次统计count。

  |     |      |     | 53421687 |     |      |     |
  | --- | ---- | --- | -------- | --- | ---- | --- |
  |     | 5342 |     |          |     | 1687 |     |
  | 53  |      | 42  |          | 16  |      | 87  |

```python
# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        self.arr, self.count = data, 0
        self.merge_sort(0, len(data)-1)
        return self.count % 1000000007
    def merge_sort(self, l, r):
        if l >= r: return
        m = int((l+r+1)/2)
        self.merge_sort(l, m-1)
        self.merge_sort(m, r)
        i, j, merge = l, m, []
        while i < m and j <= r:
            if self.arr[i] < self.arr[j]:
                merge.append(self.arr[i])
                i += 1
            else:
                merge.append(self.arr[j])
                j += 1
                self.count += m - i
        for x in range(j,r+1): merge.append(self.arr[x])
        for x in range(i,m): merge.append(self.arr[x])
        for i in range(l, r+1): self.arr[i] = merge[i-l]
```

------

### 两个链表的第一个公共结点
> 输入两个链表，找出它们的第一个公共结点。
>> 标签：链表，双指针。

------

- 若两个链表有公共节点，那么其一定有公共的尾部（公共结点后的所有节点一致）；
- 先分别统计两个链表的长度，得到两链表的长度差k；
- 长链表指针先走k-1步，之后两指针一起走，直到寻找到相同结点return

```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        length1 = length2 = 0
        head1, head2 = pHead1, pHead2
        while head1:
            head1 = head1.next
            length1 += 1
        while head2:
            head2 = head2.next
            length2 += 1
        [k, lon, sho] = [length1 - length2, pHead1, pHead2] if length1 > length2 else [length2 - length1, pHead2, pHead1]
        for _ in range(k):
            lon = lon.next
        while lon:
            if lon == sho: return lon
            lon, sho = lon.next, sho.next
```

------

### 数字在排序数组中出现的次数
> 统计一个数字在排序数组中出现的次数。
>> 标签：数组，二分法，二分插入。

------

- 直接遍历list统计次数，时间复杂度O(N)；
- 使用二分法，寻找k - 0.1和k + 0.1的插入点，时间复杂度O(log2 N)。

```python
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return self.findLocation(data, k + 0.1) - self.findLocation(data, k - 0.1)

    def findLocation(self, data, k):
        left, right = 0, len(data) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if data[mid] > k: right = mid - 1
            else: left = mid + 1
        return left
```

------

### 二叉树的深度
> 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
>> 标签：二叉树，深度优先遍历DFS，回溯算法。

------

- 统计深度要遍历所有节点，统计所有叶子节点到根节点的最大值；
- 和按层遍历类似，每遍历一层就将depth += 1，直到最后一层结束并返回。

```python
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot: return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
```

------

### 平衡二叉树
> 输入一棵二叉树，判断该二叉树是否是平衡二叉树。
>> 标签：平衡二叉树，深度优先搜索DFS，回溯法。

------

- 递归遍历整个树，判断左右子树深度差是否大于1；
- 叶节点返回1；返回根节点时，判断左子树和右子树深度差是否大于1，若大于则返回-1；
- 若已经发现返回-1的子树，则说明不是平衡二叉树，一路返回-1。

```python
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return self.getDepth(pRoot) != -1
    def getDepth(self, pRoot):
        if not pRoot: return 0
        dl = self.getDepth(pRoot.left)
        dr = self.getDepth(pRoot.right)
        return max(dl,dr) + 1 if dl != -1 and dr != -1 and -2 < dl - dr < 2 else -1
```

------

### 数组中只出现一次的数字
> 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
>> 标签：数组，位运算。

------

- 根据异或性质，对于任何数字a，a ^ a = 0， a ^ 0 = a，并且异或满足交换律；因此，若一个list里只有1个出现1次的数字，其余都出现2次，我们将list从头到尾依次执行异或操作，结果一定是那个只出现1次的数字；
- 根据以上性质，自然想到如何把此数组切分成两个数组，其中出现一次的数字a, b分别分布在两个数组中，这样就可以按照此性质来求得a, b；
- 先对list从头到尾异或，得到的结果是num_xor = a ^ b，对num_xor的二进制形式遍历，找到一个为1的数位。这个1代表a, b在这个对应数位上的数字不同。接下来按照这个数位为1和为0将list划分，则a, b就被划分到两个list里了，并且出现了两次的数字也被按对划分到两个list里。

```python
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        num_xor = array[0]
        for a in array[1:]:
            num_xor ^= a
        index = 0
        while num_xor & 1 != 1:
            num_xor >>= 1
            index += 1
        n0, n1 = 0, 0
        for a in array:
            if a >> index & 1: n0 ^= a
            else: n1 ^= a
        return [n0,n1]
```

------

### 和为S的连续正数序列
> 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
>> 标签：数组，双指针。

------

- 设定两个指针，从1, 2出发，通过判断总和与目标值大小关系移动指针；
- 当等于时，添加list至res，由于是从1,2出发，因此先添加进去的list一定最长（数字较小）；
- 为避免反复计算，总和s随着指针移动动态计算。

```python
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res, l, r, s = [], 1, 2, 3
        while l < r:
            if s >= tsum: 
                if s == tsum: res.append(list(range(l,r+1)))
                s -= l
                l += 1
            else: 
                r += 1
                s += r
        return res
```

------

### 和为S的两个数字
> 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
>> 标签：数组，双指针。

------

- 仍然是双指针法，指针先设在list两端，根据与目标值的比较逐渐向中间逼近；
- 当找到第一个结果时返回，即是乘积最小的结果，因为指针是从两段向中间逼近的（周长相等，长宽差距越大面积越小）。

```python
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        l, r = 0, len(array) - 1
        while l < r:
            if array[l] + array[r] < tsum: l += 1
            elif array[l] + array[r] > tsum: r -= 1
            else: return [array[l], array[r]]
        return []
```

------

### 左旋转字符串
> 汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
>> 标签：字符串，时间换空间。

------

- 设对于一个字符串x，其转置记为xT；则(yx)T = xT yT；
- 根据以上性质，yx = (xT yT)T，即做三次翻转即可。

```python
# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        res, length = list(s), len(s)
        if n > length : return ""
        for i in range(int(n/2)):
            res[i], res[n-1-i] = res[n-1-i], res[i]
        for i in range(n, int((n+length)/2)):
            res[i], res[length-1-i+n] = res[length-1-i+n], res[i]
        for i in range(int(length/2)):
            res[i], res[length-1-i] = res[length-1-i], res[i]
        return "".join(res)
```

------

### 翻转单词顺序列
> 牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
>> 标签：字符串，时间换空间。

------

- 和上题类似，若不借用额外空间，abcd = (dT cT bT aT)T。

```python
# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        res, length, last = list(s), len(s), -1
        for i in range(len(res)):
            if res[i] == ' ': 
                self.reverse(res, last + 1, i)
                last = i
        self.reverse(res, 0, length)
        return "".join(res)

    def reverse(self, res, l, r):
        while l < r:
            res[l], res[r-1] = res[r-1], res[l]
            l += 1
            r -= 1
```

------

### 扑克牌顺子
> LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。
>> 标签：模拟。

------

- 先排序，统计王joker的数量；
- 在剩下的牌中计算需要多少王可以填充，若王全部用完或出现对子，则返回False。

```python
# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        numbers.sort()
        joker = 0
        for n in numbers[:4]:
            if not n: joker += 1
        for i in range(joker, len(numbers) - 1):
            tmp = numbers[i+1] - numbers[i] - 1
            joker -= tmp
            if joker < 0 or tmp < 0: return False
        return True if numbers else False
```

------

### 孩子们的游戏(圆圈中最后剩下的数)
> 每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)。
>> 标签：模拟。

------

- 纯模拟这个过程。

```python
# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not n: return -1
        res = list(range(n))
        length, index = len(res), 0
        while length > 1:
            index = (index + m - 1) % length
            res.pop(index)
            length = len(res)
        return res[0]
```

------

### 求1+2+3+...+n
> 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
>> 标签：发散思维，熔断机制。

------

- 使用递归计算n+n-1+...+1，使用and的阻断性质实现递归终止条件。

```python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.sum = 0
    def Sum_Solution(self, n):
        # write code here
        n and self.Sum_Solution(n-1)
        self.sum += n
        return self.sum
```

------

### 不用加减乘除做加法
> 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
>> 标签：位运算。

------

- 对于a + b,  a ^ b异或相当于不算进位地将ab相加，如0011 ^ 0101 = 0110
- a & b << 1 相当于计算了a + b产生的进位，如 0011 & 0101 << 1 = 0001 << 1 = 0010
- 循环计算，直到进位项为0；
- 由于python长整数可以表示无限位，因此需要人工& 0xFFFFFFFF设置边界判断；
- 结果num1是无符号数，和0x7FFFFFFF作比较判断数字正负，若为负则求反码再转原码。

```python
# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            num1, num2 = (num1 ^ num2) & 0xFFFFFFFF, (num1 & num2) << 1 & 0xFFFFFFFF
        return num1 if num1 <= 0x7FFFFFFF else ~(num1 ^ 0xFFFFFFFF)
```

------

### 把字符串转换成整数
> 将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
>> 标签：字符串。

------

- 提取字符串每位依次添加进数字res；
- 遇非数字字符返回0；
- 判断首位是否是符号+ -，返回对应正负数。

```python
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here 
        if not s: return 0
        res, bit = 0, 1
        end = -1 if s[0] != '+' and s[0] != '-' else 0
        for i in range(len(s)-1, end, -1):
            num = ord(s[i]) - 48
            if num > 9 or num < 0: return 0
            res += num * bit
            bit *= 10
        return -res if s[0] == "-" else res
```

------

### 数组中重复的数字
> 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
>> 标签：哈希表Hash。

------

- 建立长度为n的hash table，用于存储每个数字的出现次数；
- 遇到第一个出现两个的数字，记录并返回True。

```python
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        table = [0 for _ in range(len(numbers))]
        for n in numbers:
            if table[n] > 0:
                duplication[0] = n
                return True
            table[n] += 1
        return False
```

------

### 构建乘积数组
> 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
>> 标签：

------

- 根据以下矩阵规律，先算下三角，再算上三角；

|      |      |      |     |      |
| ---- | ---- | ---- | --- | ---- |
| B[0] | 1    | A[1] | ... | A[N] |
| B[1] | A[0] | 1    | ... | A[N] |
| ...  | A[0] | A[1] | ... | A[N] |
| B[N] | A[0] | A[1] | ... | 1    |

```python
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B, tmp = [1], 1
        for i in range(len(A)-1):
            B.append(B[i]*A[i])
        for i in range(len(A)-1, 0, -1):
            tmp *= A[i]
            B[i-1] *= tmp
        return B
```

------

### 正则表达式匹配
> 请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配。
>> 标签：字符串，正则。

------

- 基本思路是按位匹配，但 * 较难处理，因为其前面的字符可以为任意数量（包括0），所以就会有多种情况。
- 例如：a a a和a * a匹配，* 前面的a出现两次正好匹配，但如果一直遍历a出现三次，则反而匹配失败。
- 根据以上案例，自然会想到return情况1 or 情况2的递归模式，这样只要匹配成功一种，就会返回True；
- 设s, p指针分别为i, j，按照p[j+1]是否为‘*’来分成两种情况：
  - 不为*比较简单：
    - 若s[i]等于p[j]或p[j]为‘.'，则两指针同时+1继续递归；
    - 否则匹配失败，返回False；
  - 为*分成两种情况：
    - 若s[i]等于p[j]或p[j]为‘.'，说明此*前字符至少出现一次，则递归i+1 or j+2；
    - 否则，说明*前的字符出现0次，j+2递归。
- 中止条件为：两指针同时走过末尾则匹配成功，若j单独走过末尾则匹配失败（匹配字符串已经遍历完毕，无法继续匹配）。
```python
# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        return self.match_str(s, pattern, 0, 0)

    def match_str(self, s, p, i, j):
        ls, lp = len(s), len(p)
        if not j < lp:
            if not i < ls: return True
            return False
        if j+1 < lp and p[j+1] == '*':
            if i < ls and (s[i] == p[j] or p[j] == '.'):
                return self.match_str(s, p, i+1, j) or self.match_str(s, p, i, j+2)
            return self.match_str(s, p, i, j+2)
        if i < ls and (s[i] == p[j] or p[j] == '.'):
            return self.match_str(s, p, i+1, j+1)
        return False
```

------

### 表示数值的字符串
> 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
>> 标签：字符串，问题分解。

------

- 首位字符必须为+或-或数字；
- 在e(E)之前，匹配数字or小数点；
- 在e(E)之后，首位匹配+或-或数字，后面匹配数字。
```python
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        ls, i, dot = len(s), 1, 0
        # 首位必须为“+/-/number”
        if s[0] != '+' and s[0] != '-' and (s[0] < '0' or s[0] > '9'): return False
        # 遍历1~(len-1)位，如果发现E or e就跳到下一个while
        while i < ls - 1:
            if s[i] == 'E' or s[i] == 'e':
                i += 1
                break
            elif s[i] == '.':
                if dot: return False
                dot += 1
            elif s[i] < '0' or s[i] > '9': return False
            i += 1
        # e后面首位必须为“+/-/number”
        if s[i] != '+' and s[i] != '-' and (s[i] < '0' or s[i] > '9'): return False
        i += 1
        # e不能出现两次，并且e后面的数字组合不能有小数点，其余和前面一样
        while i < ls:
            if s[i] < '0' or s[i] > '9': return False
            i += 1
        return True
```

------

### 字符流中第一个不重复的字符
> 请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
>> 标签：哈希表Hash，设计。

------

- 建立长度为256的hash table，用于统计字符出现次数。

```python
# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.dic = {}

    def FirstAppearingOnce(self):
        # write code here
        for c in self.s:
            if self.dic[c] == 1: return c
        return '#'

    def Insert(self, char):
        # write code here
        self.s += char
        if char in self.dic: self.dic[char] += 1
        else: self.dic[char] = 1

```

------

### 链表中环的入口结点
> 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
>> 标签：链表，双指针。

------

- 使用两个指针，p1步长为1，p2步长为2，同时出头结点出发一起向前走，则走k步后p1、p2相差距离为k；当p1和p2第一次重合时，p2比p1多走了一个环的周长；
- 声明两指针p1、p2在头结点，p1先走环周长的步数，然后两个节点一起向前走，下次两节点重合位置一定是环的入口节点。

```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here 
        p1, p2, step= pHead, pHead, 0
        while p1 != p2 or step == 0:
            if not p1.next or not p2.next.next: return None
            p1, p2 = p1.next, p2.next.next
            step += 1
        p1, p2 = pHead, pHead
        for _ in range(step):
            p1 = p1.next
        while p1 != p2:
            p1, p2 = p1.next, p2.next
        return p1
```

------

### 删除链表中重复的结点
> 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
>> 标签：链表，双指针。

------

- 基本思路是创建两指针h1, h2确定list中只出现一次的数字，并将这些数字链起来；
- 指针的设定和边界的处理是此题关键：
  - 设pre指针指向只出现一次的数字，当找到下一个只出现一次的数字时pre指针移动；
  - h1指向每个数字第一次出现的位置，h2指针循环前进直到找到h1 != h2的第一个数字；
  - 遇到几组连续出现的数字时，不要修改pre指针。
- 添加一个节点至头节点前，以处理左方越界问题；
- 在返回前，最后一个pre需置为None，以处理右方越界问题。
- 例如：以下是pre = 2时各指针位置。

| 1   | 1   | 2   | 3      | 4   | 4   |
| --- | --- | --- | ------ | --- | --- |
|     |     | pre | n1,tmp | n2  |     |

```python
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead: return
        pre, h1, h2 = ListNode(pHead.val - 1), pHead, pHead
        res, pre.next = pre, h2
        while h2:
            while h2 and h1.val == h2.val:
                tmp, h2 = h2, h2.next
            if tmp == h1: pre.next, pre = tmp, h1
            h1 = h2
        pre.next = None
        return res.next
```

------

### 二叉树的下一个结点
> 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
>> 标签：二叉树，中序遍历。

------

1. 此节点有右分支，则输出right子节点一路left到底的节点；
2. 此节点有父节点：
    - 此节点为父节点的左节点，则返回父节点；
    - 此节点是父节点右节点，则继续向上找父节点，直到找到为左节点的；
3. 以上都不满足，返回None

```python
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right: # 1
            node = pNode.right
            while node.left: node = node.left
            return node
        while pNode.next:  # 2
            if pNode == pNode.next.left: return pNode.next
            pNode = pNode.next
        return # 3
```

------

### 对称的二叉树
> 请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
>> 标签：二叉树，深度优先搜索DFS。

------
- 对称满足的性质：设置两个指针left，right从root根节点开始，一个向左一个向右，遇到的子节点值恒相等，且子节点同时存在或同时越过叶子节点；
- 根据此性质使用递归进行判断。
```python
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot: return True
        return self.match(pRoot.left, pRoot.right)
    def match(self, lef, rig):
        if not lef and not rig: return True
        if not lef or not rig or lef.val != rig.val: return False
        return self.match(lef.left, rig.right) and self.match(lef.right, rig.left)
```

------

### 按之字形顺序打印二叉树
> 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
>> 标签：二叉树，广度优先搜索BFS。

------

- 先解决一个基础问题：按层打印，这个前面的题中已经解决；
- 偶数层保持不变，对奇数层倒置再添加至结果。

```python
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot: return []
        res, roots, reverse = [], [pRoot], False
        while roots:
            tmp = []
            for _ in range(len(roots)):
                r = roots.pop(0)
                tmp.append(r.val)
                if r.left: roots.append(r.left)
                if r.right: roots.append(r.right)
            if reverse: tmp.reverse()
            reverse = not reverse
            res.append(tmp)
        return res
```

------

### 把二叉树打印成多行
> 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
>> 标签：二叉树，广度优先遍历BFS。

------

- 仍然是按层打印，本次使用递归方法解。

```python
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        res = []
        self.line(res, [pRoot])
        return res

    def line(self, res, roots):
        if not roots or not roots[0]: return
        tmp, re = [], []
        for r in roots:
            re.append(r.val)
            if r.left: tmp.append(r.left)
            if r.right: tmp.append(r.right)
        res.append(re)
        self.line(res, tmp)
```

------

### 序列化二叉树
> 请实现两个函数，分别用来序列化和反序列化二叉树。
>> 标签：二叉树，设计，深度优先遍历DFS。

------

- 序列化：本解答使用前序遍历序列化，通过递归完成。
  - 叶子节点的左右节点需要填充'#'。
- 反序列化：以前序遍历重构二叉树，返回根节点。
  - '#'代表叶子节点底下的None。

```python
class Solution:
    def Serialize(self, root):
        # write code here
        return self.serialize(root)[:-1]

    def serialize(self, root):
        res = ""
        if not root: return '#,'
        res += str(root.val) + ','
        res += self.serialize(root.left)
        res += self.serialize(root.right)
        return res

    def Deserialize(self, s):
        root, i = self.deserialize(s.split(","),0)
        return root

    def deserialize(self, s, i):
        if i >= len(s) or s[i] == '#':
            return None, i + 1
        root = TreeNode(int(s[i]))
        root.left, i = self.deserialize(s, i+1)
        root.right, i = self.deserialize(s, i)
        return root, i
```

------

### 二叉搜索树的第k个结点
> 给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
>> 标签：二叉搜索树，中序遍历。

------

- 二叉搜索树的中序遍历即是排序list；
- 输出二叉搜索树的中序遍历，当输出到第k个节点时记录结果并return。

```python
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        self.res, self.k, self.count = None, k - 1, 0
        self.recur(pRoot)
        return self.res
    def recur(self, root):
        if not root: return
        self.recur(root.left)
        if self.res: return
        if self.count == self.k: self.res = root
        self.count += 1
        self.recur(root.right)
```

------

### 数据流中的中位数
> 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
>> 标签：堆，设计。

------

- 采用一个大顶堆、一个小顶堆，并保证：
  - 大顶堆内的所有数字小于小顶堆的所有数字；
  - 允许大顶堆的长度==小顶堆长度+1；
- 当大顶堆长度==小顶堆长度时，中位数为大顶堆和小顶堆的顶元素的平均值；否则等于小顶堆的顶元素值（小顶堆长度>=大顶堆长度）；
- python使用heapq直接实现小顶堆q。而大顶堆p的实现方法是将push的所有元素取负。顶元素为小顶堆/大顶堆的首个元素p[0]和q[0]。

```python
import heapq
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.q = []
        self.p = []
    def Insert(self, num):
        # write code here
        if not self.p or num <= -self.p[0]: heapq.heappush(self.p, -num)
        else: heapq.heappush(self.q, num)
        if len(self.p) == len(self.q) + 2: heapq.heappush(self.q, -heapq.heappop(self.p))
        elif len(self.p) + 1 == len(self.q): heapq.heappush(self.p, -heapq.heappop(self.q))
    def GetMedian(self, data):
        # write code here
        return (self.q[0] - self.p[0]) / 2.0 if len(self.q) == len(self.p) else -self.p[0]
```

- 二分法：
  - Insert方法内用二分法插入数据，保持arr排序状态；
  - GetMedian方法根据数组长度奇偶性返回中位数。

```python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.arr = []
    def Insert(self, num):
        # write code here、
        i, j = 0, len(self.arr)-1
        while i <= j:
            m = (i+j) // 2
            if self.arr[m] < num: i = m + 1
            else: j = m - 1
        self.arr = self.arr[:i] + [num] + self.arr[i:]
    def GetMedian(self, data):
        # write code here
        m = len(self.arr)//2
        return (self.arr[m]+self.arr[m-1])/2.0 if not len(self.arr) % 2 else self.arr[m]
```

------

### 滑动窗口的最大值
> 给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
>> 标签：队列。

------

- 建立一个队列存储窗口最大值，遍历整个list，按照以下规则处理队列：
  - 循环判断队列尾部值是否小于等于num[i]，若小于等于则pop此值（后面窗口最大值一定用不到这个值了，因为num[i]更大）；
  - 循环判断队列首部是否超出滑动窗口的范围，若超出则pop；
  - 将当前指针位置i添加到队列尾部；
- 当滑动窗口范围大于0且形成窗口（i + 1 >= size），则添加队首值，队首值满足：
  - 在窗口内；
  - 大于窗口内的所有值。

```python
# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        queue, res = [], []
        for i in range(len(num)):
            while queue and num[queue[-1]] <= num[i]: queue.pop()
            while queue and queue[0] <= i - size: queue.pop(0)
            queue.append(i)
            if size and i > size: res.append(num[queue[0]])
        return res
```

------

### 矩阵中的路径
> 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
>> 标签：深度优先搜索DFS，回溯法，记忆化。

------

- 深度优先搜索（DFS）/回溯法典型题，主体逻辑如下：
  - 从当前节点出发，有上下左右四种情况，任意一种情况能走对应路径即可，递归使用or；
  - 失败的终止条件：矩阵越界 or 已经走过 or 字符匹配失败；
  - 成功的终止条件：不失败 and 已经匹配完字符串最后一位；
- 建立flags标志矩阵，记录已经走过的点位：
  - 如果遇到走过的点位直接返回False；
  - 如果当前点上下左右四个方向都匹配失败，需要将当前点Flag释放，以防止影响其他路线走此点。
- 题目中matrix输入的是一个一维list，因此index = self.cols * i + j。
- hasPath要对rows和cols进行遍历，将所有点作为起点进行DFS，只要其中一种找到就返回True。

```python
# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        self.flags = [0 for _ in range(len(matrix))]
        self.matrix, self.rows, self.cols, self.path = matrix, rows, cols, path
        for i in range(rows):
            for j in range(cols):
                if self.search(i, j, 0): return True
        return False

    def search(self, i, j, k):
        index = self.cols * i + j
        if not 0 <= i < self.rows or not 0 <= j < self.cols or \
        self.flags[index] or self.matrix[index] != self.path[k]:
            return False # 越界 or 已经走过 or 不是所需节点 
        if k == len(self.path) - 1:
            return True # 已经找完，不需要继续递归
        self.flags[index] = 1 # 走过这个点，寻找下个点
        if self.search(i+1, j, k+1) or self.search(i-1, j, k+1) or \
        self.search(i, j+1, k+1) or self.search(i, j-1, k+1):  
            return True # 四条路中有一条可以走通
        self.flags[index] = 0 # 如果无法走通，要释放这个点，以防影响其他路线中走此点
        return False
```

------

### 机器人的运动范围
> 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
>> 标签：深度优先搜索DFS，记忆化。

------

- 深度优先搜索DFS思路：
  - 从矩阵某节点开始，可以向上下左右走，每个方向的格子数量都需要统计，因此递归将几个结果+；
  - 不能走的终止条件：矩阵越界、已经统计过、不满足题中的加和条件；
  - 建立matrix统计此格子是否已被统计。
- 可以理解为机器人按照以下优先级：向右、向左、向下、向上前进，其实此题下只需要向右向左向下即可，由于上面的点都已经走过，self.moving(i, j-1)始终会return 0
```python
# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        self.matrix, self.k, self.rows, self.cols = \
        [[0 for _ in range(cols)] for _ in range(rows)], threshold, rows, cols
        return self.moving(0, 0)
    def moving(self, i, j):
        if not 0 <= i < self.rows or not 0 <= j < self.cols or \
        self.matrix[i][j] or self.k < self.sums(i) + self.sums(j):
            return 0
        self.matrix[i][j] = 1
        return 1 + self.moving(i+1, j) + self.moving(i-1, j) + \
            self.moving(i, j+1) + self.moving(i, j-1) # still pass without self.moving(i, j-1).
    def sums(self, i):
        m = 0
        while i:
            i, b = i // 10, i % 10
            m += b
        return m
```

------


## [Source:牛客网剑指offer](https://www.nowcoder.com/ta/coding-interviews)


------


数组
排序

位运算

字符串
双指针

二分查找
分治算法

队列
栈
堆
哈希表
链表
贪心算法

树
深度优先搜索 DFS
广度优先搜索 BFS
二叉搜索树 BST
平衡二叉树 BBT
递归
记忆化

动态规划
回溯算法

图
拓扑排序

============

极小化极大
蓄水池抽样
几何

并查集
