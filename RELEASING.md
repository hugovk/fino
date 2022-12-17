# Release Checklist

- [ ] Get `main` to the appropriate code release state.
      [GitHub Actions](https://github.com/hugovk/fino/actions) should be running cleanly
      for all merges to `main`.
      [![GitHub Actions status](https://github.com/hugovk/fino/workflows/Test/badge.svg)](https://github.com/hugovk/fino/actions)

- [ ] Edit release draft, adjust text if needed: https://github.com/hugovk/fino/releases

- [ ] Check next tag is correct, amend if needed

- [ ] Publish release

- [ ] Check the tagged
      [GitHub Actions build](https://github.com/hugovk/fino/actions/workflows/deploy.yml)
      has deployed to [PyPI](https://pypi.org/project/fino/#history)

- [ ] Check installation:

```bash
pip3 uninstall -y fino && pip3 install -U fino && python3 -c "import fino; print(fino.to_finnish(123))"
```
