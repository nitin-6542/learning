import pickle

class Book:
    
    def __init__(self,title, author, genre,ISBN):
        self.title=title
        self.author=author
        self.genre=genre
        self.ISBN=ISBN
        
    def __repr__(self):
        return str({"Title":self.title,"Author":self.author,"Genre":self.genre,"ISBN":self.ISBN})
    
class library(Book):
    def __init__(self):
        self.database=self.load_database()

    def add_books(self,title,author,genre,ISBN):
        x=[i for i in self.database if title==i.title]
        if len(x)==0:
        
            self.database.append(Book(title,author,genre,ISBN))
        else:
            print("book already present")

    def search_books(self,hint):
        temp=[{"title":i.title,"Author":i.author,"Genre":i.genre,"ISBN":i.ISBN} for i in self.database if hint in [i.title,i.author,i.genre,i.ISBN ]]
        if len(temp)!=0:
            return temp
        else:
            return "Book not Found"
    
    def delete_book(self,ISBN):
        temp=[(i,self.database.remove(i)) for i in self.database if ISBN ==i.ISBN ]
        if len(temp)!=0:
            
            print("deleted successfully")

        else:
            print("Book not Found")
               
               
    def save_database(self):
        with open('database.pkl', 'wb') as f:
            pickle.dump(self.database, f)

    def load_database(self):
        with open('database.pkl', 'rb') as f:
            return pickle.load(f)
    def list_by_genre(self,genre):
        return [{"Genre":[].append(i.title)} for i in self.database if i.genre==genre]
    def get_authors(self):
        return list(set([i.author for i in self.database ]))
    
    def show_history(self,history):
        for i in history:
            print(i,"\n")
    

class authentication:
    pass
    











    




