# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ShadowGeneratorDialog
                                 A QGIS plugin
 Simulate casting shadows
                             -------------------
        begin                : 2015-04-10
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Fredrik Lindberg
        email                : fredrikl@gvc.gu.se
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
import GdalTools_utils as Utils
import shadow_generator

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'shadow_generator_dialog_base.ui'))


class ShadowGeneratorDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ShadowGeneratorDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)


    def saveRasterFileName(self):
        lastUsedFilter = Utils.FileFilter.lastUsedRasterFilter()
        fileDialogFunc = Utils.FileDialog.getSaveFileName
        outputFile = fileDialogFunc(None, self.tr("Select the raster file to save the results to"), Utils.FileFilter.
                                   allRastersFilter(), lastUsedFilter)
        #outputFile = fileDialogFunc(None, self.tr("Select the raster file to save the results to"), "GeoTiff (*.tif)", lastUsedFilter)
        #outputFile = QFileDialog.getSaveFileName(None, "Output file", ".", "GeoTiff (*.tif)", lastUsedFilter)
        #svf_calculator.SkyViewFactorCalculator.outputFormat = Utils.fillRasterOutputFormat(lastUsedFilter, outputFile)
        #svf_calculator.SkyViewFactorCalculator.outputFile = outputFile
        Utils.FileFilter.setLastUsedRasterFilter(lastUsedFilter)
        self.textOutput.insert(outputFile)
