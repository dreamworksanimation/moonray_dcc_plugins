# Copyright 2023 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

set(component moonrayDccPluginsHoudini)

include(GNUInstallDirs)

install(FILES
        moonray_nodes.json
    DESTINATION
        plugin/houdini
)

install(DIRECTORY
        otls
        soho
        python2.7libs
        python3.9libs
    DESTINATION
        plugin/houdini
)

