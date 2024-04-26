from setuptools import setup, find_packages

setup(
    name='cipher_tool',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'colorama',
        # Add any other dependencies your project needs here
    ],
    entry_points={
        'console_scripts': [
            'cipher-tool = cipher_tool.main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool for encryption and decryption using Caesar and Substitution ciphers',
    keywords='encryption decryption caesar substitution cipher',
    url='https://github.com/yourusername/cipher_tool',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
