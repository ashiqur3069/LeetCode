class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse_code_array = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

	result = set()
	for word in words:
		word = word.lower()
		transformations = ""
		for chr in word:
			transformations += morse_code_array[ord(chr) - 97]
		result.add(transformations)
	return len(result)
