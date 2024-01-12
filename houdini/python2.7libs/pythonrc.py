# Copyright 2023-2024 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

import hou

import loputils


def addRendererParmFolders(node, parmgroup):
    if not loputils:
        return
    names = hou.lop.availableRendererNames()
    labels = hou.lop.availableRendererLabels()
    new_names = ["moonray"] + list(names)
    new_labels = ["Moonray"] + list(labels)

    for name, label in zip(new_names, new_labels):
        try:
            dspath = hou.findFile('soho/parameters/%s_%s.ds'
                                        % (name, parmgroup))
        except hou.OperationFailed:
            continue

        loputils.addDialogScriptFolder(dspath, node, label)


if loputils:
    loputils.addRendererParmFolders = addRendererParmFolders
