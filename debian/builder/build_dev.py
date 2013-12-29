import os

packages = []

with open('packages.txt', 'r') as f:
  for line in f:
    pkg = line.split(',')
    packages.append(pkg[0].strip())


print ', '.join(packages)