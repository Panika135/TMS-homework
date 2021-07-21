text = 'Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a ' \
       'simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, ' \
       'together with its interpreted nature, make it an ideal language for scripting and rapid application ' \
       'development in many areas on most platforms.'


text = '' .join(word for word in text if word != ',' and word != '.')
text = text.replace('-', ' ')
list_word_text = text.split()
dict_word = {word : 0 for word in list_word_text }
list_max_len = [list_word_text[0]]
for word in list_word_text:
       dict_word[word] += 1
       if len(word) > len(list_max_len[0]):
              list_max_len = [word]
       elif len(word) == len(list_max_len[0]):
              list_max_len.append(word)


print(set(list_max_len))


list_k_v = [(k, v) for k, v in dict_word.items()]
list_k_v.sort(key= lambda i : i[1], reverse=True)
print(list_k_v[0][0], 'повторился', list_k_v[0][1], 'раза')