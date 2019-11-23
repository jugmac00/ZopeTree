from os import path
from setuptools import find_packages
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='Products.ZopeTree',
      version='2.0.dev2',
      url='https://github.com/jugmac00/Products.ZopeTree',
      project_urls={
          'Issue Tracker': 'https://github.com/jugmac00/Products.ZopeTree/issues',
          'Sources': 'https://github.com/jugmac00/Products.ZopeTree',
      },      
      license='MPL 1.1',
      description="ZopeTree is a light-weight tree implementation.",
      long_description=long_description,
      long_description_content_type='text/markdown',
      maintainer='Juergen Gmach',
      maintainer_email="juergen.gmach@googlemail.com",
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Zope :: 4',
        'Framework :: Zope :: 5',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
      ],
      packages=find_packages('src'),
      namespace_packages=['Products'],
      package_dir={'': 'src'},
      python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*',
      install_requires=[
        'Zope',
        'setuptools',
        'six',
        'AccessControl',
        'zope.interface',
        'zope.testing',
      ],
      include_package_data=True,
      zip_safe=False,
      options={"bdist_wheel": {"universal": "1"}},
      )
