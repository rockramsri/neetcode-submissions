# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        head=root
        if head == None:
            return []
        arrTree=[[head]]
        level=0
        while head:
            levelArr=[]
            for i in arrTree[level]:
                if i.left!=None:
                    levelArr.append(i.left)
                if i.right!=None:
                    levelArr.append(i.right)
            if len(levelArr) ==0:
                break
            arrTree.append(levelArr)
            level+=1
            
        print(arrTree)
        return [i[len(i)-1].val for i in arrTree]


        