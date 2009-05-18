
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    try:
        from ez_setup import use_setuptools
    except ImportError:
        print "can't find ez_setup"
        print "try: wget http://peak.telecommunity.com/dist/ez_setup.py"
        sys.exit(1)
    use_setuptools()
    from setuptools import setup, find_packages


setup(
    name = 'setuptools_dummy',
    version = '0.0.1',
    description = 'Setuptools Dummy Filefinder',
    long_description = '\n'.join((
        'Setuptools Dummy Filefinder',
        '',
        'plugin for enabling all files integration',
        'even if they are not under version control system',
    )),
    author = 'centrum holdings s.r.o',
    author_email='devel@centrumholdings.com',
    license = 'BSD',
    url='http://git.netcentrum.cz/projects/django/GIT/setuptools_dummy.git/',

    py_modules=["setuptools_dummy"],

    include_package_data = True,

    classifiers = [
        "Topic :: Software Development :: Version Control",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
    ],
    entry_points = {
        'setuptools.file_finders': ['dummy = setuptools_dummy:dummylsfiles'],
    },
    install_requires = [
        'setuptools>=0.6b1',
    ],
)

