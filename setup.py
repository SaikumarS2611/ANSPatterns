import setuptools


with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

    
setuptools.setup(
    name="ANSPatterns",
    version="0.1.2",
    author="S SAIKUMAR",
    author_email="s.saikumar1103@gmail.com",
    license = "MIT",
    package = ["ANSPatterns"],
    description="A small package for patterns of Alphabets, Numbers and Symbols",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: Microsoft :: Windows :: Windows 10"
    ],
    keywords = 'patterns',
    package_dir={"": "ANSPatterns"},
    packages=setuptools.find_packages(where="ANSPatterns"),
    python_requires=">3.",
    zip_safe = False
)
