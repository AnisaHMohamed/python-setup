digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
name = "first last"
print(digits)
# indexing
print(digits[4])
# negative indexing
print(digits[-4])
# negative indexing first index
print(digits[-len(digits)])
# range in an array which initially inclusive and ends exclusively
print(digits[:3])
# slice individual parts of an array
print(name[0:5])
# strides to skips indexes
print(digits[0:10:2])
# strides includes all indexes
print(digits[::])
# strides includes all indexes with a skip of 3
print(digits[::3])
# strides includes all indexes with a skip of 3 in reverse order
print(digits[::-3])
# strides to skips indexes in reverse with a range
print(digits[10:0:-2])
# range always starts at zero
for i in range(len(digits)):
    print(digits[0:i])
# all numbers in array arranged in groups of 3
window_size = 3
for i in range(len(digits)):
    if len(digits[i:i+window_size]) == window_size:
        print(digits[i:i+window_size])
# alternativefor i in range(len(digits)):
window_size = 3
for i in range(len(digits)-(window_size-1)):
    print(digits[i:i+window_size])
