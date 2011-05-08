from sequence import sequence, getStrippedLetter
import unittest

class StrippedLetter(unittest.TestCase):
    
    def test_letter(self):
        self.assertEquals(getStrippedLetter("abc"), "a")
    
    def test_punctuation(self):
        self.assertEquals(getStrippedLetter("!abc"), "a")
        self.assertEquals(getStrippedLetter("!,+abc"), "a")
        self.assertEquals(getStrippedLetter("abc!"), "a")


class Identity(unittest.TestCase):
   
    def test_singleItem(self):
        """Single-item string"""
        string = "A"
        self.assertEquals(sequence(string), string)
   
    def test_alphabatized(self):
        """Alphabatized string"""
        string = "A B C D E"
        self.assertEquals(sequence(string), string)
    
    def test_alphabatizedSingleException(self):
        """Alphabatized string with a single exception"""
        string = "A C B D E F G"
        self.assertEquals(sequence(string), string)
    
    def test_equalString(self):
        """String with all equal elements"""
        string = "A A A A A A A A A A A A A"
        self.assertEquals(sequence(string), string) 
    
    def test_mixedCase(self):
        """Mixed case"""
        string = "a B c D e F g"
        self.assertEquals(sequence(string), string)        



class Substring(unittest.TestCase):

    def test_singleException(self):
        """Single exception sequence"""
        string = "Z C B A"
        self.assertEquals(sequence(string), "Z C")          

    def test_endOfString(self):
        """Sequence occurs at end-of-string"""
        string = "Z Y X A B C"
        self.assertEquals(sequence(string), "A B C")  
        
    def test_simpleDoubleException(self):
        """Simple string with two exceptions"""
        string = "A Z B A"
        self.assertEquals(sequence(string), "A Z B")
        
        string = "Z Y X C A"
        self.assertEquals(sequence(string), "Z Y")

    def test_multipleAlphabatized(self):
        """Multiple alphabatized substrings of different lengths"""
        string = "A Z Y B C Z Y D E F Z Y G H I J K L M"
        self.assertEquals(sequence(string), "G H I J K L M")
    
    def test_multipleAlphabatizedEndWithException(self):
        """Multiple alphabatized substrings of different lengths, ending with an exception"""
        string = "A Z Y B C Z Y D E F Z Y G H I J K L M A"
        self.assertEquals(sequence(string), "G H I J K L M A")   



class ProblemDefinition(unittest.TestCase):
    def test_initial(self):
        """Initial example given in problem definition e-mail"""
        string = "Write a program that reports the longest sequence of words that appear " \
                 "in alphabetical order in a given input text, with at most one " \
                 "exception (break in ascending alphabetical order)."
        result = "a given input text, with at most one"
        self.assertEquals(sequence(string), result)    
    
    def test_roster(self):
        """Examples given in "roster" email clarification"""
        string = "Abrahams, Adams, Bartholomew, Monroe, Windsor"
        self.assertEquals(sequence(string), string)
        
        string = "Abrahams, Adams, Monroe, Bartholomew, Windsor"
        self.assertEquals(sequence(string), string)
        
        string = "Abrahams, Monroe, Adams, Windsor, Bartholomew"
        self.assertEquals(sequence(string), "Abrahams, Monroe, Adams, Windsor,")
        
        string = "Abrahams, Bartholomew, Windsor, Adams, Monroe"
        self.assertEquals(sequence(string), string)             


if __name__ == "__main__":
    unittest.main()