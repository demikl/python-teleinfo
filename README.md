# python-teleinfo
Read and parse teleinfo data from France EDF electricity provider

Lors de l'installation, un outil CLI est installé : `bin/teleinfo_json`

## Usage

Usage du module :

```
  from teleinfo import Teleinfo
  from teleinfo.hw_vendors import RpiDom
  ti = Teleinfo(RpiDom())
  print ti.get_frame()
```

Le parseur supporte aussi l'itération :

```
  for frame in Teleinfo(RpiDom()):
      do_something_with(frame)
```

## Supported Devices

* RpiDom
* SolarBox_USB
* UTInfo 2.0 USB Dongle from Charles Hallard (http://hallard.me/utinfo/)

