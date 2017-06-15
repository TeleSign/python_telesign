from setuptools import setup, find_packages

version = "2.2.0"

try:
    with open("README") as f:
        readme_content = f.read()
except (IOError, Exception):
    readme_content = ""

setup(name='telesign',
      version=version,
      description="Telesign SDK",
      license="MIT License",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
      ],
      long_description=readme_content,
      keywords='telesign, sms, voice, mobile, authentication, identity, messaging',
      author='TeleSign Corp.',
      author_email='support@telesign.com',
      url="https://github.com/telesign/python_telesign",
      install_requires=['requests'],
      tests_require=['nose', 'mock', 'pytz', 'coverage', 'codecov'],
      packages=find_packages(exclude=['test', 'test.*', 'examples', 'examples.*']),
      )
