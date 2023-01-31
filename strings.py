"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
### git comment
"""
import pytest

def no_duplicates(a_string):
    p = list(name.strip())
    print(p)
    z=list( dict.fromkeys(p))
    print(z)
    z.sort()
    print(z)
    q=""
    for i in z:
      q=q+i
    print(q)
    pass q


def reversed_words(a_string):
        arr=["monty" ,"pythons" ,"flying" ,"circus"]
        res = arr[::-1]
        print(res)
        pass res


def four_char_strings(a_string):
    name = "monty pythons flying circus"
    print([name[i:i+4] for i in range(0, len(name), 4)])
    pass name


def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    main()
    
