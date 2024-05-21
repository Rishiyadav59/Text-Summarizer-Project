import setuptools 

with open('README.MD', 'r',encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "rishiyadav59"
SRC_REPO = 'textsummarizer'
AUTHOR_EMAIL = "rishi2127930@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rishiyadav59/Text-Summarizer-Project",
    project_url={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)