"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Anetta Martináková
email: martinakova.anetta@gmail.com
discord: Anetta M.#5044
"""

with open('texts.txt', 'r') as file:
    text = file.read()

TEXTS = [paragraph.strip() for paragraph in text.split('\n\n') if paragraph.strip()]

credentials = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

username = input("Username: ")
password = input("Password: ") # Vyžádá si od uživatele přihlašovací jméno a heslo
dash_line = "-" * 40


# if username.lower() in credentials and credentials[username.lower()] == password:
if credentials.get(username.lower()) == password:
    print(f"Welcome to the app {username}.\nWe have 3 texts to be analyzed.")
    # 3. zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,
    # 4. pokud je registrovaný, pozdrav jej a umožní mu analyzovat texty,
    print(dash_line)
else:
    print(f"username: {username} \n" 
          f"password: {password} \n"
          f"unregistered user, terminating the program..") # pokud není registrovaný, upozorni jej a ukončí program
    quit()

text_number = input("Enter a number btw. 1 and 3 to select: ")
# Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS


if not text_number.isdigit():
    print(f"{text_number} is not a number!")
    # pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.

elif int(text_number) not in range(1, 4):
    print(f"{text_number} is not btw. 1 and 3.")
    # Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí.

else:
    print(dash_line)
    # analyza textu
    paragraph = TEXTS[int(text_number) - 1]  # priradi odpovidajici odstavec
    words = paragraph.split()  # rozdeli odstavec na slova
    word_count = len(words)
    capitalized_count = 0
    uppercase_word_count = 0
    lowercase_word_count = 0
    numbers_count = 0
    numbers_sum = 0

    for word in words:
        if word.istitle():  # slova zacinajici velkym pismenem
            capitalized_count += 1
        if word.isupper() and word.isalpha():  # slova psana velkymi pismeny
            uppercase_word_count += 1
        if word.islower():  # slova psana malymi pismeny
            lowercase_word_count += 1
        if word.isnumeric():    # pocet cisel
            numbers_count += 1
        if word.isdigit():      # suma vsech cisel
            numbers_sum += int(word)

    print(f"There are {word_count} words in the selected text.\n"
          f"There are {capitalized_count} tittlecase words.\n"
          f"There are {uppercase_word_count} uppercase words.\n"
          f"There are {lowercase_word_count} lowercase words.\n"
          f"There are {numbers_count} numeric strings.\n"
          f"The sum of all numbers {numbers_sum}.")
    print(dash_line)

    word_lengths = {} # prazdny slovnik do ktereho ulozime delku slov

    for word in words:
        length = len(word) # pro kazde slovo v textu vypocitame delku daneho slova
        if length in word_lengths:
            word_lengths[length] += 1  # pokud je delka slova pritomna ve slovniku jako klic - pricteme k hodnote + 1
        else:
            word_lengths[length] = 1  # pokud delka slova ve slovniku neni nastavime hodnotu na 1

    max_length = max(word_lengths.keys()) # maximalni delka slova
    min_length = min(word_lengths.keys()) # minimalni delka slova

    print("LEN | OCCURRENCES | NR.")
    print(dash_line)

    for length in range(min_length, max_length + 1): # iterujeme pres vytvoreni slovnik delek slov
        freq = word_lengths.get(length, 0)           # pro kazdou delku slova zjistime kolikrat tam takove slovo je
        print(f"  {length:2}| {'*' * freq} {freq}")