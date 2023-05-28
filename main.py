# By Zain Zubair
# 1007 Translator

# main function
def main():
    lst1 = []

    # asks user for a sentence to convert
    txt = input("Enter a sentence to convert: ")

    # iterates through the letters in the text
    for letter in txt:
        # if the letter is not a capital or lower case letter or a space, then do not add the letter to the list
        if not ((65 <= ord(letter) <= 90) or (97 <= ord(letter) <= 122) or (ord(letter) == 32)):
            pass
        # else, append to list
        else:
            lst1.append(letter)

    # converts the list into a string
    text = ''
    for elem in lst1:
        text += str(elem)

    # calls to functions defined below
    upper = acronym_upper(text)
    split = my_split(upper)
    acr = acronym(split)
    lower = acr_lower(acr)
    # prints a line with acronyms
    print(lower)
    hom = homoglyph(lower)
    # prints a line with acronyms and homoglyphs
    print(hom)


# function for making the string upper case
def acronym_upper(string):
    text = ''
    # iterates through letter in string
    for item in string:
        # if the item is not a space (' '):
        if ord(item) != 32:
            # if item is not already an upper case letter, convert to upper case
            if 97 <= ord(item) <= 122:
                lower = (ord(item)) - 32
                new_letter = chr(lower)
                text += new_letter
            # else, just add already upper-cased letter
            else:
                text += item
        # else, add space
        else:
            text += ' '

    # return the upper string
    return text


# function for making the string lower case except for the acronyms
def acr_lower(string):
    text = ''
    # defines list of acronyms
    acr = ['BTW', 'GTG', 'LMK', 'BRB']
    # iterates through the words of the string using the split function defined below
    for word in my_split(string):
        # if the word is not in the list of acronyms, then lower-case each letter of the word
        if word not in acr:
            for letter in word:
                lower = (ord(letter)) + 32
                text += chr(lower)
            text += ' '
        # else, add the word
        else:
            text += (word + ' ')

    # return the lower string
    return text


# function to split a sentence into different words and return them in a list
def my_split(sentence):
    temp = ''
    splt_lst = []
    # iterates through the letters in the sentence
    for letter in (sentence + ' '):
        # if the element is not a space, then add the letter to temp
        if ord(letter) != 32:
            temp += letter
        # if the word reaches its end (reaches a space), add temp to the list and set temp == ''
        else:
            splt_lst.append(temp)
            temp = ''

    # return the split list
    return splt_lst


# function for turning a list into a string
def join_list(a_list):
    sntnce = ''
    # iterates through words in the list
    for words in a_list:
        # the words are added to the string followed by a space
        sntnce += str(words)
        sntnce += ' '

    # returns the string
    return sntnce


# function to replace sentences with their appropriate acronym
def acronym(upper_str):
    count = -1
    # iterates through the words in the list
    for i in upper_str:
        count += 1

        # if the word in the string is 'BY', and is followed by 'THE WAY', remove those three words and replace with
        # 'BTW'. Same process for all other words
        if (upper_str[count] == 'BY') and (upper_str[count + 1] == 'THE') and (upper_str[count + 2] == 'WAY'):
            upper_str.pop(count + 2)
            upper_str.pop(count + 1)
            upper_str.pop(count)
            upper_str.insert(count, 'BTW')

        elif (upper_str[count] == 'GOT') and (upper_str[count + 1] == 'TO') and (upper_str[count + 2] == 'GO'):
            upper_str.pop(count + 2)
            upper_str.pop(count + 1)
            upper_str.pop(count)
            upper_str.insert(count, 'GTG')

        elif (upper_str[count] == 'LET') and (upper_str[count + 1] == 'ME') and (upper_str[count + 2] == 'KNOW'):
            upper_str.pop(count + 2)
            upper_str.pop(count + 1)
            upper_str.pop(count)
            upper_str.insert(count, 'LMK')

        elif (upper_str[count] == 'BE') and (upper_str[count + 1] == 'RIGHT') and (upper_str[count + 2] == 'BACK'):
            upper_str.pop(count + 2)
            upper_str.pop(count + 1)
            upper_str.pop(count)
            upper_str.insert(count, 'BRB')

    return join_list(upper_str)


# function for turning specific letters into homographs
def homoglyph(string):
    text = ''
    count = 0
    # convert string to list so it is easier to iterate
    lst = list(string)

    # if the letter in the list is one of the specific letters, remove that letter and insert the appropriate
    # homoglyph into its index
    for letter in lst:
        if letter == 'i':
            lst.remove('i')
            lst.insert(count, '][')
        elif letter == 'a':
            lst.remove('a')
            lst.insert(count, '@')
        elif letter == 'h':
            lst.remove('h')
            lst.insert(count, '|-|')
        elif letter == 'u':
            lst.remove('u')
            lst.insert(count, '|_|')
        count += 1

    # convert the list into a string
    for i in lst:
        if i != ' ':
            text += i
        else:
            text += ' '

    # return the string
    return text


# call to main function
main()

# End 1007 Translator
