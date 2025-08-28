sentence=input()
word_to_count_frequency=input()
count=0
if word_to_count_frequency in sentence:
  print(sentence.count(word_to_count_frequency))
else:
  print("word not found")
