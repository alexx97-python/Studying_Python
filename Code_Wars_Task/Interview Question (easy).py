"""You receive the name of a city as a string, and you need to return a string that shows how many times each letter shows up in the string by using an asterisk (*).

For example:

"Chicago"  -->  "c:**,h:*,i:*,a:*,g:*,o:*"
As you can see, the letter c is shown only once, but wih 2 asterisks.

The return string should include only the letters (not the dashes, spaces, apostrophes, etc). There should be no spaces in the output, and the different letters are separated by a comma (,) as seen in the example above.

Note that the return string must list the letters in order of their first appearence in the original string."""


def get_strings(city):
    letters = {}
    result = []
    city = city.lower()
    for letter in city:
        if letter in letters.keys():
            letters[letter] += 1
        else:
            if letter != ' ':
                letters[letter] = 1
    for k, v in letters.items():
        values = '*' * v
        result.append(f'{k}:{values}')
    return ','.join(result)
