#!/usr/bin/env python
"""
Script to run VetRedRockGui
"""
from __future__ import print_function, absolute_import
from __future__ import division, unicode_literals

# import pdb

try:
    ustr = unicode
except NameError:
    ustr = str


def parser(options=None):
    """ Parser for auto VetRedRockGui
    Parameters
    ----------
    options

    Returns
    -------

    """

    import argparse

    parser = argparse.ArgumentParser(description='Run the VetRedRockGUI on\
                                     RedRock output')
    parser.add_argument(
        "-i",
        "--initials",
        type=str,
        help="optional: create new output with your initials")

    if options is None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(namespace=options)
    return args


def main(args=None):
    pargs = parser(options=args)
    import sys
    import os
    from linetools import utils as ltu
    from vetrr.vet_redrock import VetRedRockGui
    from PyQt5.QtWidgets import QApplication
    from collections import OrderedDict
    import yaml
    import glob

    if pargs.initials:
        initials = pargs.initials
    else:
        initials = None
    print(initials)

    # get the local red rock file (input to vetrr)
    # first check if its there, if not look above
    if len(glob.glob("J*_rr.fits")) != 0:
        infile = glob.glob("J*_rr.fits")[0]
    elif glob.glob("J*_rr.fits") == 0:
        infile = glob.glob("../J*_rr.fits")[0]
    else:
        import pdb
        pdb.set_trace()

    # Get the coadd_file (yaml)
    if len(glob.glob("J*coadd.yaml")) != 0:
        coadd = glob.glob("J*coadd.yaml")[0]
    else:
        import pdb
        pdb.set_trace()

    # check to see if there are any previous vetrr.json files
    outguess = glob.glob("J*vetrr*.json")
    # This is the case when no initials were supplied but no
    #   previous json file either.
    if len(outguess) == 0:
        if initials is not None:
            outfile = infile[:-7] + "vetrr_" + initials + ".json"
        else:
            print("need an outfile and initials")
            import pdb
            pdb.set_trace()
    elif initials is not None:
        print("Createing a new output file")
        outfile = infile[:-7] + "vetrr_" + initials + ".json"
    else:
        outfile = outguess[0]

    print(outfile, initials)
    import pdb
    pdb.set_trace()

    print("******************************************************")
    print("Auto found these files:")
    print("INFILE:", infile)
    print("OUTFILE:", outfile)
    print("COADD:", coadd)
    print("****************************************************** \n")

    # Load outfile if it exists
    if os.path.isfile(outfile):
        print("******************************************************")
        print("WARNING:  Loading previous file and will over-write it!")
        print("******************************************************")
        zdict = ltu.loadjson(outfile)
        zdict = OrderedDict(zdict)
    else:
        zdict = None

    # YAML coadd file?
    if coadd is not None:
        # Load the input file
        with open(coadd, 'r') as in_file:
            coadd_dict = yaml.load(in_file)

    app = QApplication(sys.argv)
    gui = VetRedRockGui(
        infile, outfile=outfile, zdict=zdict, coadd_dict=coadd_dict)
    gui.show()
    app.exec_()


if __name__ == '__main__':
    main()
