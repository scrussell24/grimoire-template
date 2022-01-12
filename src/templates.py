from typing import List

from grimoire.templates import link
from grimoire.utils import make_decorator
from hype import *


@make_decorator
def template(fn, state: str, *opts: List[int]):
    paragraphs, options, state = fn(state, *opts)
    return (
        Doc(
            Html(
                Head(
                    Title("Grimoire Story"),
                    Meta(charset="utf-8"),
                    Meta( name="viewport", content="width=device-width, initial-scale=1"),
                    Link(rel="stylesheet", href="https://unpkg.com/@picocss/pico@latest/css/pico.min.css"),
                    Style("""
ul {
    padding-left: 0px !important;
}

li {
    list-style: none !important;
}""")
                ),
                Body(
                    Main(
                        *[Section(P(p)) for p in paragraphs],
                        Section(
                        Ul(*[Li(link(o[0], o[1])) for o in options]),
                        ),
                        _class="container",
                    ),
                ),
                lang="en",
                data_theme="dark"
            )
        ),
        state,
    )
