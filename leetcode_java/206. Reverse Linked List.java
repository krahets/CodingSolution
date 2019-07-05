/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null) return null;
        ListNode pre = null, nex = null;
        while(head.next != null) {
            nex = head.next;
            head.next = pre;
            pre = head;
            head = nex;
        }
        head.next = pre;
        return head;
    }
}