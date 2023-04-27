from setuptools import setup, find_packages

__version__ = ""


# scripts = [
#     "bin/impt_config",
#     "bin/impt_process_fpfs_sim.py",
# ]
scripts = []

setup(
    name="impt",
    version=__version__,
    description="simple code to play with HSC catalog",
    author="mr superonion",
    author_email="mr.superonion@hotmail.com",
    python_requires=">=3.8",
    install_requires=[
        "numpy",
    ],
    packages=find_packages(),
    scripts=scripts,
    include_package_data=True,
    zip_safe=False,
)
