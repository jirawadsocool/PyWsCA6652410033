print ('+++++++++++++++++++++++++++++')

words1 = input("ป้อนข้อความ : ")

words2 = words1.split()

tatal_words = len(words1)

un_words = set(words1)

word_counts = {}
for word in words2:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("ประโยคนี้มี {} คำ".format(tatal_words))
print("คำที่แตกต่างกันมี {} คำ".format(len(un_words)))
for word, count in word_counts.items():
    if count > 1:
        print("The word '{}' occurs {} times.".format(word, count))