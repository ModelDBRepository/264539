# -*- coding: utf-8 -*-
# @Author: Theo Lemaire
# @Email: theo.lemaire@epfl.ch
# @Date:   2018-10-01 20:45:29
# @Last Modified by:   Theo Lemaire
# @Last Modified time: 2020-04-29 13:48:58

''' Utilities used across notebooks. '''

import os
import matplotlib
from PySONIC.utils import si_format
from root import dataroot

# Matplotlib parameters
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams['font.family'] = 'arial'


def subdirectory(name):
    ''' Return (and create if needed) a data sub-directory. '''
    if dataroot is None:
        raise ValueError('You must specify the data root directory')
    if not os.path.isdir(dataroot):
        raise ValueError('You must create the data root directory prior to running the code')
    subdir = os.path.join(dataroot, name)
    if not os.path.isdir(subdir):
        os.mkdir(subdir)
    return subdir


def codes(a, pneuron, Fdrive, PRF, tstim):
    ''' Return codes dictionary for a combination of parameters. '''
    return [
        pneuron.name,
        f'{si_format(a, space="")}m',
        f'{si_format(Fdrive, space="")}Hz',
        f'PRF{si_format(PRF, space="")}Hz',
        f'{si_format(tstim, space="")}s'
    ]


def saveFigsAsPDF(figs, figindex):
    ''' Save figures as PDFs with a specific figure index. '''
    figdir = subdirectory('figs')
    figbase = f'fig{figindex:02}'
    for fname, fig in figs.items():
        fig.savefig(os.path.join(figdir, f'{figbase}{fname}.pdf'), transparent=True)


def subthr(x):
    ''' Sub-threshold acoustic pressure (Pa). '''
    return x - 5e3


def suprathr(x):
    ''' Supra-threshold acoustic pressure (Pa). '''
    return x + 20e3
