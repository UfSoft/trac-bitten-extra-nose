#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8
# =============================================================================
# $Id: setup.py 3 2007-02-10 23:26:46Z s0undt3ch $
# =============================================================================
#             $URL: http://bitten.ufsoft.org/svn/BittenExtraNose/trunk/setup.py $
# $LastChangedDate: 2007-02-10 23:26:46 +0000 (Sat, 10 Feb 2007) $
#             $Rev: 3 $
#   $LastChangedBy: s0undt3ch $
# =============================================================================
# Copyright (C) 2006 Ufsoft.org - Pedro Algarvio <ufs@ufsoft.org>
#
# Please view LICENSE for additional licensing information.
# =============================================================================

from setuptools import setup, find_packages

setup(
    name='BittenExtraNose',
    version='0.1',
    author='Pedro Algarvio',
    author_email = 'ufs@ufsoft.org',
    description = 'Bitten Nose plugins',
    license = 'BSD',
    packages = find_packages(),
    install_requires=['nose>=0.9.2', 'bitten==dev,>=0.6dev-r378'],
    entry_points = {
        'nose.plugins': [
            'bitten#nosetests = nosebitten.plugnose:BittenNosetests',
            'bitten#nosecoverage = nosebitten.plugnose:BittenNoseCoverage'
         ]
    }
)
