/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
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