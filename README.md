# fino

[![PyPI version](https://img.shields.io/pypi/v/fino.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/fino/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/fino.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/fino/)
[![PyPI downloads](https://img.shields.io/pypi/dm/fino.svg)](https://pypistats.org/packages/fino)
[![GitHub Actions status](https://github.com/hugovk/fino/actions/workflows/test.yml/badge.svg)](https://github.com/hugovk/fino/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/hugovk/fino/branch/main/graph/badge.svg)](https://codecov.io/gh/hugovk/fino)
[![Licence](https://img.shields.io/github/license/hugovk/fino.svg)](LICENSE.txt)
[![DOI](https://zenodo.org/badge/24323566.svg)](https://zenodo.org/badge/latestdoi/24323566)
[![Code style: Black](https://img.shields.io/badge/code%20style-Black-000000.svg)](https://github.com/psf/black)

Output the Finnish word for a given integer.

- Used by [hugovk/everyfinnishno](https://github.com/hugovk/everyfinnishno) to tweet
  [@EveryFinnishNo](https://twitter.com/EveryFinnishNo).

## Installation

### From PyPI

```bash
pip install fino
```

### From source

```bash
pip install -U git+https://github.com/hugovk/fino
```

### From requirements.txt

```txt
-e git://github.com/hugovk/fino.git#egg=pylast
```

## Usage

```pycon
>>> import fino
>>> fino.to_finnish(123)
'satakaksikymmentäkolme'
>>> fino.to_finnish(123_456)
'satakaksikymmentäkolmetuhattaneljäsataaviisikymmentäkuusi'
>>> fino.to_finnish(123_456_789)
'satakaksikymmentäkolmemiljoonaaneljäsataaviisikymmentäkuusituhattaseitsemänsataakahdeksankymmentäyhdeksän'
>>> fino.to_finnish(123_456_789_012)
'satakaksikymmentäkolmemiljardianeljäsataaviisikymmentäkuusimiljoonaaseitsemänsataakahdeksankymmentäyhdeksäntuhattakaksitoista'
>>> fino.to_finnish(123_456_789_012_345)
'satakaksikymmentäkolmebiljoonaaneljäsataaviisikymmentäkuusimiljardiaseitsemänsataakahdeksankymmentäyhdeksänmiljoonaakaksitoistatuhattakolmesataaneljäkymmentäviisi'
>>> fino.to_finnish(123_456_789_012_345_678)
'satakaksikymmentäkolmetuhattaneljäsataaviisikymmentäkuusibiljoonaaseitsemänsataakahdeksankymmentäyhdeksänmiljardiakaksitoistamiljoonaakolmesataaneljäkymmentäviisituhattakuusisataaseitsemänkymmentäkahdeksan'
```
