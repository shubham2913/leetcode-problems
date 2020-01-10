def isUnivalTree(root) :
    queue = [root]
    value = root.val
    while (len(queue) > 0):
        node = queue.pop(0)
        if node.val != value:
            return False
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    return True