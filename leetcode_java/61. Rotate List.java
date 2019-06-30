/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null) return null;
        ListNode tail = head, cut = head;
        int len = 0;
        while(tail.next != null){
            tail = tail.next;
            len++;
        }
        k %= len + 1;
        for(int i = 0; i < len - k; i++) cut = cut.next;
        tail.next = head;
        ListNode res = cut.next;
        cut.next = null;
        return res;
    }
}