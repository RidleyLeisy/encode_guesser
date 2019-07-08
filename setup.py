import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="encodeguess",
    version="0.0.1",
    author="Ridley Leisy",
    author_email="leisyridley@gmail.com",
    description="A small package that suggests which columns of your dataframe need to be encoded and in what way",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RidleyLeisy/encode_guesser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)