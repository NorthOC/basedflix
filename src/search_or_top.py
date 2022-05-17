def search_or_top():
    answers = ["1", "2"]
    query = ""

    print("1. Current top 100 movies")
    print("2. Search for a movie")

    x = input(f"Enter \'{answers[0]}\' to see top movies or \'{answers[1]}\' to search for a movie: ")
    
    while x not in answers:
        x = input("Wrong input. Try again:")

    if x == answers[1]:
        query = input("Enter the movie title: ")

    return query