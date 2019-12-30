movies=[]

def menu():
    user_input=input("Enter 'a' to add a movie,'l' to see ur movies,'f' to find a movie, and 'q' to quit: ")
    while user_input!='q':

        if user_input=='a':
            add_movie()
        elif user_input=='l':
            show_movie()
        elif user_input=='f':
            find_by=input("what property of movie u are looking for ?")
            looking_for=input("what are u searching for?")
            movie = find_movie(looking_for, lambda x: x[find_by])
            print(movie or 'No movies found.')
        elif user_input=='q':
            print("stop program...")

        user_input=input("Enter 'a' to add a movie,'l' to see ur movies,'f' to find a movie, and 'q' to quit: ")


def add_movie():
    name=input("enter movie name:")
    director=input("enter director name:")
    year=input("enter the movie release year:")

    movies.append({
        'name':name,
        'director':director,
        'year':year
        })

def show_movie():
    for movie in movies:
        print(f"Name: {movie['name']}")
        print(f"Director: {movie['director']}")
        print(f"Release year: {movie['year']}")

def find_movie(expected,finder):
    
    found=[]
    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)
    return found

    
menu()

    

            
        
