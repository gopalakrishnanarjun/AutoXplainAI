from setuptools import setup, find_packages

setup(
    name='AutoXplainAI',
    version='0.2.0',
    description='An Automatic Model Explanation Framework',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Gopalakrishnan Arjunan',
    author_email='gopalakrishnana02@gmail.com',
    url='https://github.com/gopalakrishnanarjun/AutoXplainAI.git',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)