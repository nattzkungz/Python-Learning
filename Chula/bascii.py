def vowel_const_average(filename):
    max_vow = 0
    max_const = 0
    word_count = 0
    total_length = 0
    vow_word = ""
    const_word = ""
    file = [_.strip("\n").split() for _ in open(filename, "rt").readlines()]
    vowel_list = ["a", "e", "i", "o", "u"]

    def counter(word, which):
        count = 0
        global word_count
        for i in word:
            if which == "consonant":
                if i not in vowel_list:
                    count += 1
            else:
                if i in vowel_list:
                    count += 1
        return count

    for i in file:
        for j in i:
            word_count += 1
            total_length += len(j)
            vow = counter(j, "vowel")
            const = counter(j, "consonant")

            if vow > max_vow:
                max_vow = vow
                vow_word = j
            if const > max_const:
                max_const = const
                const_word = j

    avg_length = total_length/word_count
    return vow_word, const_word, avg_length


print('This program finds the word with the most vowels and')
print('the word with the most consonants')
print('It also calculates the average word length')
vowel, const, average = vowel_const_average(input("Enter file name: "))
print('The word with the most vowels is: ',vowel)
print('The word with the most consonanrs is: ', const)
print('The average word length is: ', average)

# b = open("C:\\Users\\daran\\OneDrive\\Desktop\\VSCode\\Python-Learning\\Chula\\heyt.txt")
# print(b)

### Old code


# def vowel_const_average(filename):
#     infile = open(filename, 'r')
#     text = infile.read().split(' ')

#     max_vow = max_const = 0
#     vowel = const = 0
#     wordcount = 0
#     lettercount = 0

#     for word in text:
#         #average
#         wordcount = wordcount + 1
#         lettercount = lettercount + len(word)

#         #vowels
#         vow ='aeiou'
#         vow_len = len([word for word in text if word in vow])
#         if vow_len > max_vow:
#             vowel = word
#             max_vow = vow_len

#         #consonant
#         consonants =  ['b','c','d','f','g','h','i','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
#         con_len = len([word for word in text if word in consonants])
#         if con_len > max_const:
#             const = word
#             max_const = con_len

#     return vowel, const, int(lettercount/wordcount)

# print('This program finds the word with the most vowels and')
# print('the word with the most consonants')
# print('It also calculates the average word length')
# filename = input("Enter filename: ")
# vowel, const, average = vowel_const_average(filename)
# print('The word with the most vowels is: ',vowel)
# print('The word with the most consonanrs is: ', const)
# print('The average word length is: ', average)