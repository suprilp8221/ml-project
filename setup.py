from setuptools import setup, find_packages

def get_requirements(filepath):
    """Read requirements from file and return as list."""
    with open(filepath) as f:
        requirements = f.read().splitlines()
    return requirements

setup(
    name="ml-project",
    version="0.1.0",
    author="suprilp8221",
    author_email="suprilpatil1616@gmail.com",
    description="End-to-end ML project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/suprilp8221/ml-project",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
