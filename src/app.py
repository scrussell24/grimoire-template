from grimoire import Grimoire

from src.state import State
from src.templates import template


app = Grimoire(state=State)


@app.page(start=True)
@template
def start(state, second):
    return (
        ["Hello, Scott!"],
        [("Go to second page", second)],
        state
    )


@app.page()
@template
def second(state):
    return (
        ["I'm the second page."],
        [],
        state
    )
