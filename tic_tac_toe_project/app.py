from flask import Flask, render_template, request, jsonify
import copy

app = Flask(__name__)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)): return True
        if all(board[j][i] == player for j in range(3)): return True
    if all(board[i][i] == player for i in range(3)): return True
    if all(board[i][2 - i] == player for i in range(3)): return True
    return False

def is_full(board):
    return all(cell != "" for row in board for cell in row)

def minimax(board, is_max):
    if check_winner(board, "O"): return {"score": 1}
    if check_winner(board, "X"): return {"score": -1}
    if is_full(board): return {"score": 0}

    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O" if is_max else "X"
                result = minimax(board, not is_max)
                moves.append({"score": result["score"], "row": i, "col": j})
                board[i][j] = ""

    return max(moves, key=lambda x: x["score"]) if is_max else min(moves, key=lambda x: x["score"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ai-move", methods=["POST"])
def ai_move():
    data = request.get_json()
    board = data["board"]
    move = minimax(copy.deepcopy(board), True)
    return jsonify(move)

if __name__ == "__main__":
    app.run(debug=True)