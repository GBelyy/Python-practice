import this
text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
"""text_dict = dict()  # Использование словаря 
for word in text.split():
    cleaned_word = word.strip(",.;:!").lower()
    if cleaned_word not in text_dict:
        text_dict[cleaned_word] = 0
    text_dict[cleaned_word] += 1
text_items = text_dict.items()
word_count_items = sorted(text_items, key = operator.itemgetter(1), reverse = True)
print(word_count_items[:3])"""
from collections import Counter  # Использование метода из модуля collections
cleaned_list = []
for word in text.split():
    cleaned_list.append(word.strip(",.;:!").lower())
print(Counter(cleaned_list).most_common(3))
