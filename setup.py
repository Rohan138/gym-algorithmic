from setuptools import setup

VERSION = "0.0.1"

long_description = ""
with open("README.md") as fh:
    header_count = 0
    for line in fh:
        if line.startswith("##"):
            header_count += 1
        if header_count < 2:
            long_description += line
        else:
            break

setup(
    name="gym-algorithmic",
    version=VERSION,
    description="Algorithmic Environments from OpenAI Gym",
    long_description=long_description,
    url="https://github.com/Rohan138/gym-algorithmic",
    author="Rohan Potdar",
    author_email="rohanpotdar138@gmail.com",
    license="",
    packages=["algorithmic"],
    install_requires=[
        "gym>=0.19.0",
    ],
    python_requires=">=3.6, <3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)