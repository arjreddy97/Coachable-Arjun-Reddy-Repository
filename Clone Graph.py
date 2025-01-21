class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if (node == None):
            return 
        clonedNodes = {}
        self.dfs(node,clonedNodes)
        return clonedNodes[node.val]
        
    def dfs(self,node,visited,clonedNodes):
        
        if (node.val in cloned_nodes):
            return 
        
        cloned_nodes.add(node.val)
        
        if (node.val not in clonedNodes):
            clonedNodes[node.val] = Node(node.val,[])
            
        clonedNode = clonedNodes[node.val]
        
        for nei in node.neighbors:
            
            if (nei.val not in clonedNodes):
                clonedNodes[nei.val] = Node(nei.val,[])
                
            clonedNode.neighbors.append(clonedNodes[nei.val])
            self.dfs(nei,clonedNodes)
