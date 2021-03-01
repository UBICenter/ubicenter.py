import plotly.express as px

import ubicenter as ubic


df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")


def test_add_ubi_center_logo():
    ubic.add_ubi_center_logo(fig, 1)


def test_format_fig():
    ubic.format_fig(fig)
