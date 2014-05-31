from setuptools import setup, find_packages

long_description = open('README.md').read()

try:
    # trying to convert long description from markdown to ReST
    # based on this article: https://coderwall.com/p/qawuyq
    
    import pandoc
    pandoc.core.PANDOC_PATH = 'pandoc'
    doc = pandoc.Document()
    doc.markdown = long_description
    long_description = doc.rst
    
except ImportError:
    pass

setup(
    name = 'django-globals',
    version = '0.2.1',
    description = 'Very simple application, that allow to define a thread specific global variables.',
    long_description = long_description,
    keywords = 'django apps',
    license = 'New BSD License',
    author = 'Alexander Artemenko',
    author_email = 'svetlyak.40wt@gmail.com',
    url = 'http://github.com/svetlyak40wt/django-globals/',
    install_requires = [],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    package_dir = {'': 'src'},
    packages = find_packages('src', exclude = ['example']),
    include_package_data = True,
)


