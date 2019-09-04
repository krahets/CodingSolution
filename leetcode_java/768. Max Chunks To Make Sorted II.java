class Solution {
    public int maxChunksToSorted(int[] arr) {
        LinkedList<Integer> stack = new LinkedList<Integer>();
        for(int num : arr) {
            if(!stack.isEmpty() && num < stack.getLast()) {
                int head = stack.removeLast();
                while(!stack.isEmpty() && num < stack.getLast()) stack.removeLast();
                stack.addLast(head);
            }
            else stack.addLast(num);
        }
        return stack.size();
    }
}