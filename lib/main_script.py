from stack_functions import is_balanced
from sequence_functions import remove_duplicates
from dictionary_functions import word_frequency


expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))
print(is_balanced(expression2))  


input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  


sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
