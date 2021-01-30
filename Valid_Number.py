class Solution:
    def isNumber(self, s: str) -> bool:
            if self._validate(s):
                return True
            return False
    
    def _validate(self,s):
        try:
            int(s)
            return True
        except:
            pass

        try:
            float(s)
            return True
        except:
            pass        
