def word_count(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def frequency(text):
    char_frequency = {}
    for ch in text: 
        count = 1
        if ch not in char_frequency:
            if ch == " ":
                continue
            char_frequency[ch] = count
        elif ch in char_frequency:
            char_frequency[ch] += 1
    return char_frequency

def long_word(text):
    words = text.split()
    max_len = 0
    max_word = None
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
            max_word = word
        else:
            continue
    return max_word

def avg_len(text):
    count = word_count(text)
    ch_count = 0
    words = text.split()
    for word in words:
        ch_count += len(word)
    avg_word_len = ch_count / count
    return avg_word_len

def main():
    user = input("Enter the text: ")
    count = word_count(user)
    freq = frequency(user)
    long = long_word(user)
    average = avg_len(user)
    print(f"1. Word Count: {count}\n2. Character Frequency: {freq}\n3. Longest Word: {long}\n4. Average Word Length: {average}")

main()