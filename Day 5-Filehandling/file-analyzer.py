with open("C:/Users/Hp/OneDrive/Desktop/AI-Ml-Journey/Day 5-Filehandling/data.txt", "r", encoding="utf-8") as file:
    content = file.read().strip()  
    words = content.split()  
    print(f"Total Words = {len(words)}")

    
    if content:
        lines = content.count('\n') + 1
    else:
        lines = 0
    print(f"Total Lines = {lines}")

    
    word_count = {}
    for word in words:
        
        clean_word = word.strip(".,!?:;\"'").lower()  
        if clean_word: 
            word_count[clean_word] = word_count.get(clean_word, 0) + 1

    
    if word_count:
        most_frequent_word = max(word_count, key=word_count.get)
        frequency = word_count[most_frequent_word]
        print(f"Most frequent word: '{most_frequent_word}' (appears {frequency} times)")
    else:
        print("No words found in the file.")

   


