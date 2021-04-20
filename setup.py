import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RtrcSplitCsv", # Replace with your own username
    version="0.0.1",
    author="Jeff Knight",
    author_email="jknight@arteric.com",
    description="RTRC package that splits a csv into DataFrame data and a configs dict",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Arteric-Jeff-Knight/rtrc_split_csv",
    project_urls={
        "Bug Tracker": "https://github.com/Arteric-Jeff-Knight/rtrc_split_csv/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
