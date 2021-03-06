import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygraphs",
    version="0.3.2",
    author="Gabriel B. Sant'Anna",
    author_email="baiocchi.gabriel@gmail.com",
    description="A package for the study of graph discrete data structures and algorithms",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://gitlab.com/baioc/pygraphs",
    keywords='graphs algorithms',
    packages=['pygraphs'],  # setuptools.find_packages()
    package_dir={'pygraphs': 'pygraphs/'},
    # py_modules=['pygraphs.libpygraphs'],
    package_data={'pygraphs': ['_libpygraphs.so']},
    classifiers=[
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Typing :: Typed',
        'Programming Language :: C++',
    ],
    python_requires='>=3.6',
)
