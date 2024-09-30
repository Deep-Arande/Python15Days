#  Create a class to represent a Movie with attributes like 
# title, director, and rating.



class Movie:
    title=str()
    director=str()
    rating=float()
    
    
    def __init__(self,title,director,rating):
        self.title=title
        self.director=director
        self.rating=rating
    
    def __str__(self) -> str:
        
       return f"Name={self.title}\nDirector={self.director}\nRatings={self.rating}"


movie1=Movie("The Shawshank Redemption","Frank Darabont",9.3)
movie2=Movie("The Godfather","Francis Ford Coppola",9.2)
movie3=Movie("Interstellar","Christopher Nolan",8.7)
print(f"{movie1}\n")
print(f"{movie2}\n")
print(f"{movie3}\n")

       