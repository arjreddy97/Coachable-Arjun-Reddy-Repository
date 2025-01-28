class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_combos = []
        self.helper(n,n,[],all_combos)
        return all_combos
    def helper(self,left,right,curr,all_combos):
        if left > 0:
            new_combo = curr + ["("]
            self.helper(left-1,right,new_combo,all_combos)
        if left < right:
            new_combo = curr + [")"]
            self.helper(left,right-1,new_combo,all_combos)
        if left == 0 and right == 0:

            all_combos.append("".join(curr))
