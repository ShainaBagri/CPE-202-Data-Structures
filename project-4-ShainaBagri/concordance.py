from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            f = open(filename, "r")
            if f.mode == 'r':
                text = f.read()
            f.close()
        except:
            raise FileNotFoundError
        lis = text.split()
        self.stop_table = HashTable(191)
        for i in lis:
            self.stop_table.insert(i, None)

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        Process of adding new line numbers for a word (key) in the concordance:
            If word is in table, get current value (list of line numbers), append new line number, insert (key, value)
            If word is not in table, insert (key, value), where value is a Python List with the line number
        If file does not exist, raise FileNotFoundError"""
        try:
            f = open(filename, "r")
            if f.mode == 'r':
                text = f.readlines()
            f.close()
        except:
            raise FileNotFoundError
        self.concordance_table = HashTable(191)
        for i in range(len(text)):
            j = 0
            while j < len(text[i]):
                if text[i][j]=='-':
                    text[i] = text[i][:j] + " " + text[i][j+1:]
                elif (text[i][j] in string.punctuation) or (text[i][j] in string.digits):
                    text[i] = text[i][:j] + text[i][j+1:]
                else:
                    j += 1
            text[i] = text[i].lower()
            text[i] = text[i].split()
            text[i] = list(set(text[i]))
        for i in range(len(text)):
            for j in text[i]:
                if not self.stop_table.in_table(j):
                    if not self.concordance_table.in_table(j):
                        self.concordance_table.insert(j, [i+1])
                    else:
                        lis = self.concordance_table.get_value(j)
                        lis.append(i+1)
                        self.concordance_table.insert(j, lis)


    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        f = open(filename, "w")
        lis = self.concordance_table.get_all_keys()
        lis.sort()
        for i in range(len(lis)):
            file_string = lis[i] + ":"
            vals = self.concordance_table.get_value(lis[i])
            for j in vals:
                file_string = file_string + " " + str(j)
            if i==(len(lis)-1):
                f.write(file_string)
            else:
                f.write(file_string + "\n")
        f.close()