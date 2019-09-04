class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode front = head;
        for(int i = 0; i < n; i++)
            front = front.next;
        if(front == null) return head.next;
        ListNode rear = head;
        while(front.next != null) {
            front = front.next;
            rear = rear.next;
        }
        rear.next = rear.next.next;
        return head;
    }
}