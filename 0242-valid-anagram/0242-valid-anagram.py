class Solution:
    def isAnagram(self, first_string: str, second_string: str) -> bool:
        first_dictionary = {}
        second_dictionary = {}

        if len(first_string) == len(second_string):
            for char in first_string:
                if char in first_dictionary : 
                    first_dictionary[char] += 1
                else:
                    first_dictionary[char] = 1
            # print(first_dictionary)
            
            for char in second_string:
                if char in second_dictionary : 
                    second_dictionary[char] += 1
                else:
                    second_dictionary[char] = 1
            # print(second_dictionary)
            return (first_dictionary == second_dictionary)

