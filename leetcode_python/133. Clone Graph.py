"""
# Definition for a Node.
class Node:
    def __init__(self, val, nei***ors):
        self.val = val
        self.nei***ors = nei***ors
"""
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