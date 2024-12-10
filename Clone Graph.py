class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if (node == None):
            return 
        clonedNodes = {}
        self.dfs(node,set(),clonedNodes)
        return clonedNodes[node.val]
        
    def dfs(self,node,visited,clonedNodes):
        
        if (node == None):
            return 
        
        if (node.val in visited):
            
            return 
        
        
        visited.add(node.val)
        
        if (node.val not in clonedNodes):
            clonedNodes[node.val] = Node(node.val,[])
            
        clonedNode = clonedNodes[node.val]
        
        for nei in node.neighbors:
            
            if (nei.val not in clonedNodes):
                clonedNodes[nei.val] = Node(nei.val,[])
                
            clonedNode.neighbors.append(clonedNodes[nei.val])
            
            self.dfs(nei,visited,clonedNodes)
