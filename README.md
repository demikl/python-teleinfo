# python-teleinfo
Read and parse teleinfo data from France EDF electricity provider

* Build: [![CircleCI](https://circleci.com/gh/demikl/python-teleinfo.svg?style=svg)](https://circleci.com/gh/demikl/python-teleinfo)
* Unit tests: [![codecov](https://codecov.io/gh/demikl/python-teleinfo/branch/master/graph/badge.svg)](https://codecov.io/gh/demikl/python-teleinfo)

Lors de l'installation, un outil CLI est installé : `bin/teleinfo_json`

## Usage

Usage du module :

```
  from teleinfo import Parser
  from teleinfo.hw_vendors import RpiDom
  ti = Parser(RpiDom())
  print ti.get_frame()
```

Le parseur supporte aussi l'itération :

```
  from teleinfo import Parser
  from teleinfo.hw_vendors import RpiDom
  for frame in Parser(RpiDom()):
      do_something_with(frame)
```

## Supported Devices

* RpiDom
* SolarBox_USB
* UTInfo 2.0 USB Dongle from Charles Hallard (http://hallard.me/utinfo/)

## Example

```
>>> import teleinfo
>>> from teleinfo import Parser
>>> from teleinfo.hw_vendors import UTInfo2
>>> ti = Parser(UTInfo2())
>>> ti.get_frame()

{'PPOT': '00', 'MOTDETAT': '000000', 'OPTARIF': 'HC..', 'IMAX3': '060', 'IMAX1': '060', 'ADCO': '021876647540', 'HCHC': '002234766', 'PAPP': '08490', 'HHPHC': 'A', 'IINST1': '010', 'IMAX2': '060', 'IINST3': '016', 'IINST2': '008', 'PTEC': 'HP..', 'ISOUSC': '20', 'PMAX': '11690', 'HCHP': '011085557'}

>>> for frame in Parser(UTInfo2()):
...     print frame
...
```
