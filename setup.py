import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='PdfExTools',
    version='0.1.0',
    author='Mark Front',
    author_email='markfront@gmail.com',
    description='A Python package of extended tools to process pdf files',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/markfront/PdfTools',
    packages=setuptools.find_packages(),
    install_requires=['pdfplumber>=0.5'],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)