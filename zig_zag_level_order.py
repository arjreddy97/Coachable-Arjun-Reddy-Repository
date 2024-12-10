class Solution:
   from collections import deque
   from collections import defaultdict
   def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       #O(N) O(N)
       queue = deque([(root,0)])
       levels = defaultdict(list) 
       prev_depth = 0
       while len(queue):
      
           curr,depth = queue.popleft()
           if not curr:
               continue
           if depth != prev_depth:
               if prev_depth % 2 !=0:
                   levels[prev_depth] = levels[prev_depth][::-1]
          
           levels[depth].append(curr.val)
           if curr.left:
               queue.append((curr.left,depth+1))
           if curr.right:
                queue.append((curr.right,depth+1))
      
           prev_depth = depth
       output = list(levels.values())
       if len(output) and len(output) % 2 == 0:
           output[-1] = output[-1][::-1]
      
       return output

