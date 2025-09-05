import string
import sys
import os

def average_word_length(text: str) -> str:
    """
    Calculate the average word length in a given text.
    Cleans punctuation, ignores numbers, and handles empty input.
    
    Parameters:
        text (str): The input text.
    
    Returns:
        str: A formatted string with the average word length.
    """
    words = text.split()
    
    cleaned_words = []
    for word in words:
        # Remove punctuation
        word = word.strip(string.punctuation)
        
        # Keep only alphabetic words (ignore numbers/mixed tokens)
        if word.isalpha():
            cleaned_words.append(word)
    
    if not cleaned_words:
        return "No valid words found in the input."
    
    # Compute average length
    total_length = sum(len(word) for word in cleaned_words)
    avg_length = total_length / len(cleaned_words)
    
    return f"Average word length: {avg_length:.2f}"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Read from file if filename provided
        filename = sys.argv[1]
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            sys.exit(1)
        
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        # Fall back to user input
        text = input("Enter some text: ").strip()
    
    if not text:
        print("Input was empty. Please provide some text or a valid file.")
    else:
        result = average_word_length(text)
        print(result)
