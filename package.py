# -*- coding: utf-8 -*-

name = 'openvdb'

version = '7.1.0-houdini-18.5.351-ta.1.0.1'

authors = [
    'benjamin.skinner',
]

requires = [
    'openexr-2.4.0',
    'tbb-2019',
    'blosc-1.5',
    'hboost-1.72.0-houdini',
]

private_build_requires = [
    'python',
    'houdini-18.5.351',
]

build_command = "python {root}/rez_build.py"

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10'],
    #['platform-windows', 'arch-x64', 'os-windows-10', 'boost-1.65'],
]


def commands():

    # Split and store version and package version
    split_versions = str(version).split('-')
    env.OPENVDB_VERSION.set(split_versions[0])
    env.OPENVDB_PACKAGE_VERSION.set(split_versions[1])

    env.OPENVDB_ROOT.set("{root}")
    env.OPENVDB_ROOT_DIR.set("{root}")
    env.OPENVDB_INCLUDE_DIR.set("{root}/include")
    env.OPENVDB_LIBRARY_DIR.set("{root}/lib")
    env.OPENVDB_BINARY_DIR.set("{root}/bin")

    env.PATH.append( str(env.OPENVDB_BINARY_DIR) )
