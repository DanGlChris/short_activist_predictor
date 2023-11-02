"""
    # Copyright 2023 DanGlChris (Daglox Kankwanda). All rights reserved.
"""
from setuptools import setup, find_packages
import os
def clean():
    """Remove build directory and its contents."""
    os.system('rm -rf build')

if __name__ == "__main__":
    try:
        setup(
            name='short_activist_predictor',
            version='1.0.0c0',
            package_dir={"": "src"},
            packages=find_packages(where="short_activist_predictor"),
            license='GPL-v3.0',
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
                "huggingface_hub>=0.16.4",
            ],
            url='https://github.com/DanGlChris/short_activist_predictor',
            author='Daglox Kankwanda',
            author_email='dagloxkankwenda@gmail.com',
            classifiers=[
                'Development Status :: 3 - Alpha',
                'Intended Audience :: Developers',
                'Topic :: Software Development :: Libraries :: Python Modules',
                'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                'Programming Language :: Python :: 3.10',
                'Operating System :: Microsoft :: Windows',
                'Operating System :: POSIX :: Linux',
            ],
            cmdclass= {'clean': clean},
            zip_safe=False,
            egg_base='./src',

        )
    except:  # noqa
        print(
            "\n\nAn error occurred while building the project, "
            "please ensure you have the most updated version of setuptools, "
            "setuptools_scm and wheel with:\n"
            "   pip install -U setuptools setuptools_scm wheel\n\n"
        )
        raise
