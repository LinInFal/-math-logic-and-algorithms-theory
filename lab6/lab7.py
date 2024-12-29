"""
Задача 1А. Поиск в массиве
"""
def task_1a(n, m, array_a, array_b):
    set_a = set(array_a)

    result = ["YES" if b in set_a else "NO" for b in array_b]
    print("\n".join(result))

n, m = map(int, input().split())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))
task_1a(n, m, array_a, array_b)

# in:
# 3 3
# 2 3 5
# 1 2 3
# out:
# NO
# YES
# YES

"""
Задача 1В. Максимум в скользящем окне
"""
def task_1b(n, arr, m, moves):
    l, r = 0, 0
    result = []
    current_max = arr[0]
    for op in moves:
        if op == 'R':
            r += 1
            if r < n:
                current_max = max(current_max, arr[r])
        elif op == 'L':
            if l < r:
                l += 1
                if l <= r:
                    current_max = max(arr[l:r + 1])
        result.append(current_max)
    return result

with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    arr = list(map(int, f.readline().split()))
    m = int(f.readline().strip())
    moves = list(map(str, f.readline()))

output = task_1b(n, arr, m, moves)

with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, output)))

# in:
# 4
# -3 -2 -1 0
# 6
# RRRLLL
# out:
# -2 -1 0 0 0 0

"""
Задача 1C. Жадная последовательность
"""
def task_1c(n, m, arr):
    for _ in range(m):
        arr.sort()
        first = arr.pop(0)
        second = arr.pop(0)
        arr.append(first + second)
    return list(arr)

with open('input.txt', 'r') as f:
    n, m = map(int, f.readline().split())
    arr = list(map(int, f.readline().split()))

output = task_1c(n, m, arr)

with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, output)))

# in:
# 4 1
# 1 2 3 4
# out:
# 3 4 3

"""
Задача 1D. Дифтонги
"""
def task_1d(n, words):
    def is_vowel(char):
        return char in 'aeiouy'

    def count_diphthongs(word):
        count = 0
        word_len = len(word)

        for i in range(word_len - 1):
            if is_vowel(word[i]) and is_vowel(word[i + 1]):
                if (i == 0 or not is_vowel(word[i - 1])) and (i + 2 == word_len or not is_vowel(word[i + 2])):
                    count += 1
        return count

    max_diphthongs = 0
    diphthong_counts = []

    for w in words:
        count = count_diphthongs(w)
        diphthong_counts.append(count)
        if count > max_diphthongs:
            max_diphthongs = count

    return [words[i] for i in range(n) if diphthong_counts[i] == max_diphthongs]

with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    words = [f.readline().strip() for _ in range(n)]

output = task_1d(n, words)

with open('output.txt', 'w') as f:
    f.write('\n'.join(map(str, output)))

# in:
# 3
# e
# ee
# eee
# out:
# ee

"""
Задача 1E. Ближайшее число
"""
def task_1e(n, nums):
    result = [0] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        else:
            result[i] = nums[i]
        stack.append(nums[i])
    return result

with open('input.txt', 'r') as f:
    lines = f.readlines()
    if len(lines) == 1:
        nums = list(map(int, lines[0].split()))
        n = nums[0]
        nums = nums[1:]
    else:
        n = int(lines[0].strip())
        nums = list(map(int, lines[1].split()))

output = task_1e(n, nums)

with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, output)))

# in:
# 4 1 2 3 4
# out:
# 2 3 4 4