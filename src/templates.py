from grimoire.templates import default_page
from grimoire.utils import make_decorator
from hype import Div, P


@make_decorator
@default_page("Grimoire Story")
def template(fn, state, *opts):
    paragraphs, options, state = fn(state, *opts)
    content = Div(
        *[P(p) for p in paragraphs],
    )
    return content, options, state