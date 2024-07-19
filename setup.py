from setuptools import setup, find_packages

long_description = open('README.md').read()

setup(
  name = 'yaapt.torch',
  packages = find_packages(),
  version = '1.0.0',
  license = 'Apache 2.0',
  description = 'YAAPT Pitch Tracking function in PyTorch ',
  long_description = long_description,
  long_description_content_type="text/markdown",
  author = 'Pierre Champion',
  url = 'https://github.com/pchampio/yaapt.torch',
  keywords = [
    'pitch',
    'F0',
    'yaapt',
    'pytorch',
    'torch'
  ],
  install_requires=[
    'torch>=1.5',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
