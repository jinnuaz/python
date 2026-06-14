

class roman_to_integer:
    def romanToInt(self, s: str) -> int:

        # ---> Largest to smallest: Add them up
        # ---> Smaller before Larger: Subtract smaller

        roman_letters = {
                            'I': 1,
                            'V': 5,
                            'X': 10,
                            'L': 50,
                            'C': 100,
                            'D': 500,
                            'M': 1000
                        }
        res = 0

        for i in range(len(s)):
            if i+1 < len(s) and roman_letters[s[i]] < roman_letters[s[i + 1]]:
                res = res - roman_letters[s[i]]
            else:
                res = res + roman_letters[s[i]]

        return res

obj = roman_to_integer()
result = obj.romanToInt("IV")
print(result)
