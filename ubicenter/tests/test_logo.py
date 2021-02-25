import plotly.express as px

import ubicenter as ubic


def test_logo():
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    ubic.add_ubi_center_logo(fig, 1)


def 
