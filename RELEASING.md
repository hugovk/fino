# Release Checklist

* [ ] Get master to the appropriate code release state. [Travis CI](https://travis-ci.org/hugovk/fino) should be running cleanly for all merges to master.
* [ ] Update version:
```bash
git checkout master
edit setup.py
```
* [ ] Commit and tag with the version number:
```bash
git add setup.py
git commit -m "Release 0.6.0"
git tag -a 0.6.0 -m "Release 0.6.0"
```
* [ ] Create a distribution and release on PyPI:
```bash
pip3 install -U pip setuptools wheel twine keyring
rm -rf build
python3 setup.py sdist --format=gztar bdist_wheel
twine check dist/fino-0.6.0*
twine upload -r pypi dist/fino-0.6.0*
```
* [ ] Check installation: `pip3 uninstall -y fino && pip install -U fino`
* [ ] Push commits and tags:
 ```bash
git push
git push --tags
```
* [ ] Create new GitHub release: https://github.com/hugovk/fino/releases/new
  * Tag: Pick existing tag "0.6.0"
