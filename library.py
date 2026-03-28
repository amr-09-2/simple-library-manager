# first list (books I own)
list_1 = []

book_own_1 = input("Enter the name of a book you own: ")
list_1.append(book_own_1)

book_own_2 = input("Enter another book (or press enter to skip): ")
if book_own_2:
    list_1.append(book_own_2)
    print(f"You have in your library: {list_1}")
else:
    print(f"You have in your library: {list_1}")


# wish list (books I want)
list_2 = []

wish_book_1 = input("Enter the name of a book you wish to have in the future: ")
list_2.append(wish_book_1)

wish_book_2 = input("Enter another book if you want (or press enter to skip): ")
if wish_book_2:
    list_2.append(wish_book_2)
    print(f"Your wish list: {list_2}")
else:
    print(f"Your wish list: {list_2}")


# move book from wish list to library
bought_book = input("Enter the name of a book from your wish list that you bought (or press enter to skip): ")

if bought_book in list_2:
    list_2.remove(bought_book)
    list_1.append(bought_book)
    print(f"The library now: {list_1}")
    print(f"The wish list now: {list_2}")
else:
    print(f"The library: {list_1}")
    print(f"The wish list: {list_2}")


# donation
donation_book = input("Enter a book you want to donate (or press enter to skip): ")

if donation_book in list_1:
    list_1.remove(donation_book)
    print(f"Final library: {list_1}")

elif donation_book:
    list_1.append(donation_book)
    print(f"Your final library after donation: {list_1}")

else:
    print(f"Your final library: {list_1}")
