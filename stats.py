
def get_num_words(text):
    return len(text.split())

def get_character_counts(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def get_counts_sorted(counts):
    sorted_counts = []
    for char in counts:
        if char.isalpha():
            sorted_counts.append({"char": char, "count": counts[char]})
    return sorted(sorted_counts, key=lambda x: x["count"], reverse=True)


