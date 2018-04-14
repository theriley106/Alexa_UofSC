wordList = open('subjects.txt').read().split("\n")
valAdd = ""

for word in wordList:
	valAdd += """{
                            "name": {
                                "value": "word1"
                            }
                        },""".replace('word1', word.lower())

print valAdd
