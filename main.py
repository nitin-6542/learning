from book import Book ,library
import pickle
operations='''add -> to add the book details
remove -> to remove the
search -> to search the Book
all -> to get all saved books details
save-> to save the all details of Book
show_history -> to show the history of current operation 
authors -> to get all authors of all books
genre -> to get all genre 
exit -> to exit from program '''

def start():
    print(" * "*10+"\n")
    print("Book managment system \n")
    print("Suppported Operations \n")
    print(operations)
    print(" * "*10+"\n")
    while True:

        choice=input("Please Enter your choice : ")

        if choice =="add":
            
            title=input("Please enter Title\n")
            author=input("Please enter author name\n")
            genre=input("Please enter Genre\n")
            ISBN=input("Please enter ISBN\n")
            
            library.add_books(title,author,genre,ISBN)
        if choice=="remove":
            ISBN=input("Please enter ISBN \n ")
            library.delete_book(ISBN)

        if choice=="search":
            hint=input("Please enter the Title or Author or genre or ISBN")
            print(library.search_books(hint))
        
        if choice == "exit":
            break
        if choice=="all":
            print(library.load_database())
            
        if choice == "save":
            print(library.database)
            library.save_database()
        if choice == "genre":
            genre=input("Enter the genre value to get all books \n ")
            print(library.list_by_genre(genre))
        if choice == "authors":
            print(library.get_authors())
        
        current_session_history.append(choice)
        if choice == "show_history":
            library.show_history(tuple(current_session_history))
        if choice not in ["all","save","genre","add","search","remove","authors","show_history"]:
            print("please enter valid choice")
        
        

if __name__=="__main__":
    library=library()
    current_session_history=[]

    start()