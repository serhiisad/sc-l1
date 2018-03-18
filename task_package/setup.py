from setuptools import setup, find_packages

setup(name='task_package',
      version='0.1',
      description='package',
      install_requires=[
          'requests'
      ],
      include_package_data=True,
      zip_safe=False)