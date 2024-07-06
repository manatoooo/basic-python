text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
def countwords(text):
    words=text.split()
    return ''.join(map(lambda word: str(len(word)),words))
import re
removesign=text.lower()
removesign=re.sub(r'[^\w\s]','',removesign)
result =countwords(removesign)
print(result)
