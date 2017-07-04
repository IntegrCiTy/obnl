from setuptools import setup, find_packages
from setuptools.config import read_configuration
import platform

conf_dict = read_configuration('./setup.cfg')

setup(name=conf_dict['name'],
      maintainer=conf_dict['maintainer'],
      maintainer_email=conf_dict['maintainer_email'],
      url=conf_dict['url'],
      version=conf_dict['release'],
      platforms=[platform.platform()],  # TODO indicate really tested platforms

      packages=find_packages(),
      install_requires=conf_dict['required'],

      # metadata

      description=conf_dict['summary'],
      long_description=conf_dict['description_file'],

      license=conf_dict['licence'],

      keywords=conf_dict['keywords'],

      classifiers=conf_dict['classifiers'],
      )
