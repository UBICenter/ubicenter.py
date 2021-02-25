from plotly import graph_objects as go


def add_ubi_center_logo(fig: go.Figure, x: float, y: float = -0.12) -> None:
    """ Adds UBI Center logo to a plotly figure. Returns nothing.

    :param fig: Plotly figure.
    :type fig: go.Figure
    :param x: Horizontal coordinate.
    :type x: float
    :param y: Horizontal coordinate, defaults to -0.12.
    :type y: float, optional
    """
    fig.add_layout_image(
        dict(
            source="https://raw.githubusercontent.com/UBICenter/blog/master/jb/_static/ubi_center_logo_wide_blue.png",
            # See https://github.com/plotly/plotly.py/issues/2975.
            # source="../_static/ubi_center_logo_wide_blue.png",
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
