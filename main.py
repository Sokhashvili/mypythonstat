# ლისტს აკლია 4 იანი



# def missing_number(nums):
#     list_1 = list(range(1, nums[-1] + 1))
#     m_num = [i for i in list_1 if i not in nums]
#     new_list = nums[:]
#     new_list.append(m_num[0])
#     print(sorted(new_list))

# nums = [1, 2, 3, 5, 6, 7, 8, 9, 10]
# missing_number(nums)



# def first_repeating(nums):
#     def binary_search(arr, target):
#         left, right = 0, len(arr) - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if arr[mid] == target:
#                 return mid
#             elif arr[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return -1

#     nums.sort() 
#     first_repeating = None
#     for i in range(1, len(nums)):
#         index = binary_search(nums, nums[i])
#         if index != -1 and index < i:
#             first_repeating = nums[index]
#             break
#     index_9 = binary_search(nums, 9)
#     return first_repeating, index_9

# nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
# first_repeating, index_9 = first_repeating(nums)
# if first_repeating is not None:
#     print("First repeating number:", first_repeating)
#     print("Index of number 9 is:", index_9)
# else:
#     print("No repeating number found.")

    #ქართულად რომ ვწერ პრინტში მიჭედავს


# operator_function = {
#     '+': lambda a, b: a + b,
#     '-': lambda a, b: a - b,
#     '*': lambda a, b: a * b,
#     '/': lambda a, b: a / b if b != 0 else "Error: Division by zero"
# }

# def main():
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     operator = input("Enter operator (+, -, *, /): ")

#     if operator in operator_function:
#         result = operator_function[operator](num1, num2)
#         print("Result:", result)
#     else:
#         print("Invalid operator")

# if __name__ == "__main__":
#     main()




# def change_last_value(lst, new_value):
#     result = []
#     for tup in lst:
#         temp_list = list(tup)
#         temp_list[-1] = new_value
#         result.append(tuple(temp_list))
#     return result

# sample = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# new_value = 100
# updated_samples = change_last_value(sample, new_value)
# print("Original list of tuples:", sample)
# print("Updated list of tuples:", updated_samples)




# def find_smallest_largest(data):
#     smallest = None
#     largest = None
#     for tup in data:
#         for value in tup:
            
#             if smallest is None or value < smallest:
#                 smallest = value
#             if largest is None or value > largest:
#                 largest = value
    
#     return smallest, largest
# data = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# smallest, largest = find_smallest_largest(data)
# print("Smallest value:", smallest)
# print("Largest value:", largest)



# def sashualo(tuples):
#     means = []
#     for i in tuples:
#         total = sum(i)
#         mean = total / len(i)
#         means.append(mean)
#     return means

# input_tuples = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# output = sashualo(input_tuples)
# print("Output =", output)

#   ბიბლიოთეკა


# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, title, author, genre):
#         self.books.append({'title': title, 'author': author, 'genre': genre})

#     def search_by_title(self, title):
#         found_books = [book for book in self.books if book['title'].lower() == title.lower()]
#         return found_books

#     def search_by_author(self, author):
#         found_books = [book for book in self.books if book['author'].lower() == author.lower()]
#         return found_books

#     def search_by_genre(self, genre):
#         found_books = [book for book in self.books if book['genre'].lower() == genre.lower()]
#         return found_books


# def main():
#     library = Library()
#     library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
#     library.add_book("To Kill a Mockingbird", "1", "Fiction")
#     library.add_book("1984", "George Orwell", "Dystopian")
#     library.add_book("Pride and Prejudice", "Jane Austen", "Romance")
#     library.add_book("The Divine Comedy", "Dante Alighieri", "Epic poetry")

#     while True:
#         print("\n1. Search by Title")
#         print("2. Search by Author")
#         print("3. Search by Genre")
#         print("4. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             title = input("Enter the title to search: ")
#             found_books = library.search_by_title(title)
#             if found_books:
#                 print("Found Books:")
#                 for book in found_books:
#                     print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")
#             else:
#                 print("No books found with that title.")

#         elif choice == '2':
#             author = input("Enter the author to search: ")
#             found_books = library.search_by_author(author)
#             if found_books:
#                 print("Found Books:")
#                 for book in found_books:
#                     print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")
#             else:
#                 print("No books found by that author.")

#         elif choice == '3':
#             genre = input("Enter the genre to search: ")
#             found_books = library.search_by_genre(genre)
#             if found_books:
#                 print("Found Books:")
#                 for book in found_books:
#                     print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")
#             else:
#                 print("No books found with that genre.")

#         elif choice == '4':
#             print("Exiting...")
#             break

#         else:
#             print("Invalid choice. Please enter again.")


# main()
