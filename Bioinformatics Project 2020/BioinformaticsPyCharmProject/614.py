import random

# Εισάγουμε στις μεταβλητές τύπου string τις αντίστοιχες ακολουθίες απο τα αρχεία 614Α και 614Β.
with open('614A', 'r') as file:
    akoluthia1 = file.read().replace('\n', '')

with open('614B', 'r') as file:
    akoluthia2 = file.read().replace('\n', '')


# Μετατρέπουμε τις μεταβλητές μας σε λίστες.
wordList1 = list(akoluthia1)
wordList2 = list(akoluthia2)

# Πέρνουμε το μήκος της κάθε ακολουθίας.
lengthWord1 = len(akoluthia1)
lengthWord2 = len(akoluthia2)

# Παίζει πρώτος ο παίχτης 1
player = 1

# Με την χρήση του συγκεκριμένου while loop θέσαμε ένα όριο για το μέχρι πότε θα συνεχίζεται το παιχνίδι με βάση
# το μήκος της κάθε αλληλουχίας σε κάθε γύρο.
# Το παιχνίδι θα σταματάει όταν ο παίχτης που είναι η σειρά του δεν μπορεί να κάνει κίνηση, δηλαδή το μήκος της κάθε
# αλληλουχίας δεν τηρεί τον παρακάτω περιορισμό.
while (len(wordList1) >= 1 and len(wordList2) >= 2) or (len(wordList1) >= 2 and len(wordList2) >= 1):

    # (Τελευταίος γύρος) Αν το μήκος της 1ης ακολουθίας είναι ίσο με 1 ο παίχτης που παίζει αφαιρεί ενα νουκλεοτήδιο
    # από αυτήν και δύο απο την άλλη.
    if (len(wordList1) == 1) and (len(wordList2) > 1):
        position1 = random.randint(0, len(wordList1) - 1)
        wordList1.pop(position1)
        for i in range(2):
            position2 = random.randint(0, len(wordList2) - 1)
            wordList2.pop(position2)
        if player == 1:
            player = 2
        else:
            player = 1

    # (Τελευταίος γύρος) Αλλιώς αν το μήκος της 2ης ακολουθίας είναι ίσο με 1 ο παίχτης που παίζει αφαιρεί ένα
    # νουκλεοτήδιο από αυτήν και δύο απο την άλλη.
    elif (len(wordList1) > 1) and (len(wordList2) == 1):
        for i in range(2):
            position1 = random.randint(0, len(wordList1) - 1)
            wordList1.pop(position1)
        position2 = random.randint(0, len(wordList2) - 1)
        wordList2.pop(position2)
        if player == 1:
            player = 2
        else:
            player = 1
    # Αν ο γύρος δεν είναι ο τελευταίος τότε οι παίχτες μας διαλέγουν τυχαία .
    else:
        # Οι τυχαίοι αριθμοί wordListNumber 1,2 καθορίζουν από ποιά λίστα θα αφαιρεθούν πρώτα νουκλεοτήδια.
        wordListNumber = random.randint(1, 2)

        # Αν ο αριθμός selrand είναι 1 τότε βγάζει ένα νουκλεοτήδιο αλλιώς αν είναι 2 βγάζει 2.
        selrand = random.randint(1, 2)

        # Σύμφωνα με τις οδηγίες της άσκησης ο κάθε παίχτης στην σειρά του θα μπορεί να αφερεί 2 νουκλεοτήδια απο την
        # μία αλληλουχία (είτε την πρώτη είτε την δεύτερη) και 1 νουκλεοτήδιο από την άλλη.
        # Ο κάθε παίχτης παίζει εναλάξ. Αν η μεταβλητή player είναι 1 παίζει ο πρώτος αλλιώς αν είναι 2 ο δεύτερος.
        if wordListNumber == 1:

            if selrand == 1:
                position1 = random.randint(0, len(wordList1) - 1)
                wordList1.pop(position1)
                for i in range(2):
                    position2 = random.randint(0, len(wordList2) - 1)
                    wordList2.pop(position2)
                if player == 1:
                    player = 2
                else:
                    player = 1

            else:
                for i in range(2):
                    position1 = random.randint(0, len(wordList1) - 1)
                    wordList1.pop(position1)
                position2 = random.randint(0, len(wordList2) - 1)
                wordList2.pop(position2)
                if player == 1:
                    player = 2
                else:
                    player = 1

        else:

            if selrand == 1:
                position2 = random.randint(0, len(wordList2) - 1)
                wordList2.pop(position2)
                for i in range(2):
                    position1 = random.randint(0, len(wordList1) - 1)
                    wordList1.pop(position1)
                if player == 1:
                    player = 2
                else:
                    player = 1

            else:
                for i in range(2):
                    position2 = random.randint(0, len(wordList2) - 1)
                    wordList2.pop(position2)
                position1 = random.randint(0, len(wordList1) - 1)
                wordList1.pop(position1)
                if player == 1:
                    player = 2
                else:
                    player = 1

# Εμφανίζουμε τον παίχτη που κέρδισε
print("Κέρδισε ο παίχτης: ")
print(player)
