"""
    # Copyright 2023 DanGlChris (Daglox Kankwanda). All rights reserved.
"""
from setuptools import setup, find_packages

if __name__ == "__main__":
    try:
        setup(
            name='short-activist-pred',
            version='1.0.0',
            packages=find_packages(exclude=['tests*']),
            license='GPL-3.0',
            description='Short activists prediction',
            long_description=open('README.md').read(),
            install_requires=[
                'bertopic>=0.15.0',
                'pdfplumber>=0.10.2',
                'numpy>=1.20.0',
                'pandas>=1.1.5',
                'matplotlib>=3.1.7',
                'nltk>=3.8.1',
                'wordcloud>=1.9.2',
                'transformers>=4.34.0',
                "huggingface_hub>=3.0.4",
                "pwinput>=1.0.3",
            ],
            url='https://github.com/DanGlChris/short-activist-pred',
            author='Daglox Kankwanda',
            author_email='dagloxkankwenda@gmail.com'
        )
    except:  # noqa
        print(
            "\n\nAn error occurred while building the project, "
            "please ensure you have the most updated version of setuptools, "
            "setuptools_scm and wheel with:\n"
            "   pip install -U setuptools setuptools_scm wheel\n\n"
        )
        raise
