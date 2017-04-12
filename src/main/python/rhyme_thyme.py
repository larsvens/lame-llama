import sys
import nltk

class RhymeThyme(object):

    def rhyme_thyme(self, word):
        # Check if word or sentence
        if len(word.split(' ')) > 1: self.ws = 'sentence'
        else: self.ws = 'word'

        if word == "Your mama is so fat...":
            return "...she just had a baby and said it was delicious ;)"

        # get dictionary from nltk
        entries = nltk.corpus.cmudict.entries()

        output = ''

        for word in word.split(' '):

            # Let syllables be the array of syllables which rhyme with the input word
            syllables = [syl for inp, syl in entries if inp == word]

            # Number of characters in end of syllable which have to agree in order to rhyme
            level = 5

            # Loop through syllables and choose the words which have syllables..
            rhymes = []
            for syllable in syllables:
                rhymes += [inp for inp, pron in entries if pron[-level:] == syllable[-level:]]

            # Remove the duplicate rhymes by using set(), and then convert to list()
            possibleRhymes  = [str(rhyme) for rhyme in rhymes]
            possibleRhymes = list(set(possibleRhymes))
            # Make sure that output word is not the same as input word
            if len(possibleRhymes) > 0:
                possibleRhymes.remove(word)

            allwords = [str(oneword) for oneword in nltk.corpus.words.words()]
            possibleRhymes = [x for x in possibleRhymes if x in allwords]
            if len(possibleRhymes) == 0:
                output += 'Failed to find rhyming word... '
            else:
                # Output one answer
                output += str(possibleRhymes[0]) + ' '


        return output

    def input_from_user(self):
        # Input word
        version_info = sys.version_info[:2]
        using_python_v3 = version_info[0] == 3
        out_str = 'Input word or sentence:   '
        word = input(out_str) if using_python_v3 else raw_input(out_str)
        return word

    def output_to_user(self, word):
        # Output word to user
        text = 'Rhyming '+ self.ws + ': ' + word
        print(text)
        return text

    def print_welcome_text(self):
        text = "Welcome to Rhyme Thyme - the awesome rhyming time. \n"
        print(text)
        return text

    def print_goodbye_text(self):
        text = "Goodbye!\n" 
        print(text)
        return text

    def __init__(self):
        self.print_welcome_text()
        word = self.input_from_user()
        self.output_to_user(self.rhyme_thyme(word))

if __name__ == '__main__':
    RhymeThyme()
