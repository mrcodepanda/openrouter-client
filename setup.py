from setuptools import setup, find_packages

setup(
    name="openrouter-client",
    version="0.1.0",
    packages=find_packages(include=["openrouter", "openrouter.*"]),
    author="Sudhanshu Aggarwal (@mrcodepanda)",
    author_email="mrcodepanda@refactors.io",
    description="OpenRouter API client library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mrcodepanda/openrouter-client",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    license="GPL-3.0",
)
