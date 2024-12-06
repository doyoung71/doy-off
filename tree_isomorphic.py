def parse_tree(preorder):
    """Parses the preorder traversal string into a nested tree structure."""
    stack = []
    root = []
    stack.append(root)
    
    for token in preorder:
        if token == "#":  # End of children
            stack.pop()
        else:
            node = []  # Create a new node
            stack[-1].append(node)  # Add the node as a child of the last node
            stack.append(node)  # Push this node to the stack
    
    return root[0] if root else []

def are_isomorphic(tree1, tree2):
    """Checks if two trees are isomorphic."""
    if len(tree1) != len(tree2):  # Number of children must match
        return False

    if len(tree1) == 0:  # Both are leaves
        return True

    # Check isomorphism for all permutations of children
    n = len(tree1)
    used = [False] * n

    def can_match(i, j):
        return are_isomorphic(tree1[i], tree2[j])

    def backtrack(index):
        if index == n:
            return True
        for j in range(n):
            if not used[j] and can_match(index, j):
                used[j] = True
                if backtrack(index + 1):
                    return True
                used[j] = False
        return False

    return backtrack(0)

def main():
    t = int(input().strip())  # Number of test cases
    results = []
    
    for _ in range(t):
        tree1 = parse_tree(input().strip().split())
        tree2 = parse_tree(input().strip().split())
        if are_isomorphic(tree1, tree2):
            results.append("Isomorphic.")
        else:
            results.append("Not isomorphic.")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
