def longestCommonPrefix(arr, n):
    # If the array is empty, return "-1"
    if n == 0:
        return "-1"
    
    # Find the shortest string in the array
    shortest_string = min(arr, key=len)
    
    # Initialize the prefix as the shortest string
    prefix = shortest_string
    
    # Iterate over each string in the array
    for string in arr:
        # Compare characters of the prefix and the current string
        while string[:len(prefix)] != prefix and prefix:
            # Reduce the prefix by one character from the end
            prefix = prefix[:len(prefix)-1]
        # If the prefix becomes empty, return "-1"
        if not prefix:
            return "-1"
    
    return prefix if prefix else "-1"

# Example usage:
arr1 = ["geeksforgeeks", "geeks", "geek", "geezer"]
n1 = len(arr1)
print(longestCommonPrefix(arr1, n1))  # Output: "gee"

arr2 = ["hello", "world"]
n2 = len(arr2)
print(longestCommonPrefix(arr2, n2))  # Output: "-1"
