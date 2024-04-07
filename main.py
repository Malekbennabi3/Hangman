import random


class Hangman:
    s = ""
    m = []
    strikes = 8
    words = []  # ['amie', 'gramme', 'jeux', 'trierai', 'kata']
    word = ""
    let = []
    lang = 'en'

    def __init__(self, strikes=8, lang="en"):
        self.strikes = strikes
        self.fichier(f'{lang}.txt')
        self.word = self.words[int(random.random() * (len(self.words)))]

        for i in range(0, len(self.word)):
            self.m.append('_')
            self.s = self.s + '_'

        print("\nThe hidden word: " + self.s + "\n")

    def assign(self, c):

        self.let.append(c)

        if c in self.word:
            for i in range(0, len(self.m)):
                if self.word[i] == c:
                    self.m[i] = c
        else:
            self.strikes = self.strikes - 1
            print(f"False letter, you have {self.strikes}/8 left \n")

        print(self.chaine(self.m) + "\n")

    def played_let(self):
        print(f"You played the letters: {', '.join(self.chaine(self.let))}")

    def chaine(self, l):
        s = ""
        for i in range(0, len(l)):
            s = s + l[i]
        return s

    def fichier(self, nf):
        # Ouvrir le fichier en mode lecture
        with open(nf, 'r') as file:
            lines = file.readlines()  # Lire toutes les lignes du fichier

        # Supprimer les sauts de ligne ('\n') de chaque ligne et créer une liste
        lines_list = [line.strip() for line in lines if len(line.strip()) > 3]

        self.words = lines_list


if __name__ == '__main__':

    lang = input("ENGLISH (en) | or | FRENCH (fr) ? ")
    h = Hangman(8, lang)
    while h.strikes > 0:
        x = input("Play a letter: ")
        h.assign(x)
        h.played_let()
        if not '_' in h.m:
            h.strikes = 0
            print("You Win !")
        elif '_' in h.m and h.strikes == 0:
            print(f"\nYou lost !  ===> The word was '{h.word.capitalize()}'")
