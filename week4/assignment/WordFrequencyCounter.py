# Word Frequency Counter
import string
 
 
def word_frequency(text):
    words = text.lower().split()
    cleaned = [w.strip(string.punctuation) for w in words]
 
    counts = {}
    for w in cleaned:
        if w:
            counts[w] = counts.get(w, 0) + 1
 
    top3 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]
    return top3
 
 
text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""
 
top3 = word_frequency(text)
print("Top 3 words:")
for word, count in top3:
    print(f"{word} — {count} times")
