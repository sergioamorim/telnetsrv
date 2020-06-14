from distutils.core import setup


def from_file(file):
  with open(file=file) as f:
    return f.read()


setup(
  name="telnetsrv",
  packages=["telnetsrv"],
  package_dir={'': '.'},
  version="0.4.1",
  description="Telnet server handler library",
  long_description=from_file('README.rst'),
  author="Sergio",
  author_email="sata@ic.ufal.br",
  url="https://github.com/sergioamorim/telnetsrv",
  license=from_file('LICENSE'),
  platforms="Linux, Windows",
)
