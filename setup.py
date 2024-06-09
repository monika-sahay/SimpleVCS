from setuptools import setup, find_packages


def parse_requirements(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line and not line.startswith('#')]


instal_requires = parse_requirements('requirements.txt')


setup(
    name='simplevcs',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'SimpleVCS=simplevcs.simplevcs:main',
        ],
    },
    install_requires=instal_requires,
    author='Monika Monika',
    author_email='monika_sahay@yahoo.com',
    description='A minimalistic version control system',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/monika-sahay/simplevcs',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
