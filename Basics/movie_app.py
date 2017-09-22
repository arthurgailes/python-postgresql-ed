# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 11:56:35 2017

@author: agail
"""

#from movie import Movie
#from user import User
#import json
#
#
#
#with open ('my_file.txt', 'r') as f:
#    json_data = json.load(f)
#    user = User.from_json(json_data)
#    print(user.json())

import os
import json
from user import User

def menu():
    name = input("What is your name? ")
    filename = "{}.txt".format(name)
    options = """Enter 'a' to add a movie, 's' to see the list of movies, 'w' to set a movie
               as watched, 'd' to delete a movie, 'l' to see the list of watched 
               movies, 'f' to save, and 'q' to save and quit. """
    if file_exists(filename): 
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(name)    
    user_input = input(options)
    while user_input != 'q':
        if user_input == 'a':
            movie_name = input("Enter the movie name: ")
            movie_genre = input("Enter the movie genre: ")
            user.add_movie(movie_name, movie_genre)
        elif user_input == 's':
            for movie in user.movies:
                print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre,
                      movie.watched))
        elif user_input == 'w':
            movie_name = input("Enter the movie name to set as watched: ")
            user.set_watched(movie_name)
        elif user_input == 'd':
            movie_name = input("Enter the movie name: ")
            user.delete_movie(movie.name)
        elif user_input == 'l':
            for movie in user.watched_movies():
                print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre,
                      movie.watched))
        elif user_input == 'f':
            with open(filename, 'w') as f:
                json.dump(user.json(), f)
            
        user_input = input(options)
        
def file_exists(filename):
    return os.path.isfile(filename)

menu()