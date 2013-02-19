from distutils.core import setup

setup(name='django-clicktale',
      version='1.0.0',
      description=('A simple Django application to integrate ClickTale into '
                   'your projects'),
      author='TPG PBS Core Services',
      keywords="django clicktale integration",
      author_email='TPG-PBS-CoreServices@3pillarglobal.com',
      url='https://github.com/pbs/django-clicktale',
      packages=['clicktale', 'clicktale.templatetags'],
      package_data={'clicktale': ['templates/clicktale/*.html']},
      classifiers=['Development Status :: 1 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
