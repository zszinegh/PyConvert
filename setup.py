from distutils.core import setup

setup(
    name='PyConvert',
    version='0.1.0',
    packages=['pyconvert'],
    url='',
    license='MIT',
    author='Zoltan Szinegh',
    author_email='zoltan.szinegh@gmail.com',
    description='Conversion Tool',
    scripts=['bin/pyconvert'],
    install_requires=['nose']
)
