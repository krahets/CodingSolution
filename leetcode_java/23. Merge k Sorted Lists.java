class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        LinkedList<ListNode> res = new LinkedList(Arrays.asList(lists));
        while (res.size() > 1) {
            res.addLast(merge(res.removeFirst(),res.removeFirst()));
        }
        return res.size() == 0 ? null : res.get(0);
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