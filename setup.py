
from setuptools import setup, find_packages

setup(
    name="centralized_logger",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "python-json-logger",
    ],
    description="A centralized JSON logging library for Python applications.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/centralized-logger",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
