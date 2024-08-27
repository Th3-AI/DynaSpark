from setuptools import setup, find_packages

setup(
    name='dynaspark',
    version='1.1.1',
    packages=find_packages(),
    description='A client for interacting with the DynaSpark API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Th3-AI/DynaSpark',
    author='Th3-C0der',
    author_email='dvp.ai.ml@gmail.com',
    install_requires=[
        'requests>=2.30.0',
    ],
    python_requires='>=3.11',
)
