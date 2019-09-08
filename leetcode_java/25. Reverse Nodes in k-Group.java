/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode res = new ListNode(0), tail = res;
        ListNode cur = head, pre = null, nex = null;
        while(cur != null) {
            ListNode tmp = cur, left = cur;
            for(int i = 0; i < k - 1; i++) {
                tmp = tmp.next;
                if(tmp == null) {
                    tail.next = cur;
                    return res.next;
                }
            }
            for(int i = 0; i < k; i++) {
                nex = cur.next;
                cur.next = pre;
                pre = cur;
                cur = nex;
            }
            tail.next = pre;
            tail = left;
        }
        tail.next = null;
        return res.next;
    }
}