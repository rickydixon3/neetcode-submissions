class Solution:

    def encode(self, strs: List[str]) -> str:
        # one way we could do it is to just combine it into one
        #master string and set where it neesd to be seperated
        #into different string arrays
        encoded_string = ""

        for s in strs:
            # get length of string to intiialize start 
            length = str(len(s))
            encoded_string += length
            encoded_string += "#" #seperator
            encoded_string += s # word itself

        return encoded_string
        

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        # pointer to traverse the input string
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+= 1
            length = int(s[i:j])
            decoded_strs.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        
        return decoded_strs

        




