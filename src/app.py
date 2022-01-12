from grimoire import Grimoire

from src.state import State
from src.templates import template


app = Grimoire(state=State)


@app.page(start=True)
@template
def start(state, second, third):
    return (
        ["Hello, Scott!"],
        [("Go to second page", second), ("Go to third page", third)],
        state
    )


@app.page()
@template
def second(state):
    return (
        ["I'm the second page.", f"{state.foo}"],
        [],
        state
    )

@app.page()
@template
def third(state):
    return (
        ["I'm the third page.", f"{state.bar}"],
        [],
        state
    )
