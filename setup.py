import os, sys, subprocess
from setuptools import setup, find_packages 
from distutils.cmd import Command


version = "1.2.2"

f = open("README.rst")
try:
    try:
        readme_content = f.read()
    except:
        readme_content = ""
finally:
    f.close()

class doc(Command):

    description = "generate or test documentation"

    user_options = [("test", "t",
                     "run doctests instead of generating documentation")]

    boolean_options = ["test"]

    def initialize_options(self):
        self.test = False

    def finalize_options(self):
        pass

    def run(self):
        if self.test:
            path = "doc/_build/doctest"
            mode = "doctest"
        else:
            path = "doc/_build/%s" % version
            mode = "html"

            try:
                os.makedirs(path)
            except:
                pass

        status = subprocess.call(["sphinx-build", "-E", "-D", "version=%s" % version,
                                  "-b", mode, "doc", path])

        if status:
            raise RuntimeError("documentation step '%s' failed" % (mode,))

        sys.stdout.write("\nDocumentation step '%s' performed, results here:\n"
                         "   %s/\n" % (mode, path))



setup(name='telesign',
      version=version,
      description=("Telesign SDK"),
      license="MIT License",
      classifiers = [
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.4",
      ], 
      long_description=readme_content,
      keywords = 'telesign, sms, two factor authentication',
      author = 'TeleSign Corp.',
      author_email='support@telesign.com',
      url="http://github.com/telesign/python_telesign",
      install_requires=['requests>=2.8.0',
                        ],

      packages=find_packages(exclude=['test', 'test.*']),
      cmdclass={"doc": doc},
     )

