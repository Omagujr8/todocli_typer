# TodoCLI Typer 📝

A simple, fast, and user-friendly Command Line Interface (CLI) To-Do application built with Python and [Typer](https://typer.tiangolo.com/). This tool allows you to manage your daily tasks directly from your terminal, storing them securely in a local SQLite database.

## 🌟 Features

* **Add Tasks:** Quickly add new to-do items from the command line.
* **List Tasks:** View all your current tasks with their status.
* **Complete Tasks:** Mark items as done.
* **Delete Tasks:** Remove tasks you no longer need.
* **Local Storage:** Uses a lightweight SQLite database (`todo.db`) to persist your tasks across sessions.

## 📁 Project Structure

* `todocli.py`: The main entry point containing the Typer CLI commands and logic.
* `model.py`: Contains the data models representing a To-Do item.
* `db.py`: Handles the database connection, setup, and query operations.
* `todo.db`: The local SQLite database file (generated automatically).
* `LICENSE`: MIT License information.

## 🚀 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Omagujr8/todocli_typer.git](https://github.com/Omagujr8/todocli_typer.git)
    cd todocli_typer
    ```

2.  **Set up a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    *Ensure you have `typer` installed. If you used other libraries like `rich` for terminal formatting, install them as well.*
    ```bash
    pip install typer 
    # pip install rich (Optional, if used for UI)
    ```

## 💻 Usage

Run the CLI using Python. Here are some of the standard commands you can use (update these if your specific function names differ):

**View all commands and help text:**
```bash
python todocli.py --help
