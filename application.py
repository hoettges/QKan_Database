# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DoNothingYet
                                 A QGIS plugin
 Importiert Kanaldaten aus Hystem-Extran
                              -------------------
        begin                : 2016-10-06
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Jörg Höttges/FH Aachen
        email                : hoettges@fh-aachen.de
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
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon
# Initialize Qt resources from file resources.py
# import resources_rc
# Import the code for the dialog
# from k_he2qk_dialog import ImportFromHEDialog
import os.path


class DoNothingYet:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        locale = QSettings().value('locale/userLocale')[0:2]
        # locale_path = os.path.join(
            # self.plugin_dir,
            # 'i18n',
            # 'ImportFromHE_{}.qm'.format(locale))

        # if os.path.exists(locale_path):
            # self.translator = QTranslator()
            # self.translator.load(locale_path)

            # if qVersion() > '4.3.3':
                # QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        # self.menu = self.tr(u'&QKan Import from Hystem-Extran')
        # # TODO: We are going to let the user set this up in a future iteration
        # self.toolbar = self.iface.addToolBar(u'ImportFromHE')
        # self.toolbar.setObjectName(u'ImportFromHE')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('ImportFromHE', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        # icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        # action.triggered.connect(callback)
        # action.setEnabled(enabled_flag)

        # if status_tip is not None:
            # action.setStatusTip(status_tip)

        # if whats_this is not None:
            # action.setWhatsThis(whats_this)

        # if add_to_toolbar:
            # self.toolbar.addAction(action)

        # if add_to_menu:
            # self.iface.addPluginToVectorMenu(
                # self.menu,
                # action)

        # self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        pass

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""

        pass

    def run(self):
        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass
