from distutils.core import setup

setup(name='django-clicktale',
      version='1.0.0',
      description='A simple Django application to integrate ClickTale into your projects',
      author='Adrian Buturca',
      author_email='adrian.buturca@3pillarglobal.com',
      url='http://github.com/clintecker/django-google-analytics/tree/master',
      packages=['clicktale','clicktale.templatetags',],
      package_data={'clicktale': ['templates/clicktale/*.html']},
      classifiers=['Development Status :: 1 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
