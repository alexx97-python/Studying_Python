"""
Suppose we know the process by which a string s was encoded to a string r (see explanation below). The aim of the kata is to decode this string r to get back the original string s.

Explanation of the encoding process:
input: a string s composed of lowercase letters from "a" to "z", and a positive integer num
we know there is a correspondence between abcde...uvwxyzand 0, 1, 2 ..., 23, 24, 25 : 0 <-> a, 1 <-> b ...
if c is a character of s whose corresponding number is x, apply to x the function f: x-> f(x) = num * x % 26, then find ch the corresponding character of f(x)
Accumulate all these ch in a string r
concatenate num and r and return the result
For example:

encode("mer", 6015)  -->  "6015ekx"

m --> 12,   12 * 6015 % 26 = 4,    4  --> e
e --> 4,     4 * 6015 % 26 = 10,   10 --> k
r --> 17,   17 * 6015 % 26 = 23,   23 --> x

So we get "ekx", hence the output is "6015ekx"
Task
A string s was encoded to string r by the above process. complete the function to get back s whenever it is possible.

Indeed it can happen that the decoding is impossible when positive integer num has not been correctly chosen. In that case return "Impossible to decode".

Examples
"6015ekx"  -->  "mer"
"5057aan"  -->  "Impossible to decode"
"""


def decode(r):
    numbers = [str(num) for num in range(10)]
    if r[0] not in numbers:
        return 'Impossible to decode'
    divisor = int(''.join([e for e in r if e in numbers]))
    string = [e for e in r if e not in numbers]
    result = []

    if divisor % 2 == 0:
        return 'Impossible to decode'

    for letter in string:
        reminder = ord(letter) - 97
        character = [chr(number + 97) for number in range(26) if (number * divisor) % 26 == reminder]
        result.append(character[0])
    return ''.join(result)


print(decode("6015ekx"))
decode('761328qockcouoqmoayqwmkkic')
decode('1273409kuqhkoynvvknsdwljantzkpnmfgf')
decode('1122305vvkhrrcsyfkvejxjfvafzwpsdqgp')
decode('1544749cdcizljymhdmvvypyjamowl')

print(decode('aaaababbaaabaabbbaababbbbabababbbbabaaabbababbbaabbabbbaabbaabaaaabaaaaabbabbaabaabbbbaaaaaabbbbaaaaaabbaababbaaaabbaabbaaabbbabbabbbbabaa'))

