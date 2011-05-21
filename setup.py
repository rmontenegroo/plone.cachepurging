from setuptools import setup, find_packages

version = '1.0.1'

setup(name='plone.cachepurging',
      version=version,
      description="Cache purging support for Zope 2 applications",
      long_description=open('README.txt').read() + '\n' +
                       open('CHANGES.txt').read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone cache purge',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plone.cachepurging',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.interface',
          'zope.component',
          'zope.event',
          'zope.annotation',
          'zope.lifecycleevent',
          'zope.i18nmessageid',
          'five.globalrequest',
          'plone.registry',
          'Zope2',
      ],
      extras_require={
        'test': ['plone.app.testing'],
      },
      )
