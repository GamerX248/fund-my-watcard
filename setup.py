from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = [_.strip() for _ in f.readlines() if _]

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="fund-my-watcard",
    version="0.1.3",
    packages=find_packages(),
    python_requires=">=3.4",
    scripts=["fund-my-watcard/watcard"],
    install_requires=requirements,
    author="xingweitian",
    author_email="xingweitian@gmail.com",
    description="A tool to fund your WatCard in an easy way",
    long_description=long_description,
    license="GPL-3.0",
    keywords="WatCard",
    url="https://github.com/xingweitian/fund-my-watcard",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
