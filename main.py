from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too



    

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    movie = get_random_movie()

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    day2 = "<h1>Tomorrow's Movie</h1>"
    day2 +="<ul>"
    day2 += "<li>" + movie + "</li>"
    day2 += "</ul>"

    return content + day2

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    # TODO: randomly choose one of the movies, and return it
    movie = ["Star Wars Episode V:Empire Strikes Back", "Star Wars Episode IV: A New Hope","Star Wars Episode VI: Return of the Jedi"]
    movie.append("A Star Wars Story: Rogue One")
    movie.append("A Star Wars Story: Han solo")
    movie.append("Star Wars Episode I: Phantom Menace")
    movie.append("Star Wars Episode II: Clone Wars")
    movie.append("Star Wars Episode III: Revenge of the Sith")
    # more = input("Add a new movie to the list:")
    # movie.append(more)
    number = random.randrange(0, len(movie))
    return movie[number]

app.run()
