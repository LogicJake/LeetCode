# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-10-29 14:50:37
# @Last Modified time: 2018-10-29 15:12:41


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        top = root

        ans = cur = TreeNode(None)

        if root is None:
            return root
        while not top is None or len(stack) != 0:
            while top is not None:
                stack.append(top)
                top = top.left

            top = stack.pop()
            if res is None:
                res = top
            else:
                res.letf = top
                res = top
            top = top.right
        return res_top