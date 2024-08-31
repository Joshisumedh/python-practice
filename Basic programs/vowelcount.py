#python program to count number of each vowel
word = input("Enter the word : ")
vowels = 'aeiouAEIOU'
count = {vowel: 0 for vowel in vowels}
for char in word:
    if char in count:
        count[char] += 1
    
print(count)