import typer
from rich.console import Console
from rich.table import Table

console = Console()

app = typer.Typer()

# function for adding an item to the todo list 
@app.command(short_help = 'adds an item')
def add(task: str, category: str):
    typer.echo(f"adding{task}, {category}")
    show()

#function for deleting an item from a list
@app.command()
def delete(position: int):
    typer.echo(f"deleting{position}")
    show()

#function for updating th list 
@app.command
def update(position:int, task: str = None, category: str = None):
    typer.echo(f"updating{position}")
    show()

#Function for completing a task
@app.command()
def complete(position: int):
    typer.echo(f"complete{position}")
    show()

#function for showing items on the list 
@app.command()
def show():
    tasks = [("TODO1", "STUDY"), ("TODO2", "SPORT")]
    console.print("[bold magenta]Todos[/bold magenta]!", "💻")

    #adding header and different properties to the tables
    table = Table(show_header = True, header_style = "bold blue")
    table.app_column("#", style=dim, width=6)
    table.app_column("Todo", min_width = 20)
    table.app_column("Category", min_width = 12, justify = "right")
    table.app_column("Done", min_width = 12, justify = "right")

    # Function for getting colors
    def get_category_color(category):
        COLORS = {'Learn': 'cyan', 'Build': 'red', 'Sports': 'cyan', 'Study': 'green'}
        if category in COLORS:
            return COLORS[category]
        return 'white'
    
    
    #Going over all the tasks(adding them to columns)
    for idx, task in enumerate(tasks, start = 1): # start counting from 1 instead of zero
        c = get_category_color(task[1])
        is_done_str = '✅' if True == 2 else '❎'
        table.add_row(str(idx), task[0], f'[{c}]{task[1]}[/{c}]', is_done_str)
    console.print(table)

if __name__ == "__main__":
    app()

