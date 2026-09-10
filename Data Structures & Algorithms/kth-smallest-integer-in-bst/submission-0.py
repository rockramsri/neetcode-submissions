# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.heapOfSizeK=[]
        self.flag=False
        def depth(head,t):
            if head==None or self.flag:
                return 
            depth(head.left,t)
            print(head.val,t)
            if len(self.heapOfSizeK)==t:
                self.flag=True
                return
            else:
                self.heapOfSizeK.append(head.val)
            depth(head.right,t)

        # while True:
        #     while head.left==None:
        #         head=head.left
        #     self.heapOfSizeK.append(head.val)

        head=root
        depth(head,k)
        #print(self.heapOfSizeK[len(self.heapOfSizeK)-1])
        return self.heapOfSizeK[len(self.heapOfSizeK)-1]
        

        