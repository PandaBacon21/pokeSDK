from setuptools import setup, find_packages

setup(
    name='pokemon_sdk',
    version='0.1.0',
    python_requires='>=3.13',
    packages=find_packages(),
    install_requires=[
        'annotated-types==0.7.0',
        'certifi==2025.1.31',
        'charset-normalizer==3.4.1',
        'idna==3.10',
        'iniconfig==2.0.0',
        'packaging==24.2',
        'pluggy==1.5.0',
        'pydantic==2.10.6',
        'pydantic_core==2.27.2',
        'pytest==8.3.4',
        'requests==2.32.3',
        'setuptools==75.8.0',
        'tqdm==4.67.1',
        'typing_extensions==4.12.2',
        'urllib3==2.3.0',
    ],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)