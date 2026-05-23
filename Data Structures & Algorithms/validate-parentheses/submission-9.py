class Solution:
    def isValid(self, s: str) -> bool:
        brackets_dict = {"}":"{", ")":"(", "]":"["}
        storage_list = []
        for i in range(len(s)):
            if s[i] not in brackets_dict:
                storage_list.append(s[i])
            else:
                if storage_list and storage_list[-1] == brackets_dict[s[i]]:
                    storage_list.pop()
                else:
                    return False
        return not bool(storage_list)
        