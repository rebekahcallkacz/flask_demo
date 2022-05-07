from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def get_index():
    return "Hello"

# Hit this route: http://127.0.0.1:8001/greeting/module/Beka
@app.route("/greeting/module/<name>")
def get_module_greeting(name):
    greeting_statement = f"Hello, {name}"
    return greeting_statement


# Hit this route: http://127.0.0.1:8001/greeting/query_param?name=Beka
@app.route("/greeting/query_param", methods=["GET"])
def get_query_param_greeting():
    name = request.args.get("name")
    greeting_statement = f"Hello, {name}"
    return greeting_statement


# Hit this route: /game?date=2021-08-05&teamId=578&playerId=493
@app.route("/game", methods=["GET"])
def get_game():
    date = request.args.get("date")
    team_id = request.args.get("teamId")
    player_id = request.args.get("playerId")
    if team_id is None and date is None and player_id is None:
        return "Must pass in at least one query parameter", 400
    info = {}
    if team_id:
        info["team_id"] = team_id
    if player_id:
        info["player_id"] = player_id 
    if date:
        info["date"] = date
    return info


if __name__ == "__main__":
    app.run(port=8001, debug=True)