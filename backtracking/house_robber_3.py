def rob(root):

    def solve(root):
        if not root:
            return [0, 0]
        
        left = solve(root.left)
        right = solve(root.right)

        include_root = root.data + left[1] + right[1]
        exclude_root = max(left) + max(right)

        return [include_root, exclude_root]
    
    return max(solve(root))
    
