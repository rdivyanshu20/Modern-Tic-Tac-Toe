# Modern Tic-Tac-Toe (Python Desktop App)

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen.svg)

A highly polished, industry-standard Tic-Tac-Toe desktop application built entirely in Python. 

Unlike legacy academic implementations, this project leverages a strict **Model-View-Controller (MVC)** architecture, comprehensive **type hinting**, and a contemporary flat-design UI—all while requiring **zero external dependencies**.

<div align="center">
  </div>

## Features

* **Modern Flat UI:** Utilizes a carefully curated dark-mode color palette with pastel accents, ditching the outdated 90s grid lines for clean, component-based spacing.
* **Zero Dependencies:** Built entirely on Python's standard library (`tkinter`). No `pip install` required.
* **Clean Architecture:** Strict decoupling between the pure mathematical game state (`TicTacToeEngine`) and the visual rendering layer (`TicTacToeGUI`).
* **Production-Ready Code:** Fully type-hinted (`typing` module) and documented, adhering to PEP 8 standards.
* **Defensive Design:** Prevents illegal moves, multi-clicks, and state corruption during gameplay.

##  Getting Started

### Prerequisites
You only need Python installed on your system (Version 3.8 or higher is recommended to support modern type hints).

### Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/modern-tic-tac-toe.git](https://github.com/yourusername/modern-tic-tac-toe.git)
   cd modern-tic-tac-toe
