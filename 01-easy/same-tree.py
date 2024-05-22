class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def sameTree(p:TreeNode, q:TreeNode):
    # check if trees are empty (base case)
    if p is None and q is None:
        return True
    elif p is not None and q is not None:
        if p.val == q.val and (sameTree(p.left,q.left)) and (sameTree(p.right,q.right)):
            return True
        return False
    else:
        return False
            

        

        
        

