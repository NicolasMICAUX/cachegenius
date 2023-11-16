"""Setup.py for Pypi.org"""
from distutils.core import setup

setup(
    name="cachegenius",
    packages=["cachegenius"],
    version="0.1.0",
    description="Speed-up your code by automatically identifying functions that should use caching in your code!",
    author="Nicolas Micaux",
    url="https://github.com/NicolasMICAUX/cachegenius",
    install_requires=[],
    keywords=["cache", "caching", "automatically"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.5",
    # Set README.md as description
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
