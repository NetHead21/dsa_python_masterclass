# list iteration
my_list: list[int] = [1, 2, 3, 4, 5, 6]
for num in my_list:
    print(num)


# List iteration and summing numbers
numbers: list[int] = [1, 2, 3, 4, 5, 6]
sum_of_numbers = 0

for num in numbers:
    sum_of_numbers += num

print(f"Sum of numbers is: {sum_of_numbers}")
# or everything can be written as:
print(f"Sum of numbers is: {sum(numbers)}")
# the result is the same but without using
# loops and it is more faster

# Printing triangle
for i in range(5):
    for j in range(i + 1):
        print("* ", end="")
    print()


word = "Hello, World!"
vowel_count = 0
for char in word.lower():
    if char in "aeiou":
        vowel_count += 1

# or can be rewritten as
# it is more efficient and faster
vowel_count_v2 = sum(1 for char in word.lower() if char in "aeiuo")

print(f"Number of vowels: {vowel_count}")
print(f"Number of vowels: {vowel_count_v2}")


numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

# or can be rewritten as
even_numbers_v2 = [num for num in numbers if num % 2 == 0]

print(f"Even numbers: {even_numbers}")
print(f"Even numbers: {even_numbers_v2}")
