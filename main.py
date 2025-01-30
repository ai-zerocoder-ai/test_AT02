def count_vowels(s):
    vowels = "aeiouAEIOUyY"
    return sum(1 for char in s if char in vowels)
