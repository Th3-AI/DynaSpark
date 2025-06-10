from setuptools import setup, find_packages
import os

# Read README with UTF-8 encoding
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="dynaspark",
    version="1.2.2.1",
    packages=find_packages(),
    install_requires=[
        "requests>=2.30.0",
        "urllib3>=2.0.0"
    ],
    author="Th3-C0der",
    author_email="dvp.ai.ml@gmail.com",
    description="A Python client for the DynaSpark API - Free AI text generation, text-to-speech, and image generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Th3-C0der/DynaSpark",
    project_urls={
        "Bug Tracker": "https://github.com/Th3-C0der/DynaSpark/issues",
        "Documentation": "https://github.com/Th3-C0der/DynaSpark#readme",
        "Source Code": "https://github.com/Th3-C0der/DynaSpark",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.6",
    keywords="ai, text-generation, image-generation, audio-generation, api, dynaspark",
    license="MIT",
    zip_safe=False,
)
