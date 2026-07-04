"""
Modern Tic-Tac-Toe Desktop Application
Implements an industry-standard MVC architecture with strict type hinting,
clean separation of concerns, and a highly polished contemporary flat UI.
"""

import tkinter as tk
from tkinter import font as tkfont
from typing import List, Optional, Tuple


class TicTacToeEngine:
    """Handles the pure game logic and state independent of the UI."""

    def __init__(self) -> None:
        self.board: List[Optional[str]] = [None] * 9
        self.current_player: str = "X"
        self.winner: Optional[str] = None
        self.winning_combination: Optional[Tuple[int, int, int]] = None
        self.is_tie: bool = False

    def make_move(self, position: int) -> bool:
        """Attempts to place the current player's token at the given position.
        
        Returns True if the move was valid and executed, False otherwise.
        """
        if self.board[position] is not None or self.winner or self.is_tie:
            return False

        self.board[position] = self.current_player
        
        if self._check_win():
            self.winner = self.current_player
        elif None not in self.board:
            self.is_tie = True
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
            
        return True

    def _check_win(self) -> bool:
        """Evaluates rows, columns, and diagonals for a win condition."""
        win_states: List[Tuple[int, int, int]] = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for combo in win_states:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] 
                    and self.board[combo[0]] is not None):
                self.winning_combination = combo
                return True
        return False

    def reset(self) -> None:
        """Resets the internal engine state back to a new game."""
        self.__init__()


class TicTacToeGUI(tk.Tk):
    """Manages the modern graphical user interface and user interactions."""

    # Modern Design Token Palette
    COLOR_BG = "#1E1E2E"         # Deep Slate / Dark mode background
    COLOR_CARD = "#252538"       # Slightly lighter slate for structural elements
    COLOR_TEXT = "#CDD6F4"       # Off-white for readability
    COLOR_MUTED = "#A6ADC8"      # Light grey for subtitles
    COLOR_X = "#F38BA8"          # Vibrant pastel rosewater for X
    COLOR_O = "#89B4FA"          # Vibrant pastel lavender-blue for O
    COLOR_WIN = "#A6E3A1"        # Emerald green accent for highlights
    
    def __init__(self, engine: TicTacToeEngine) -> None:
        super().__init__()
        self.engine = engine
        
        # Window Configuration
        self.title("Tic-Tac-Toe")
        self.geometry("420x550")
        self.configure(bg=self.COLOR_BG)
        self.resizable(False, False)
        
        # Setup Typography
        self.title_font = tkfont.Font(family="Helvetica", size=22, weight="bold")
        self.status_font = tkfont.Font(family="Helvetica", size=12, weight="normal")
        self.grid_font = tkfont.Font(family="Helvetica", size=32, weight="bold")
        self.button_font = tkfont.Font(family="Helvetica", size=11, weight="bold")
        
        self.buttons: List[tk.Button] = []
        self._build_ui()

    def _build_ui(self) -> None:
        """Constructs the modern, flat layout structure."""
        # Header / Status Widget Panel
        self.header_frame = tk.Frame(self, bg=self.COLOR_BG, pady=20)
        self.header_frame.pack(fill=tk.X)
        
        self.title_label = tk.Label(
            self.header_frame, 
            text="TIC-TAC-TOE", 
            font=self.title_font, 
            fg=self.COLOR_TEXT, 
            bg=self.COLOR_BG
        )
        self.title_label.pack()
        
        self.status_label = tk.Label(
            self.header_frame, 
            text=f"Player {self.engine.current_player}'s Turn", 
            font=self.status_font, 
            fg=self.COLOR_MUTED, 
            bg=self.COLOR_BG,
            pady=5
        )
        self.status_label.pack()

        # Grid Wrapper Context
        self.grid_frame = tk.Frame(self, bg=self.COLOR_BG, padx=25, pady=10)
        self.grid_frame.pack(expand=True, fill=tk.BOTH)
        
        # Generate the 3x3 Interaction Board
        for i in range(9):
            btn = tk.Button(
                self.grid_frame,
                text="",
                font=self.grid_font,
                bg=self.COLOR_CARD,
                fg=self.COLOR_TEXT,
                activebackground=self.COLOR_BG,
                activeforeground=self.COLOR_TEXT,
                bd=0,
                relief=tk.FLAT,
                highlightthickness=0,
                command=lambda pos=i: self._handle_click(pos)
            )
            row, col = divmod(i, 3)
            # Standard grid padding creates clean, borderless channels organically
            btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)
            self.buttons.append(btn)
            
        # Configure Grid Weights for Responsiveness within boundary limits
        for i in range(3):
            self.grid_frame.grid_rowconfigure(i, weight=1)
            self.grid_frame.grid_columnconfigure(i, weight=1)

        # Control Panel Footer
        self.footer_frame = tk.Frame(self, bg=self.COLOR_BG, pady=25)
        self.footer_frame.pack(fill=tk.X)
        
        self.reset_button = tk.Button(
            self.footer_frame,
            text="RESET GAME",
            font=self.button_font,
            bg=self.COLOR_CARD,
            fg=self.COLOR_TEXT,
            activebackground=self.COLOR_BG,
            activeforeground=self.COLOR_TEXT,
            bd=0,
            relief=tk.FLAT,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self._reset_game
        )
        self.reset_button.pack()

    def _handle_click(self, position: int) -> None:
        """Processes user grid interaction through UI triggers."""
        active_player = self.engine.current_player
        
        # Commit action to engine layer
        if self.engine.make_move(position):
            # Resolve changes cleanly on Visual Layer
            target_btn = self.buttons[position]
            color = self.COLOR_X if active_player == "X" else self.COLOR_O
            target_btn.config(text=active_player, fg=color, state=tk.DISABLED, disabledforeground=color)
            
            self._update_game_status()

    def _update_game_status(self) -> None:
        """Evaluates state transitions to update labels and view configurations."""
        if self.engine.winner:
            self.status_label.config(
                text=f"Player {self.engine.winner} Wins!", 
                fg=self.COLOR_WIN
            )
            # Highlight winning cells and lock board
            if self.engine.winning_combination:
                for idx in self.engine.winning_combination:
                    self.buttons[idx].config(bg=self.COLOR_WIN, disabledforeground=self.COLOR_BG)
            self._disable_all_buttons()
            
        elif self.engine.is_tie:
            self.status_label.config(text="It's a Tie Game!", fg=self.COLOR_TEXT)
            self._disable_all_buttons()
            
        else:
            self.status_label.config(
                text=f"Player {self.engine.current_player}'s Turn", 
                fg=self.COLOR_MUTED
            )

    def _disable_all_buttons(self) -> None:
        """Prevents further user interaction once game achieves final state."""
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

    def _reset_game(self) -> None:
        """Flushes structural values inside engine and updates the view panel."""
        self.engine.reset()
        self.status_label.config(
            text=f"Player {self.engine.current_player}'s Turn", 
            fg=self.COLOR_MUTED
        )
        
        for btn in self.buttons:
            btn.config(
                text="", 
                state=tk.NORMAL, 
                bg=self.COLOR_CARD,
                fg=self.COLOR_TEXT
            )


if __name__ == "__main__":
    # Bootstrap execution safely following standard design patterns
    game_engine = TicTacToeEngine()
    app = TicTacToeGUI(game_engine)
    app.mainloop()
