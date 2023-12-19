from __future__ import annotations as _annotations

from fastui import AnyComponent
from fastui import components as c
from fastui.events import GoToEvent

page_title = 'OpenAI Keeper'


def layout(*components: AnyComponent, title: str | None = None) -> list[AnyComponent]:
    return [
        c.PageTitle(text=f'{page_title} — {title}' if title else page_title),
        c.Navbar(
            title=page_title,
            title_event=GoToEvent(url='/'),
            links=[
                c.Link(
                    components=[c.Text(text='GitHub')],
                    on_click=GoToEvent(url='https://github.com/chyroc/openai_keeper'),
                ),
            ],
        ),
        c.Page(
            components=[
                *((c.Heading(text=title),) if title else ()),
                *components,
            ],
        ),
    ]
