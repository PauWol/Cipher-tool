from setuptools import setup, find_packages

setup(
    name='cipher_tool',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'collections',
        'colorama',
        'tqdm'
    ],
    entry_points={
        'console_scripts': [
            'cipher-tool = cipher_tool.main:main',
        ],
    },
    author='Paul Wolf',
    author_email='your.email@example.com',
    description='A tool for encryption and decryption using Caesar and Substitution ciphers',
    keywords='encryption decryption caesar substitution cipher',
    url='https://github.com/PauWol/Cipher-tool',
       classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3',
)
