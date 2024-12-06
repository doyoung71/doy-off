def solution(v):
    """
    Finds the remaining point to complete a rectangle given three vertices.
    
    Args:
        v (list): A list of three points, each represented as [x, y].

    Returns:
        list: The coordinates of the remaining point as [x, y].
    """
    # Use XOR operation to find the unique x and y coordinates
    x = v[0][0] ^ v[1][0] ^ v[2][0]
    y = v[0][1] ^ v[1][1] ^ v[2][1]
    
    return [x, y]

# Example usage
print(solution([[1, 4], [3, 4], [3, 10]]))  # Output: [1, 10]
print(solution([[1, 1], [2, 2], [1, 2]]))  # Output: [2, 1]
