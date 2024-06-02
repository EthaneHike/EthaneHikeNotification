from setuptools import setup, find_packages

setup(
    name='EthaneHikeNotification',
    version='0.1',
    packages=find_packages(),
    description='',
    # long_description=open('README.md').read(),
    # python3，readme文件中文报错
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/EthaneHike/EthaneHikeNotification',
    author='Yang Haocheng',
    author_email='yanghaocheng@petalmail.com',
    license='MIT',
    install_requires=[

    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
