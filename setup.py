import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="histy-mason", # Replace with your own username
    version="0.0.1",
    author="Mason Hall",
    author_email="masonhall@gmail.com",
    description="A command-line tool for generating histograms from timestamped logs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fmhall/histy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)