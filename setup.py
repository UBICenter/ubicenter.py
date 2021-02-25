from setuptools import setup

setup(
    name="ubicenter",
    version="0.1.0",
    description="Internal tools for the UBI Center.",
    url="http://github.com/UBICenter/ubicenter.py",
    author="Max Ghenis",
    author_email="max@ubicenter.org",
    license="MIT",
    packages=["ubicenter"],
    install_requires=["plotly",],
    zip_safe=False,
)
