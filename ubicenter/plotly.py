from plotly import graph_objects as go
from typing import Union


CONFIG = {"displayModeBar": False}

LOGO_URL = (
    "https://raw.githubusercontent.com/UBICenter/ubicenter.org/master/"
    "assets/images/logos/wide-blue.jpg"
)

LIGHTER_BLUE = "#ABCEEB"  # Blue 100.
LIGHT_BLUE = "#49A6E2"  # Blue 500.
BLUE = "#1976D2"  # Blue 700.
DARK_BLUE = "#0F4AA1"  # Blue 900.
GRAY = "#BDBDBD"
WHITE = "#FFFFFF"

BLUE_COLOR_SEQUENCE = [LIGHTER_BLUE, LIGHT_BLUE, BLUE, DARK_BLUE]


def add_ubi_center_logo(
    fig: go.Figure, x: float = 0.98, y: float = -0.12
) -> None:
    """Adds UBI Center logo to a plotly figure. Returns nothing.

    :param fig: Plotly figure.
    :type fig: go.Figure
    :param x: Horizontal coordinate.
    :type x: float
    :param y: Vertical coordinate, defaults to -0.12.
    :type y: float, optional
    """
    fig.add_layout_image(
        dict(
            source=LOGO_URL,
            xref="paper",
            yref="paper",
            x=x,
            y=y,
            sizex=0.12,
            sizey=0.12,
            xanchor="right",
            yanchor="bottom",
        )
    )


def format_fig(
    fig: go.Figure,
    show: bool = True,
    width: int = 800,
    height: int = 600,
    **kwargs
) -> Union[None, go.Figure]:
    """Formats figure with UBI styling and logo.
    **kwargs passed to add_ubi_center_logo.

    :param fig: Plotly figure.
    :type fig: go.Figure
    :param show: Whether to show the figure, defaults to True.
        If False, returns the figure.
    :type show: bool
    :param width: Width of the figure, defaults to 800.
    :type width: int, optional
    :param height: Height of the figure, defaults to 600.
    :type height: int, optional
    :return: If show is True, nothing. If show is False, returns the
        formatted plotly figure.
    :rtype: go.Figure
    """
    add_ubi_center_logo(fig, **kwargs)
    fig.update_xaxes(
        title_font=dict(size=16, color="black"), tickfont={"size": 14}
    )
    fig.update_yaxes(
        title_font=dict(size=16, color="black"), tickfont={"size": 14}
    )
    fig.update_layout(
        hoverlabel_align="right",
        font_family="Roboto",
        title_font_size=20,
        plot_bgcolor="white",
        paper_bgcolor="white",
        width=width,
        height=height,
    )

    if show:
        fig.show(config=CONFIG)
    else:
        return fig
