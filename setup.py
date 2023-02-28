from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'say',
    version = '0.0.1',
    author = 'Adonai Afewerki',
    author_email = 'john.doe@foo.com',
    license = 'Apache License 2.0',
    description = 'A program that will use gTTS to make a tts file then read it to you',
    long_description = long_description,
    long_description_content_type = "Use method",
    url = 'None yet',
    py_modules = ['my_tool', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        say=my_tool:cli
    '''
)