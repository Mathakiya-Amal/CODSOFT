const boardEl = document.getElementById("board");
const messageEl = document.getElementById("message");
let board = [["", "", ""], ["", "", ""], ["", "", ""]];

function renderBoard() {
  boardEl.innerHTML = "";
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      const cell = document.createElement("div");
      cell.className = "cell";
      cell.textContent = board[i][j];
      if (board[i][j] === "") {
        cell.addEventListener("click", () => {
          board[i][j] = "X";
          renderBoard();
          checkGameState("X");
          fetch("/ai-move", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ board }),
          })
            .then((res) => res.json())
            .then((move) => {
              board[move.row][move.col] = "O";
              renderBoard();
              checkGameState("O");
            });
        });
      } else {
        cell.classList.add("disabled");
      }
      boardEl.appendChild(cell);
    }
  }
}

function checkGameState(player) {
  if (isWinner(player)) {
    messageEl.textContent = `${player} wins!`;
    disableBoard();
  } else if (isDraw()) {
    messageEl.textContent = "It's a draw!";
  }
}

function isWinner(p) {
  for (let i = 0; i < 3; i++) {
    if (board[i].every(c => c === p)) return true;
    if ([0, 1, 2].every(j => board[j][i] === p)) return true;
  }
  if ([0, 1, 2].every(i => board[i][i] === p)) return true;
  if ([0, 1, 2].every(i => board[i][2 - i] === p)) return true;
  return false;
}

function isDraw() {
  return board.flat().every(cell => cell !== "");
}

function disableBoard() {
  document.querySelectorAll(".cell").forEach(cell => cell.classList.add("disabled"));
}

renderBoard();