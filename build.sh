rm -rf *egg-info build dist

python3 setup.py build sdist bdist_wheel

rm -rf *egg-info build