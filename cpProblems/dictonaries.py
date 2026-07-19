class Solution:

    # A Python dictionary is a built-in, mutable, and unordered collection of key-value pairs.
    # Keys must be unique and immutable (like strings or numbers), 
    # while values can be any data type, data exists as pairs, orsorting in keys
    # Internally, they use hash tables: key-> hash func ->value
    # on avg op : O(1), worst: O(n)
    # when to use?
        # Data has unique identifiers
        # Fast lookup is required
        # need structured information
    # when to use list & dictionary
        # list-> order is required
        # dictonary-> faster access
    def usea_of_dictionaries(self,st):
        dictonary_a={}
        dictonary_a={
            "A":2,
            "B":3,
            "AB":2
        }