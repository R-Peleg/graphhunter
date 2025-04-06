from setuptools import setup, find_packages

setup(
    name="graphhunter",
    version="0.1.0",
    description="Python library for finding special graphs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Reuven Peleg",
    author_email="4018286+R-Peleg@users.noreply.github.com",  # Replace with your email
    url="https://github.com/yourusername/graphhunter",  # Replace with your repository URL
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "networkx>=2.5",  # Add other dependencies if needed
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)