import random
import string

def getting_words():
    #getting nouns and adjectives
    adjectives = ["Happy", "Cool", "Funky", "Quick", "Charming", "Brave","Mysterious","Vivid","Daring","Energetic"]
    nouns = ["Tiger", "Dragon", "Phoenix", "Knight", "Unicorn", "Wizard","Samurai","Falcon","Panther","Cobra"]
    return adjectives, nouns

def generateUsername(adjectives, nouns, include_nums, include_special_char, structure="A-N"):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = ""

    if structure == "A-N":
        username = f"{adjective}{noun}"
    elif structure == "N-A":
        username = f"{noun}{adjective}"
    elif structure == "A#N":
        special_char = include_special_char if include_special_char else random.choice(string.punctuation)
        if special_char == "!":
            username = f"{adjective}{noun}{special_char}"
        else:
            username = f"{adjective}{special_char}{noun}"
        
    elif structure == "A-N99":
        if(include_nums==None):
            number = str(random.randint(10, 99))
            username=f"{adjective}{noun}{number}"
        else:
            number=include_nums
            username = f"{adjective}{noun}{number}"
    elif structure == "A#N99":
        number=include_nums
       
        if(include_nums==None):
            number=str(random.randint(10, 99))
        special_char = include_special_char if include_special_char else random.choice(string.punctuation)
        if(special_char=="!"):
            username=f"{adjective}{noun}{number}!"
        else:
            username=f"{adjective}{special_char}{noun}{number}"
    elif structure == "AN#99":
        number=include_nums
       
        if(include_nums==None):
            number=str(random.randint(10, 99))
        special_char = include_special_char if include_special_char else random.choice(string.punctuation)
        if(special_char=="!"):
            username=f"{adjective}{noun}{number}!"
        else:
            username=f"{adjective}{noun}{special_char}{number}"
    return username

def save_usernames_to_file(usernames, filename="usernames.txt"):
    """Save generated usernames to a file."""
    with open(filename, "a") as file:  # Append mode to continue writing
        for username in usernames:
            file.write(username + "\n")


def main():
    adjectives,nouns=getting_words()
    print("Welcome to Username Generator")
    
    accept="c"
    while(accept=="c"):
        try:
            include_nums=int(input("Enter a number of choice or skip:- "))
        except:
            include_nums=None
        try:
            include_special_char=input("Enter a special char or skip:- ")
            if include_special_char not in string.punctuation:
                include_special_char=None
        except:
            include_special_char=None

        print("Choose a structure: \nA-N(Adjective-noun)\n N-A(noun-adjective)\n A#N(adjective-special char-noun)\n A-N99(Adjectve-noun-number)\n A#N99(adjective-noun-number)\n AN#99(adjective-noun-special char-number)\n")
        structure = input("Enter your choice (or press Enter to use default A-N): ").strip().upper()
        if not structure:
            structure = "A-N"
        try:
            count = int(input("How many usernames would you like to generate?   "))
        except:
            count=5
        usernames = [
            generateUsername(adjectives, nouns, include_nums, include_special_char,structure)
            for _ in range(count)
        ]
        print("\nGenerated Usernames:")
        for username in usernames:
            print(username)
        try:
            save_option = input("Would you like to save these usernames to a file? (y/n):  ").strip().lower()
        except:
            save_option="n"
        if save_option == "y":
            save_usernames_to_file(usernames)
            print(f"Usernames saved to 'usernames.txt'.")
        
        accept=input("Type c to continue:- ")

if __name__ == "__main__":
    main()