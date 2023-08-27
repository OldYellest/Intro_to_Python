def lists():
    books = ["Moby Dick", "The Way of Men", "Extreme Ownership"]
    random = ["Moby Dick", 1, 5.4, "The Way of Men"]

    print(books)
    print(books.pop())
    print(books)
    books.append('Concrete Hell')
    print(books)

# pop() returns the last value from the list and gets rid of it
# XYZ.append() inserts a new item to the list
# The use of "tuples" is the same as lists, but pop() and append() cannot be used
