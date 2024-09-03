class Solution:
    def groupAnagrams(self, strings_list: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(List)

        for string in strings_list:
            sorted_string = "".join(sorted(string))
            # print(sorted_string)
            if sorted_string in anagram_groups:
                anagram_groups[sorted_string].append(string)
                # print(anagram_groups[sorted_string])
            else:
                anagram_groups[sorted_string] = [string]
                # print(anagram_groups[sorted_string])
                # print(anagram_groups)

        # Remember to return values of the default dictionary in form of a List
        return (anagram_groups.values())