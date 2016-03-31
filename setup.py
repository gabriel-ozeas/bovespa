from setuptools import setup, find_packages

setup(name='bovespa',
      version='0.1.0',
      description='Reads historical quote files from BM&FBovespa (Brazillian Stock Exchange)',
      url='http://github.com/thypad/bovespa',
      author='Thyago Neves Porpino',
      author_email='thyago.porpino@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False)
