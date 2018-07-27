# Release Checklist

* [ ] Get master to the appropriate code release state. [Travis CI](https://travis-ci.org/hugovk/fino) should be running cleanly for all merges to master.
* [ ] Update version in `setup.py` and commit:
```bash
git checkout master
edit setup.py
git add setup.py
git commit -m "Release 0.3.0"
```
* [ ] Tag the last commit with the version number:
```bash
git tag -a 0.3.0 -m "Release 0.3.0"
```
* [ ] Release on PyPI:
```bash
pip install -U pip setuptools wheel twine keyring
python setup.py sdist --format=gztar
twine upload -r pypi dist/fino-0.3.0*
```
* [ ] Check installation: `pip install -U fino`
* [ ] Push commits and tags:
 ```bash
git push
git push --tags
```
* [ ] Create new GitHub release: https://github.com/hugovk/fino/releases/new
  * Tag: Pick existing tag "0.3.0"
  * Title: "Release 0.3.0"
