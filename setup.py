import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

GITHUB_URL = "https://github.com/feslima/pyinterboleto"

setuptools.setup(
    name="pyinterboleto",
    version="0.0.1",
    author="Felipe Souza Lima",
    author_email="feslima93@gmail.com",
    description=("Biblioteca para facilitar o manuseio de boletos de contas "
                 "PJ no Banco Inter."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=GITHUB_URL,
    project_urls={
        "Bug Tracker": f"{GITHUB_URL}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)