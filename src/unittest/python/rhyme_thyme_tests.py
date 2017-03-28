import unittest
from nltk.corpus import words
from rhyme_thyme import RhymeThyme

class test_rhyme_thyme(unittest.TestCase):

    def test_rhyme_thyme(self):
        self.assertTrue(type(RhymeThyme.rhyme_thyme(self,'abcd') == str), 'Not returning a string')
        self.assertTrue(len(RhymeThyme.rhyme_thyme(self, 'abcd')) > 0, 'Returning empty word')
        self.assertTrue((RhymeThyme.rhyme_thyme(self,'pear') in words.words()) or RhymeThyme.rhyme_thyme(self,'pear') == 'Failed to find rhyming word...', 'Not returning proper english word')

    def test_goodbye(self):
        text = 'Goodbye!\n'
        self.assertEqual(RhymeThyme.print_goodbye_text(self), text, 'Not printing goodbye text properly!')
    
    def test_welcome(self):
        text = "Welcome to Rhyme Thyme - the awesome rhyming time. \n"
        self.assertEqual(RhymeThyme.print_welcome_text(self), text, 'Not printing welcome text properly!')

    def test_output_to_user(self):
        word = 'whazzup'
        text = 'Rhyming word:  ' + word
        self.assertEqual(RhymeThyme.output_to_user(self, word), text, 'Not outputting to user properly!')
