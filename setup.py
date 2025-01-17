from setuptools import setup, find_packages

setup(
    name='ColorLogger',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'colorama',
    ],
    description='A simple color logger using colorama and logging',
    author='Bhaskar Saikia',
    author_email='bhaskar.op@outlook.com',
    url='https://github.com/yourusername/my_color_logger',  # Update with your repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)