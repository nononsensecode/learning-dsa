def all_unique(items: list[str]) -> bool:
    unique_items = set(items)
    return len(unique_items) == len(items)

# Time Complexity: O(n)
# Space Complexity: O(n)
