from grimoire.templates import link
from grimoire.utils import make_decorator
from hype import Div, P, Ul, Li


@make_decorator
def template(fn, state, *opts):
    paragraphs, options, state = fn(state, *opts)
    content = Div(
        *[P(p) for p in paragraphs],
        Ul(*[Li(link(o[0], o[1])) for o in options])
    )
    return content, state
