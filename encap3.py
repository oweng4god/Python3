class WordReverser:
    """
    A simple class to reverse a string word by word.
    """

    def reverse_words(self, text):
        # Split the text into words
        words = text.split()

        # Reverse the list of words
        reversed_words = words[::-1]

        # Join them back into a string
        return " ".join(reversed_words)
if __name__ == "__main__":
    reverser = WordReverser()
    
    sentence = "Hello this is a Python example"
    result = reverser.reverse_words(sentence)
    
    print("Original:", sentence)
    print("Reversed:", result)
