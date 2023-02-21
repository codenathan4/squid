class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        def nested_integer():
            global i
            if s[i] in '-0123456789':
                item_str = ''
                while i < len(s) and s[i] in '-0123456789':
                    item_str += s[i]
                    i+=1
                return NestedInteger(int(item_str))
            elif s[i] == '[':
                lst = NestedInteger()
                i+=1
                if s[i] != ']':
                    lst.add(nested_integer())
                while s[i] == ',':
                    i+=1
                    lst.add(nested_integer())
                if s[i] == ']':
                    i+=1
                    return lst
        global i
        i = 0
        return nested_integer()
