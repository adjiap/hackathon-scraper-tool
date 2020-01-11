from setuptools import setup, find_packages

setup(
    name='WebScraping-Tool',
    version='0.4',
    install_requires=['beautifulsoup4', 'selenium', 'pandas'],
    packages=find_packages(),
    url='https://github.com/adjiap/hackathon-scraper-tool',
    license='BSD 3-Clause License',
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Environment :: Win32 (MS Windows)',
                 'Framework :: Sphinx',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: Microsoft :: Windows :: Windows 10',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.7',
                 'Topic :: Internet :: WWW/HTTP :: Browsers'
                 'Topic :: Text Processing :: Markup :: HTML'],
    author='Adji Arioputro',
    author_email='',
    description=''
)
