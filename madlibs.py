"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

# @app.route('/goodbye')
# def goodbye_form():  
#     return render_template("goodbye.html") 

@app.route('/game')
def show_madlib_form():
    """
    Make a function called show_madlib_form() and have the URL /game route 
    to it. In this function, get the user’s response to the yes-or-no question 
    on the “would you like to play a game?” form.
    """
    game_response = request.args.get('game')
    player = request.args.get('person')
    print(player)
    print("*************************")

    # print(game_response)
    if game_response == "yes":

        return render_template("game.html")
    elif game_response == "no":

        return render_template("goodbye.html", person=player)

@app.route('/madlib')
def show_matlib():
    player_name = request.args.get('name')
    player_color = request.args.get('color')
    player_noun = request.args.get('noun')
    player_adj = request.args.get('adjective')

    monster_scales = request.args.get('scales')
    monster_horns = request.args.get('horns')

    if monster_scales == None:
        monster_scales = "no scales"

    if monster_horns == None:
        monster_horns = "no horns"

    matlibhtml = choice(["madlib.html","madlib2.html"])


    return render_template(matlibhtml, person=player_name, color=player_color, noun=player_noun, adjective=player_adj, scales = monster_scales, horns=monster_horns)



if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
