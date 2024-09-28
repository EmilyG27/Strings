count = 0
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
positive_words = str(positive_words)
negative_words = str(negative_words)
reviews_stringed = str(reviews)
words_list = ["good", "excellent", "bad", "poor", "average"]

good = reviews_stringed.count("good")
excellent = reviews_stringed.count("excellent")
great = reviews_stringed.count("great")
awesome = reviews_stringed.count("awesome")
fantastic = reviews_stringed.count("fantastic")
superb = reviews_stringed.count("superb")
amazing = reviews_stringed.count("amazing")

bad = reviews_stringed.count("bad")
poor = reviews_stringed.count("poor")
terrible = reviews_stringed.count("terrible")
horrible = reviews_stringed.count("horrible")
awful = reviews_stringed.count("awful")
disappointing = reviews_stringed.count("disappointing")
subpar = reviews_stringed.count("subpar")

for words in words_list:
    reviews_stringed = reviews_stringed.replace(words, words.upper())
print(reviews_stringed)
#Task 2
print(f"Positive words appear", good + excellent + great + awesome + fantastic + superb + amazing, "times.")
print(f"Negative words appear", bad + poor + terrible + horrible + awful + disappointing + subpar, "times.")
#Task 3
dots = "..."
preview = [x('\W+'[:30]) + dots for x in reviews]
print(preview)