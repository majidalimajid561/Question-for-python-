def is_vowel(char):
    vowels = 'aeiouAEIOU'
    return char in vowels

def categorize_character(char):
    if char.isalpha():
        if is_vowel(char):
            return f'{char} is a vowel.'
        else:
            return f'{char} is a consonant.'
    else:
        return 'Not an alphabetic character.'

# Example usage:
if __name__ == '__main__':
    test_chars = ['a', 'b', 'A', 'Z', '1']
    for ch in test_chars:
        print(categorize_character(ch))