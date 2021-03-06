from setuptools import setup

setup(
    name='portalutils',
    packages=['portalutils'],
    version='0.0.3',
    url='https://github.com/Jack-Kingdom/portalutils.git',
    description='Portal access utility.',
    long_description=open('README.md').read(),

    author='Jack King',
    author_email='email@qiaohong.org',
    license='MIT',

    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',
    ], install_requires=['requests']
)
