# Sliding Window Patterns — Complete Interview Guide

A comprehensive, production-ready reference for mastering **Sliding Window** problems in technical coding interviews.

---

## Table of Contents

1. [Core Concept & Applicability](#1-core-concept--applicability)
2. [Core Code Templates](#2-core-code-templates)
3. [Pattern Breakdown & Expanded Problem Sets](#3-pattern-breakdown--expanded-problem-sets)
   - [Pattern 1: Fixed Size Window](#pattern-1-fixed-size-window)
   - [Pattern 2: Variable Size Window (Maximizing / Minimizing)](#pattern-2-variable-size-window-maximizing--minimizing)
   - [Pattern 3: HashMap & Substring Matching](#pattern-3-hashmap--substring-matching)
   - [Pattern 4: Monotonic Queue Window](#pattern-4-monotonic-queue-window)
   - [Pattern 5: Exact K Transformation Trick](#pattern-5-exact-k-transformation-trick)
   - [Pattern 6: Circular & Hybrid Sliding Window](#pattern-6-circular--hybrid-sliding-window)
   - [Pattern 7: Two-Pointer Fast/Slow & Non-Shrinking Windows](#pattern-7-two-pointer-fastslow--non-shrinking-windows)
4. [Deep Dive: Advanced Interview Edge Cases](#4-deep-dive-advanced-interview-edge-cases)
5. [Time & Space Complexity Reference](#5-time--space-complexity-reference)
6. [Comprehensive Learning Roadmap](#6-comprehensive-learning-roadmap)
7. [Golden Rules Summary](#7-golden-rules-summary)

---

## 1. Core Concept & Applicability

### What is Sliding Window?
Sliding Window is an optimization technique used to transform nested loops O(N²) into linear time O(N) for problems involving **contiguous subarrays or substrings**. Instead of recomputing overlapping elements from scratch, you maintain a moving window state updated in O(1) time per step.

```text
Array: [ 1  2  3  4  5 ]
Step 1: [ 1  2  3 ]        -> sum = 6
Step 2:    [ 2  3  4 ]     -> sum = 6 - 1 + 4 = 9
Step 3:       [ 3  4  5 ]  -> sum = 9 - 2 + 5 = 12
```

---

### Identification Signals
Consider Sliding Window when the problem involves **contiguous segments** and uses keywords like:

- **Contiguous / Subarray / Substring / Consecutive**
- **Longest / Shortest / Maximum / Minimum / Subsegment**
- **At Most K / Exactly K / Window of size K / Budget of K**

> **Rule of Thumb:** If the problem involves contiguous data and all values are **non-negative**, Sliding Window is almost always the optimal target. If negative numbers are present and you need subarray sums, standard sliding window breaks—consider **Prefix Sum + HashMap** or **Monotonic Deque** instead.

---

## 2. Core Code Templates

### Fixed Size Window (⭐)
Maintain a static window size of K by adding the incoming right element and dropping the trailing left element once size exceeds K.

```python
def fixed_window(nums: list[int], k: int) -> int:
    left = 0
    window_state = 0
    ans = float('-inf')

    for right in range(len(nums)):
        window_state += nums[right]  # 1. Expand window

        if right - left + 1 > k:     # 2. Shrink window if size exceeds k
            window_state -= nums[left]
            left += 1

        if right - left + 1 == k:    # 3. Process valid window state
            ans = max(ans, window_state)

    return ans
```

---

### Variable Size Window — Dynamic Contraction (⭐⭐)
Expand the right boundary until the window condition becomes invalid, then contract from the left until validity is restored.

```python
def variable_window_min(nums: list[int], target: int) -> int:
    left = 0
    window_state = 0
    ans = float('inf')

    for right in range(len(nums)):
        window_state += nums[right]  # Include right element

        while window_state >= target:  # Contract while condition is valid (for MIN length)
            ans = min(ans, right - left + 1)
            window_state -= nums[left]
            left += 1

    return ans if ans != float('inf') else 0
```

---

### HashMap / Substring Window (⭐⭐⭐)
Track frequency counts or unique element counts to satisfy substring requirements.

```python
from collections import defaultdict

def hashmap_window(s: str, k: int) -> int:
    counts = defaultdict(int)
    left = 0
    ans = 0

    for right in range(len(s)):
        counts[s[right]] += 1  # Add right character to map

        while len(counts) > k: # Condition: At most K distinct elements
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1

        ans = max(ans, right - left + 1)

    return ans
```

---

### Monotonic Queue Window (⭐⭐⭐⭐)
Maintain a double-ended queue (`deque`) of indices to preserve monotonic order (increasing or decreasing) within a moving window.

```python
from collections import deque

def max_sliding_window(nums: list[int], k: int) -> list[int]:
    q = deque()  # Stores indices, maintaining monotonically decreasing values
    ans = []

    for right, val in enumerate(nums):
        # 1. Maintain monotonic property (pop smaller elements)
        while q and nums[q[-1]] <= val:
            q.pop()
        q.append(right)

        # 2. Remove elements outside the left boundary
        if q[0] <= right - k:
            q.popleft()

        # 3. Record answer once full window is formed
        if right >= k - 1:
            ans.append(nums[q[0]])

    return ans
```

---

## 3. Pattern Breakdown & Expanded Problem Sets

### Pattern 1: Fixed Size Window
Focuses on running sums, running averages, or character counts within a static boundary K.

| # | Problem | Difficulty | Key Concepts |
|---|---|---|---|
| LC 643 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | **Easy** | Running sum, initial window setup |
| LC 1456 | [Max Vowels in a Substring of Length K](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | **Medium** | Vowel tracking, character state |
| LC 1052 | [Grumpy Bookstore Owner](https://leetcode.com/problems/grumpy-bookstore-owner/) | **Medium** | Gain window trick, conditional contribution |
| LC 1423 | [Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) | **Medium** | Complementary window strategy (minimize inner window) |
| LC 2461 | [Max Sum of Distinct Subarrays With Length K](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/) | **Medium** | Frequency map + fixed size constraint |
| LC 2090 | [K Radius Subarray Averages](https://leetcode.com/problems/k-radius-subarray-averages/) | **Medium** | Fixed size sum with index offsetting |
| LC 1100 | [Find K-Length Substrings With No Repeated Characters](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/) | **Medium** | Fixed window + set distinct check |
| LC 1343 | [Number of Sub-arrays of Size K with Average >= Threshold](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) | **Medium** | Threshold comparison on static windows |
| LC 2379 | [Minimum Recolors to Get K Consecutive Black Blocks](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/) | **Easy** | Minimum white block flips in window of size K |

---

### Pattern 2: Variable Size Window (Maximizing / Minimizing)
Dynamically scales window length based on target thresholds, conditions, or budget constraints.

| # | Problem | Difficulty | Key Concepts |
|---|---|---|---|
| LC 209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | **Medium** | Standard dynamic contraction for MIN length |
| LC 713 | [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) | **Medium** | Count valid windows: `right - left + 1` |
| LC 1658 | [Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) | **Medium** | Inverse window optimization (find max middle sum) |
| LC 1838 | [Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/) | **Medium** | Sorting + window budget cost calculation |
| LC 1004 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | **Medium** | Flip budget (K zero replacement) |
| LC 1493 | [Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) | **Medium** | Single deletion variant (K=1) |
| LC 2024 | [Maximize the Confusion of an Exam](https://leetcode.com/problems/maximize-the-confusion-of-an-exam/) | **Medium** | Two-pass/max frequency flip budget |
| LC 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | **Medium** | Max frequency optimization within dynamic window |
| LC 904 | [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | **Medium** | At most 2 distinct elements in window |
| LC 2730 | [Find Longest Semi-Repetitive Substring](https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/) | **Medium** | At most 1 adjacent equal pair condition |
| LC 2779 | [Maximum Beauty of an Array After Applying Operation](https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/) | **Medium** | Sort + sliding window range condition |

---

### Pattern 3: HashMap & Substring Matching
Leverages frequency maps or array-based direct maps to detect anagrams, permutations, or required substring contents.

| # | Problem | Difficulty | Key Concepts |
|---|---|---|---|
| LC 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | **Medium** | Map/Set of character positions |
| LC 159 | [Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) | **Medium** | HashMap size bound |
| LC 340 | [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) | **Medium** | Generalized distinct counting |
| LC 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | **Hard** | Match counter optimization, target map contraction |
| LC 567 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | **Medium** | Fixed size frequency match |
| LC 438 | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | **Medium** | Sliding anagram signature match |
| LC 30 | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | **Hard** | Multi-offset sliding window with word maps |
| LC 1610 | [Maximum Number of Visible Points](https://leetcode.com/problems/maximum-number-of-visible-points/) | **Hard** | Polar angles conversion + sliding window angle range |

---

### Pattern 4: Monotonic Queue Window
Utilizes double-ended queues (`deque`) to track maximums or minimums within sliding bounds in O(1) amortized time per step.

| # | Problem | Difficulty | Key Concepts |
|---|---|---|---|
| LC 239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | **Hard** | Decreasing Monotonic Deque |
| LC 1438 | [Longest Continuous Subarray With Abs Diff <= Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | **Medium** | Dual Deques (Min Deque + Max Deque) |
| LC 862 | [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) | **Hard** | Monotonic Deque + Prefix Sums (handles negative values) |
| LC 1696 | [Jump Game VI](https://leetcode.com/problems/jump-game-vi/) | **Medium** | DP + Monotonic Deque optimization |
| LC 2398 | [Maximum Number of Robots Within Budget](https://leetcode.com/problems/maximum-number-of-robots-within-budget/) | **Hard** | Max Deque + Running Sum variable window |

---

### Pattern 5: Exact K Transformation Trick
Directly computing subsegments with **"Exactly K"** criteria is tricky because windows aren't strictly monotonic. We resolve this by computing **"At Most K"** and applying the mathematical identity:

$$Exact(K) = AtMost(K) - AtMost(K - 1)$$

| # | Problem | Difficulty | Key Concepts |
|---|---|---|---|
| LC 992 | [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) | **Hard** | Direct implementation of AtMost trick |
| LC 1248 | [Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/) | **Medium** | Transform odd numbers into count budget |
| LC 930 | [Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/) | **Medium** | AtMost sum subtraction |
| LC 1208 | [Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget/) | **Medium** | Absolute difference cost window |
| LC 3306 | [Count of Substrings Containing Every Vowel and K Consonants II](https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/) | **Hard** | AtLeast/AtMost Transformation with frequency maps |

---

### Pattern 6: Circular & Hybrid Sliding Window

| Pattern Type | Problem | Difficulty | Key Concept |
|---|---|---|---|
| **Circular** | LC 918: [Max Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) | **Medium** | max(Kadane, Total - MinSubarray) |
| **Circular** | LC 2134: [Min Swaps to Group All 1's II](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/) | **Medium** | Virtual array doubling (`2N` via modulo) |
| **Circular** | LC 1652: [Defuse the Bomb](https://leetcode.com/problems/defuse-the-bomb/) | **Easy** | Circular index wrap-around with fixed window |
| **Prefix Sum** | LC 560: [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | **Medium** | Prefix sum map (Handles negative values) |
| **Prefix Sum** | LC 525: [Contiguous Array](https://leetcode.com/problems/contiguous-array/) | **Medium** | Map binary balances to first seen indices |
| **Binary Search**| LC 1482: [Min Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) | **Medium** | BS on answer + validation window check |

---

### Pattern 7: Two-Pointer Fast/Slow & Non-Shrinking Windows
Instead of contracting `left` inside a `while` loop, **non-shrinking windows** only shift `left` by at most 1 per step, maintaining the maximum valid window size found so far.

```python
# Non-shrinking window for maximum length
def max_window_non_shrinking(nums: list[int], k: int) -> int:
    left = 0
    # window_state initialization...

    for right in range(len(nums)):
        # Expand window: add nums[right] to state

        # If condition is violated, shift left by ONLY 1 step (window never shrinks)
        if is_invalid(window_state, k):
            # Remove nums[left] from state
            left += 1

    # The maximum length discovered remains (len(nums) - left)
    return len(nums) - left
```

| # | Problem | Difficulty | Key Concepts |
|---|---|---|---|
| LC 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | **Medium** | O(N) single-pass with non-shrinking window |
| LC 1493 | [Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) | **Medium** | Non-shrinking size maintenance |

---

## 4. Deep Dive: Advanced Interview Edge Cases

### Edge Case 1: Handling Negative Numbers in Subarray Sums
Standard sliding window relies on **monotonicity**: adding an element *must* increase the sum, and shrinking *must* decrease it. When negative values are present, monotonicity breaks.

- **Standard Sum equal to K with negatives:** Use **Prefix Sum + HashMap** (O(N) time, O(N) space).
- **Shortest Subarray with Sum >= K with negatives (LC 862):** Use **Prefix Sum + Monotonic Deque** (O(N) time, O(N) space).

### Edge Case 2: Multi-Offset Sliding Window (LC 30)
When sliding on string sequences in chunks of length L (e.g., matching words of length 3), you must run L independent sliding windows starting from offset `0, 1, ..., L-1`.

---

## 5. Time & Space Complexity Reference

| Pattern | Time Complexity | Space Complexity | Primary Overhead |
|---|---|---|---|
| **Fixed Window** | O(N) | O(1) | Primitive registers |
| **Variable Window** | O(N) | O(1) | Pointers |
| **HashMap Window** | O(N) | O(Σ) | Character set size (Σ) |
| **Monotonic Deque** | O(N) | O(K) | Deque size capped at K |
| **Prefix Sum + Hash**| O(N) | O(N) | Subarray sum map |

---

## 6. Comprehensive Learning Roadmap

```text
Level 1: Fundamentals
├── LC 643  (Fixed Size Basics)
├── LC 1456 (Fixed Character Window)
└── LC 209  (Dynamic Window Expansion/Contraction)

Level 2: String & Frequency Patterns
├── LC 3    (Unique Characters Window)
├── LC 567  (Permutation Matching)
├── LC 904  (At Most K Distinct)
└── LC 1004 (Flip/Replacement Budget)

Level 3: Advanced Optimization & Monotonic Queues
├── LC 76   (Minimum Window Matching)
├── LC 992  (Exactly K -> AtMost Trick)
├── LC 239  (Monotonic Deque Windowing)
├── LC 1438 (Dual Deque Min/Max Window)
└── LC 862  (Negative Numbers + Prefix Deque)
```

---

## 7. Golden Rules Summary

1. **Subsegment Contiguity:** Sliding window requires contiguous elements. If elements can be rearranged non-contiguously, standard sliding window will fail.
2. **Monotonic Behavior (Non-negative Values):** Adding an element must predictably expand/increase the target sum or frequency. If negative numbers introduce non-monotonic jumps, switch to a **Prefix Sum + HashMap** or **Monotonic Deque**.
3. **Number of Subarrays Calculation:** For variable dynamic windows ending at `right`, the total valid contiguous subarrays ending at index `right` is given by:
   $$	ext{Subarrays} = 	ext{right} - 	ext{left} + 1$$
4. **Exactly K Problems:** Turn `Exactly(K)` into `AtMost(K) - AtMost(K - 1)`.
5. **Window Max/Min:** Use a Monotonic Deque to maintain range extremes in O(1) amortized time per step.



# Sliding Window & Prefix Sum Patterns Update

This update introduces advanced algorithmic patterns, deeper state tracking strategies, pattern recognition signals, and expanded problem sets covering LeetCode classics.

---

## 🚀 Key Additions Included in the Update

### Pattern 6: Prefix Sum + HashMap (When Window Invariant Breaks)
* **Learning Objectives:**
  * Understand why negative numbers break standard sliding window monotonicity.
  * Master $O(N)$ lookup using running prefix sums and HashMaps ($\text{Prefix}[j] - \text{Prefix}[i] = K$).
  * Learn remainder arithmetic for divisibility constraints ($\text{Prefix}[i] \bmod K$).
* **Pattern Recognition Signals:**
  * Contiguous subarray problem containing **negative integers** or balanced properties (e.g., equal 0s and 1s).
  * Constraints involving exact sums ($\text{Sum} = K$) or multiples ($\text{Sum} \bmod K = 0$).
* **Problems:**
  * [LC 560: Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
  * [LC 325: Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/)
  * [LC 523: Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)
  * [LC 974: Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)
  * [LC 525: Contiguous Array](https://leetcode.com/problems/contiguous-array/)

---

### Pattern 7: Circular Window Strategy
* **Learning Objectives:**
  * Handle boundary-wrapping without physically mutating input structures.
  * Apply array duplication ($2N$), modular indexing ($i \bmod N$), and total sum subtraction tricks.
* **Pattern Recognition Signals:**
  * Explicit mention of "circular array" or wrap-around constraints (last element connects to first element).
  * Taking elements from both ends (left and right edges simultaneously).
* **Problems:**
  * [LC 918: Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)
  * [LC 1423: Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)
  * [LC 2134: Minimum Swaps to Group All 1s Together II](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/)
  * [LC 1652: Defuse the Bomb](https://leetcode.com/problems/defuse-the-bomb/)

---

### Pattern 8: Sliding Window + HashMap Deep Dive
* **Learning Objectives:**
  * Maintain complex dynamic state across expanding/contracting windows.
  * Track exact character frequencies, match counters (`matched == unique`), and distinct item thresholds.
* **Pattern Recognition Signals:**
  * Dynamic substring searching involving permutations, anagrams, or frequency matching.
  * Problems specifying "At most $K$ distinct characters" or "Shortest substring containing all target chars".
* **Problems:**
  * [LC 3: Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
  * [LC 76: Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
  * [LC 438: Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
  * [LC 567: Permutation in String](https://leetcode.com/problems/permutation-in-string/)
  * [LC 424: Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
  * [LC 904: Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)
  * [LC 159: Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
  * [LC 340: Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)

---

### Pattern 9: Binary Search + Sliding Window / Greedy
* **Learning Objectives:**
  * Convert optimization problems ("Find min/max capacity") into decision problems (`isValid(mid)`).
  * Use dynamic windowing or greedy passes as validation helpers inside a binary search loop over answer space.
* **Pattern Recognition Signals:**
  * Problem asks to "Minimize the Maximum" or "Maximize the Minimum".
  * Direct search space is large, but checking whether a candidate answer works takes $O(N)$ time.
* **Problems:**
  * [LC 1838: Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/)
  * [LC 1482: Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)
  * [LC 1552: Magnetic Force Between Two Balls](https://leetcode.com/problems/magnetic-force-between-two-balls/)
  * [LC 875: Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)

---

### Pattern 10: Advanced & Multi-Structure Sliding Window
* **Learning Objectives:**
  * Combine sliding window bounds with heaps, monotonic deques, and balance-tree maps.
  * Efficiently extract min, max, or median values from sliding ranges in $O(\log N)$ or $O(1)$ time.
* **Pattern Recognition Signals:**
  * Sliding window requires dynamic order statistics (e.g., maintaining dynamic median or min/max absolute differences within range $K$).
  * Multiple lists or arrays whose bounds must expand/contract together.
* **Problems:**
  * [LC 76: Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
  * [LC 632: Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/)
  * [LC 480: Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)
  * [LC 220: Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/)

---

## 📚 General Enhancements

* **Updated Table of Contents:** Streamlined navigation across all patterns.
* **Learning Roadmap:** Expanded progression paths structured across 5 distinct mastery levels.
* **Golden Rules:** Added quick-reference heuristics for handling circular arrays, breaking monotonicity, and binary search answer-space optimization.
