# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
vowels_sum = 0
for letter in word.lower():
    if letter in vowels:
        vowels_sum += 1
print(vowels_sum)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    letter = word[0]
    print(letter)
### Комментарий Яны: чувствствую, тут что-то не так должно быть, но на отдельной же выводит... Надо было продемонстрировать знание \n?

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words_length = 0
for word in sentence.split():
    words_length += len(word)
print(words_length/len(sentence.split()))
    