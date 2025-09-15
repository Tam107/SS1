def convertSentenceToPigLatin(sentence):
    def is_vowel(char):
        return char.lower() in 'aeiou'

    def convert_word(word):
        if not word:
            return word

        # Check if word has no vowels
        has_vowel = False
        for char in word:
            if is_vowel(char):
                has_vowel = True
                break

        if not has_vowel:
            return word + 'yayyay'

        # If word starts with vowel
        if is_vowel(word[0]):
            return word + 'yay'

        # Find first vowel position
        vowel_pos = 0
        for i, char in enumerate(word):
            if is_vowel(char):
                vowel_pos = i
                break

        # Convert to Pig Latin
        return word[vowel_pos:] + word[:vowel_pos] + 'ay'

    # Split sentence into words, convert each, and join back
    words = sentence.split()
    converted_words = [convert_word(word) for word in words]
    return ' '.join(converted_words)