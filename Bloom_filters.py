"""Use murmur package for hash functions"""
import mmh3

import numpy as np

import Helper

"""Bloom Filter Class"""
class Bloom_Filter:
    """Inititalization function that takes in the false positive rate
        and number of elements to be inserted"""
    def __init__(self,fp_rate,count):
        self.false_pos=fp_rate

        self.length=count

        """Calculate array size"""
        self.array_size=int((-(self.length)*np.log(self.false_pos))/(np.log(2)**2))

        """Initiate a numpy array with zeros"""
        self.array=np.zeros(self.array_size,dtype=int)

        """calculate the optimal number of hash functions needed"""
        self.hash_num=int(round((self.array_size/self.length)*np.log(2)))

    """Insertion method"""
    def insert(self,item):

        """hash the item to be inserted to different hash functions with different seed numbers"""
        for i in range(self.hash_num):

            """The result mod the size of the array to get the index"""
            index=mmh3.hash(item,i)%(self.array_size)

            """set the specific index to 1"""
            self.array[index]=1
        return

    """Search method"""
    def search(self,item):

        """Variable to indicate if the item is in the array"""
        found=0

        for i in range(self.hash_num):
            index=mmh3.hash(item,i)%(self.array_size)

            """If all the indices is already 1, then found=True"""
            if self.array[index]==1:
                found=found+1
            else:
                None

        return found==self.hash_num


"""TESTING"""
helper=Helper.Helpers()
helper.read_txt('sample.txt')
bf_test=Bloom_Filter(0.05,helper.word_count)

bf_test=Bloom_Filter(0.2,1500)
bf_test.array_size

for line in helper.words:
    for word in line.split():
        bf_test.insert(word)
