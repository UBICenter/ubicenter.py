from plotly import graph_objects as go


CONFIG = {"displayModeBar": False}

def add_ubi_center_logo(
    fig: go.Figure, x: float = 0.98, y: float = -0.12
) -> None:
    """ Adds UBI Center logo to a plotly figure. Returns nothing.

    :param fig: Plotly figure.
    :type fig: go.Figure
    :param x: Horizontal coordinate.
    :type x: float
    :param y: Vertical coordinate, defaults to -0.12.
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


def format_fig(fig: go.Figure, show: bool=False, **kwargs) -> go.Figure:
    """ Formats figure with UBI styling and logo.
    **kwargs passed to add_ubi_center_logo.

    :param fig: Plotly figure.
    :type fig: go.Figure
    :param show: Whether to show the figure.
    :type show: bool
    :return: Formatted plotly figure. Also shows it.
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
        width=1000,
        height=800,
    )
    if show:
        fig.show(config=CONFIG)
    return fig
