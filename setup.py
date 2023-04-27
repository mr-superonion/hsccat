from setuptools import setup, find_packages

__version__ = ""


scripts = []

setup(
    name="hsccat",
    version=__version__,
    description="simple code to play with HSC catalog",
    author="mr superonion",
    author_email="mr.superonion@hotmail.com",
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "astropy",
        "scipy",
        "matplotlib",
    ],
    packages=find_packages(),
    scripts=scripts,
    include_package_data=True,
    zip_safe=False,
)
