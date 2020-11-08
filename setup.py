import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdfextools-20_mark.gu-front_20",
    version="0.2.0",
    author="Mark Front",
    author_email="mark.front@gmail.com",
    description="A set of extended tools to process pdf files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/markfront/PdfExTools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
