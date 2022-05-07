from flask import Flask, request

# Initialize the Flask app
app = Flask(__name__)

# Define your first route - every route needs a few things:
# 1. The decorator - this is which route you are defining (route must start with /)
@app.route("/")
# 2. The function that runs when the route is called (each function must have its own unique name)
def get_index():
    # 3. What the route does - this route returns the string "Hello"
    return "Hello"

# This is one way of passing in variables to a Flask route
# Hit this route: http://127.0.0.1:8001/greeting/module/Beka
# What's in <> is the variable you are passing in
@app.route("/greeting/module/<name>")
# You need to define the parameter that is being passed to the function from the route
# This should be whats in the <>
def get_module_greeting(name):
    # Now you can use this/these parameter(s) as you want
    greeting_statement = f"Hello, {name}"
    return greeting_statement

# This is a better way of passing in variables
# Hit this route: http://127.0.0.1:8001/greeting/query_param?name=Beka
# Define your route and the method
@app.route("/greeting/query_param", methods=["GET"])
def get_query_param_greeting():
    # This allows you to check if the route request included the route parameter "name"
    name = request.args.get("name")
    # Now you can use this variable in the same way
    greeting_statement = f"Hello, {name}"
    return greeting_statement


# Why is the second method better? Look at the route below
# If you used the other method, this request would look like this: /game/2021-08-03/578/493
# The route below is MUCH easier to read
# Hit this route: /game?date=2021-08-05&teamId=578&playerId=493
@app.route("/game", methods=["GET"])
def get_game():
    # Get any query parameters used
    # If you don't pass in one of the parameters, request.args.get will return None
    date = request.args.get("date")
    team_id = request.args.get("teamId")
    player_id = request.args.get("playerId")
    # If none of of the query parameters are defined, return a 400 Bad Request message
    if team_id is None and date is None and player_id is None:
        return "Must pass in at least one query parameter", 400
    # Otherwise, create a dictionary
    info = {}
    # For any parameters passed in, add it to the dictionary
    if team_id:
        info["team_id"] = team_id
    if player_id:
        info["player_id"] = player_id 
    if date:
        info["date"] = date
    # Return the dictionary
    return info


# If this python file is called, execute this code
if __name__ == "__main__":
    # Run the app on port 8001
    # debug=True means that the app will reload if you make and save changes to the file
    # and if there are errors it will show you an error message
    app.run(port=8001, debug=True)