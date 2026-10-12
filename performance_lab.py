
# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there is a tie, return any of the most frequent values.

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    return max(counts, key=counts.get)


"""
Time and Space Analysis for problem 1:
- Best-case: O(n), because every element must be counted.
- Worst-case: O(n), assuming average O(1) dictionary operations.
- Average-case: O(n), for counting all elements.
- Space complexity: O(n), because the dictionary can store n unique values.
- Why this approach? A dictionary counts each number in one pass.
- Could it be optimized? The time complexity is already O(n).
- Trade-offs: Uses extra memory to avoid repeatedly scanning the list.
"""


# Tests for Problem 1
assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
assert most_frequent([5, 5, 5]) == 5
assert most_frequent([]) is None
assert most_frequent([7]) == 7


# 🔍 Problem 2: Remove Duplicates While Preserving Order

def remove_duplicates(nums):
    seen = set()
    result = []

    for number in nums:
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result


"""
Time and Space Analysis for problem 2:
- Best-case: O(n), because every element must be checked.
- Worst-case: O(n) average under normal hash-set behavior.
- Average-case: O(n), with average O(1) set lookups.
- Space complexity: O(n) for the set and result list.
- Why this approach? A set tracks previously seen values while
  the result list preserves the original order.
- Could it be optimized? The time complexity is already O(n).
- Trade-offs: Uses extra memory to preserve order efficiently.
"""


# Tests for Problem 2
assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
assert remove_duplicates([]) == []
assert remove_duplicates([1, 1, 1]) == [1]
assert remove_duplicates([3, 2, 1]) == [3, 2, 1]


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Assume the input list contains no duplicates.

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for number in nums:
        complement = target - number

        if complement in seen:
            pairs.append((complement, number))

        seen.add(number)

    return pairs


"""
Time and Space Analysis for problem 3:
- Best-case: O(n), because every element is checked.
- Worst-case: O(n), assuming average O(1) set lookups.
- Average-case: O(n), plus the cost of storing the output.
- Space complexity: O(n), for the set and result pairs.
- Why this approach? A set lets us check for a matching complement
  without comparing every possible pair.
- Could it be optimized? The search is already O(n), excluding output.
- Trade-offs: Uses extra memory to reduce the time from O(n^2)
  for a nested-loop solution to O(n) average time.
"""


# Tests for Problem 3
assert set(find_pairs([1, 2, 3, 4], 5)) == {(1, 4), (2, 3)}
assert find_pairs([], 5) == []
assert find_pairs([1, 2, 3], 10) == []
assert find_pairs([1, 4, 6, 9], 10) == [(1, 9), (4, 6)]


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)

def add_n_items(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    capacity = 2
    items = [None] * capacity
    size = 0

    for number in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            print(f"Resizing from {capacity} to {new_capacity}")

            new_items = [None] * new_capacity
            for index in range(size):
                new_items[index] = items[index]

            items = new_items
            capacity = new_capacity

        items[size] = number
        size += 1

    return items[:size]


"""
Time and Space Analysis for problem 4:
- Resizes happen when size reaches capacity: 2, 4, 8, 16, etc.
- Worst-case for a single append: O(n) when resizing copies
  all existing elements.
- Amortized time per append: O(1), because doubling makes
  resizing increasingly infrequent.
- Total time for n appends: O(n).
- Space complexity: O(n) for the allocated list.
- Why this approach? It demonstrates how dynamic arrays grow.
- Could it be optimized? Python lists already use dynamic resizing;
  this function simulates the process for learning purposes.
- Trade-offs: Resizing occasionally costs O(n) time and temporarily
  requires extra memory, but doubling reduces total copying.
"""


# Tests for Problem 4
assert add_n_items(0) == []
assert add_n_items(1) == [0]
assert add_n_items(2) == [0, 1]
assert add_n_items(6) == [0, 1, 2, 3, 4, 5]

try:
    add_n_items(-1)
    assert False, "Expected ValueError for negative n"
except ValueError:
    pass


# 🔍 Problem 5: Compute Running Totals

def running_total(nums):
    result = []
    total = 0

    for number in nums:
        total += number
        result.append(total)

    return result


"""
Time and Space Analysis for problem 5:
- Best-case: O(n), because every number must be processed.
- Worst-case: O(n), because each number is processed once.
- Average-case: O(n), for the single pass through the list.
- Space complexity: O(n), for the output list.
- Why this approach? A running sum avoids recalculating the sum
  of all previous elements at every position.
- Could it be optimized? Extra space is necessary to return a new
  list containing all the running totals.
- Trade-offs: Stores the output in memory for a simple O(n) solution.
"""


# Tests for Problem 5
assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
assert running_total([]) == []
assert running_total([5]) == [5]
assert running_total([-1, 2, -3]) == [-1, 1, -2]


# 🔧 Optimization comparison
"""
Problem 3 was optimized by replacing nested loops with a set.

Original approach:
- Time complexity: O(n^2), because each number is compared
  against other numbers.
- Auxiliary space: O(1), excluding the output list.

Optimized approach:
- Time complexity: O(n) average, using set lookups.
- Auxiliary space: O(n), because the set stores seen numbers.

The optimized version is faster for large inputs but uses more
memory. The output pairs still require additional space.
"""

print("All performance lab tests passed!")