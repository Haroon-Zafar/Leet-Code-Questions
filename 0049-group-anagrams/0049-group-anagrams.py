class Solution:
    def groupAnagrams(self, string_list: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for string in string_list:
            sorted_string = "".join(sorted(string))
            anagram_groups[sorted_string].append(string)
            
            
        return list(anagram_groups.values())
        