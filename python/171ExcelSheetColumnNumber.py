class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        pos = len(columnTitle) - 1

        for letter in columnTitle:
            result += self.letter_to_number(letter)*(26**pos)
            pos -= 1

        return result

    def letter_to_number(self, letter):
        return ord(letter.upper()) - ord('A') + 1