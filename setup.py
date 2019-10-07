from setuptools import setup
requirements = [
"aiohttp"
]

setup(
    name='AioQrtag',
    version='2.0',
    description=" AioQrtag",
    author="dark0ghost",
    url='https://github.com/dark0ghost/AioQrtag/',
    packages=[
        'aiohttp',
    ],
    package_dir={'aioqrtag':
                     'aioqrtag'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
)
