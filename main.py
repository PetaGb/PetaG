TEXTS = {1: '''
Situated about 10 miles west of Kemmerer,
Fossil Butte , is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         2: '''At the base of Fossil Butte are the bright
 red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         3: '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
         }

users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
separator = "-" * 40

username = input("Your username: ".upper())
password = input("Your password: ".upper())

print(separator)

if users.get(username) == password:
    print(f"Hello {username.title()}, welcome to our text analyser!")
else:
    print(f"You are not registered {username.title()}. Please register.")
    quit()

text_selection = input("There are 3 texts. Select number: ")

if not text_selection.isnumeric():
  print("You must select a number. Terminating.")
  quit()

else:
  text_selection = int(text_selection)
  if not text_selection in range(1,4):
    print("You must select a valid number. Terminating.")
    quit()

print(separator)


text_keys = TEXTS.keys()


if text_selection in text_keys:
    selected_text = TEXTS[text_selection]
    listed_text = selected_text.split()
    cleaned_text = []
    for word in listed_text:
      clean_word = word.strip(".,")
      if clean_word.isalnum():
        cleaned_text.append(clean_word)

    total = int(len(cleaned_text))
    print(f"There are {total} words in selected text.")
else:
    print(f"{text_selection} is not valid selection. Terminating")
    quit()

list_title = []

for word in cleaned_text:
    if word.istitle():
        list_title.append(word)
        total_titles = len(list_title)

print(f"There are {total_titles} titlecase words.")

list_upper = []

for word in cleaned_text:
    if word.isupper() and word.isalpha():
        list_upper.append(word)
        total_uppers = len(list_upper)

        if len(list_upper) == 0:
            print("There is no uppercase word.")
        elif len(list_upper) == 1:
            print("There is 1 uppercase word.")
        else:
            print(f"There are {total_uppers} uppercase words.")

list_lower = []

for word in cleaned_text:
    if word.islower():
        list_lower.append(word)
        total_lowers = len(list_lower)

print(f"There are {total_lowers} lowercase words.")

list_numbers = []

for word in cleaned_text:
    if word.isnumeric():
        list_numbers.append(word)
        total_numbers = len(list_numbers)
if len(list_numbers) == 1:
    print("There is one number.")
else:
    print(f"There are {total_numbers} numbers.")

list_numbers = []

for word in cleaned_text:
    if word.isnumeric():
        word = int(word)
        list_numbers.append(word)
        sum_numbers = sum(list_numbers)

print(f"The sum of all numbers is {sum_numbers}.")

print(separator)

print("|RANK|  WORD LENGHT  |OCC.|")

print(separator)

new_text = []

for word in cleaned_text:
    word = "*" * len(word)
    new_text.append(word)

dict_text = {}

for word in new_text:
    if word not in dict_text:
        dict_text[word] = 1
    else:
        dict_text[word] = dict_text[word] + 1

sorted_words: list = sorted(list(dict_text.values()), reverse=True)[0:]

result = list()

for occurance in dict_text:
    if dict_text[occurance] in sorted_words:
        result.append((dict_text[occurance], occurance))

for index, tupl in enumerate(sorted(result, reverse=True), 1):
    if index < 10:
        print(f"| {index}. |{tupl[1]: ^15}|{tupl[0]}x |")
    else:
        print(f"|{index}. |{tupl[1]: ^15}|{tupl[0]}x |")
