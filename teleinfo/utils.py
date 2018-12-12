#!/usr/bin/env python

def frame_to_json():
    import logging
    logging.basicConfig()

    import sys
    import teleinfo
    from teleinfo.hw_vendors import RpiDom, SolarBox_USB
    import getopt
    import json

    ps_name = sys.argv[0]
    argv = sys.argv[1:]

    SUPPORTED_DEVICES = {
        "RpiDom": RpiDom,
        "SolarBox_USB": SolarBox_USB
    }

    def usage():
        print("{} -d|--device <hw_device>".format(ps_name))
        print("{} [-h|--help]".format(ps_name))
        print("")
        print("Supported hardware devices are:")
        print("  {}".format(SUPPORTED_DEVICES.keys()))

    device = None
    try:
        opts, args = getopt.getopt(argv, "hd:", ["help", "device="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-d", "--device"):
            try:
                device = SUPPORTED_DEVICES.get(arg)
            except KeyError:
                print("Invalid device: {}".format(arg))
                usage()
                sys.exit(2)
    if device is None:
      print("Missing device argument")
      usage()
      sys.exit(2)

    ti = teleinfo.Parser(device())
    print(json.dumps(ti.get_frame(), indent=2, separators=(',', ':')))
