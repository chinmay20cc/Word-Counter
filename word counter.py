def count_words(text):
    """
    Counts the number of words in the given text.

    Args:
        text (str): The text to count words in.

    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)

def main():
    """
    Main function to run the word counting program.
    """
    print("Welcome to the Word Counter Program developed by Chinmay Choudhari!")
    
    
    user_input = input("Please enter a sentence or paragraph from which you would like to calculate the number of words : ").strip()
    
    
    if not user_input:
        print("Error: No input provided. Please enter some text.")
        return
    
    
    word_count = count_words(user_input)
    
    
    print(f"The number of words in the given text is: {word_count}")

if __name__ == "__main__":
    main()
