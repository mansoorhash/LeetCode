class Solution:
    def isValid(self, s: str) -> bool:

        queue = list()
        valid = True
        for i,op in enumerate(s):
            if op in ("(","{","["):
                match op:
                    case "(":
                        queue.append(")")    
                    case "{":
                        queue.append("}")  
                    case "[":
                        queue.append("]")
            elif op in (")", "}", "]"):
                if len(queue) == 0: return False
                elif op != queue[len(queue)-1]:
                    return False
                else:
                    queue.pop()
        if len(queue) > 0: return False
        return True
            

        