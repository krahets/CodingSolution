import java.util.ArrayList;
import java.util.Arrays;

/**
 * Definition for singly-linked list. public class ListNode { int val; ListNode
 * next; ListNode(int x) { val = x; } }
 */
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