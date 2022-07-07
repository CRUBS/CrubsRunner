# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Axel Tremaudant on 10/06/2022

from PySide6 import QtCore, QtWidgets, QtGui


class InitData:
    def __init__(self):
        self.window = {
            'name_tool_bar': "Projet",
            'tool_bar_movable': False,
            'speed_tip': "Vitesse de deplacement du robot",

            'new_project_name': "Nouveau",
            'new_project_status_tip': "Creer un nouveau projet",
            'new_project_shortcut': QtGui.QKeySequence.New,  # Ctrl + N
            'new_project_icon': QtGui.QIcon("icon/icon_new.png"),

            'open_project_name': "Ouvrir",
            'open_project_shortcut': QtGui.QKeySequence.Open,  # Ctrl + O
            'open_project_status_tip': "Ouvrir un projet",
            'open_project_icon': QtGui.QIcon("icon/icon_open.png"),
            'open_project_dialog_title': "Ouvrir un projet",

            'save_project_name': "Enregistrer",
            'save_project_shortcut': QtGui.QKeySequence.Save,  # Ctrl + S
            'save_project_status_tip': "Enregistrer le projet",
            'save_project_icon': QtGui.QIcon("icon/icon_save.png"),

            'save_as_project_name': "Enregistrer sous",
            'save_as_project_shortcut': QtGui.QKeySequence.SaveAs,  # Ctrl + Shift + S
            'save_as_project_status_tip': "Enregistrer sous le projet",
            'save_as_project_icon': QtGui.QIcon("icon/icon_save_as.png"),
            'save_as_project_dialog_title': "Enregistrer le projet",
            'project_extension': "CrubsRunner project (*.crp)",
            'saving_file_first_line': "## Fichier de sauvegarde de projet CrubsRunner du {date}\n",
            'window_first_line': "\n## Window\n",
            'grid_first_line': "\n## Grid\n",
            'board_first_line': "\n## Board\n",
            'main_robot_first_line': "\n## Main robot\n",
            'second_robot_first_line': "\n## Second robot\n",
            'gcrubs_first_line': "\n## gcrubs\n",

            'import_name': "Importer",
            'import_shortcut': QtGui.QKeySequence.Italic,  # Ctrl + I
            'import_status_tip': "Importer un composant",
            'import_icon': QtGui.QIcon("icon/icon_import"),
            'import_dialog_title': "Choisir le composant a importer",
            'import_dialog_modal': True,
            'import_radio_board_name': "Plateau",
            'import_radio_main_robot_name': "Robot principal",
            'import_radio_second_robot_name': "Robot secondaire",
            'import_radio_main_robot_checked': False,
            'import_radio_board_checked': True,
            'import_radio_second_robot_checked': False,
            'import_cancel_btn_name': "Annuler",
            'import_ok_btn_name': "Valider",
            'import_cancel_btn_checked': True,
            'import_ok_btn_checked': False,

            'export_name': "Exporter",
            'export_shortcut': QtGui.QKeySequence(QtCore.Qt.CTRL | QtCore.Qt.Key_E),
            'export_status_tip': "Exporter un composant",
            'export_icon': QtGui.QIcon("icon/icon_export"),
            "export_dialog_title": "Exporter un composant",  # Other parameters : same as import

            'top_view_action_name': "Vue de dessus",
            'top_view_action_shortcut': QtGui.QKeySequence.AddTab,  # Ctrl + T
            'top_view_action_status_tip': "Vue de dessus",
            'top_view_action_icon': QtGui.QIcon("icon/icon_top_view.png"),

            'start_view_action_name': "Vue de depart",
            'start_view_action_shortcut': QtGui.QKeySequence.Underline,  # Ctrl + U
            'start_view_action_status_tip': "Vue de depart",
            'start_view_action_icon': QtGui.QIcon("icon/icon_start_view.png"),

            'bottom_view_action_name': "Vue de dessous",
            'bottom_view_action_shortcut': QtGui.QKeySequence.Bold,  # Ctrl + B
            'bottom_view_action_status_tip': "Vue de dessous",
            'bottom_view_action_icon': QtGui.QIcon("icon/icon_bottom_view.png"),

            'undo_name': "Annuler le deplacement",
            'undo_shortcut': QtGui.QKeySequence.Undo,  # Ctrl + Z
            'undo_status_tip': "Annuler le deplacement",
            'undo_icon': QtGui.QIcon("icon/icon_undo.png"),
            'max_len_doing': 50,

            'redo_name': "Remettre le deplacement",
            'redo_shortcut': QtGui.QKeySequence.Redo,  # Ctrl + Shift + Z ou Ctrl + Y
            'redo_status_tip': "Remettre le deplacement",
            'redo_icon': QtGui.QIcon("icon/icon_redo.png"),

            'window_title': "CrubsRunner",
            'accept_drops': True,
            'window_start_width': 1200,
            'window_start_height': 800,

            'add_component_dock_area': QtCore.Qt.RightDockWidgetArea,  # Place le dockWidget a droite
            'name_component_dock': "Composants",
            'component_dock_allowed_areas': QtCore.Qt.RightDockWidgetArea | QtCore.Qt.LeftDockWidgetArea,
            'component_dock_features': QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable,  # Ne peut etre ferme
            'properties_dock_allowed_areas': QtCore.Qt.RightDockWidgetArea | QtCore.Qt.LeftDockWidgetArea,
            'add_properties_dock_area': QtCore.Qt.RightDockWidgetArea,
            'properties_dock_features': QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable,
            'sequence_dock_allowed_areas': QtCore.Qt.RightDockWidgetArea | QtCore.Qt.LeftDockWidgetArea,
            'add_sequence_dock_area': QtCore.Qt.LeftDockWidgetArea,
            'sequence_dock_features': QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable,

            'import_message_box_type': QtWidgets.QMessageBox.Warning,
            'import_message_box_title': "Erreur d'importation",
            'import_message_box_message': "Vous devez supprimer le composant avant d'en importer un autre.",
            "drop_message_box_message": "Les deux robots sont deja attribues, veuillez en supprimer un avant "
                                        "d'en ajouter un autre.",

            'status_bar_message': "Position du {element} : ({x}, {y}) mm",
            'color_status_message': "Couleur : r = {r}, v = {v}, b = {b} ",
            'position_status_message': "Position : x = {x} mm, y = {y} mm, angle = {angle} degres ",

            'menu_bar_menu1': "&Fichier",
            'menu_bar_menu2': "&Edition",
            'menu_bar_menu3': "&Run",

            'error_open_file_type': QtWidgets.QMessageBox.Critical,
            'error_open_file_title': "Fichier non trouve",
            'error_open_file_message': "Le fichier '{filename}' n'a pas ete trouve.'"
        }

        self.board = {
            'type': "board",
            'name': "Plateau",
            'file': "",

            'new_message_box_type': QtWidgets.QMessageBox.Information,
            'new_message_box_title': "Information",
            'new_message_box_message': "Choisir le plateau",
            'file_dialog_open_title': "Choisir le plateau",
            'file_dialog_open_extensions': "All files (*.stl *.crb) ;; STL (*.stl) ;; CrubsRunner board (*.crb)",
            'save_extension': "CrubsRunner board (*.crb)",
            'color': (255 / 255, 211 / 255, 133 / 255, 1),  # de 0 a 1
            'edge_color': (105 / 255, 105 / 255, 105 / 255, 1),  # de 0 a 1

            'element_name': "Plateau",
            'appearance_translation_x': -1500,
            'appearance_translation_y': 1000,
            'appearance_translation_z': 0,

            'window_title': "Proprietes du plateau",

            'color_name': "Choisir la couleur du plateau",
            'color_cursor': QtCore.Qt.PointingHandCursor,
            'color_default': False,
            'color_dialog_title': "Couleur du plateau",
            'edge_color_name': "Choisir la couleur des bords",
            'edge_color_default': False,
            'edge_color_dialog_title': "Couleur des bords du plateau",

            'close_btn_name': "Fermer",
            'close_cursor': QtCore.Qt.PointingHandCursor,
            'close_default': True,
            'reset_btn_name': "Reset",
            'reset_cursor': QtCore.Qt.PointingHandCursor,
            'reset_default': False,
            'remove_btn_name': "Supprimer",
            'remove_default': False,
            'remove_cursor': QtCore.Qt.PointingHandCursor,

            'remove_message_box_type': QtWidgets.QMessageBox.Question,
            'remove_message_box_title': "Suppression d'element",
            'remove_message_box_message': "Etes-vous sur de vouloir supprimer le plateau ?\n"
                                          "Cette action est irreversible.",
            'remove_message_box_buttons': QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes,
        }

        self.main_robot = {
            'type': "robot",
            'name': "Robot principal",
            'file': "",

            'new_message_box_type': QtWidgets.QMessageBox.Information,
            'new_message_box_title': "Information",
            'new_message_box_message': "Choisir le robot principal",
            'file_dialog_open_title': "Choisir le robot principal",
            'file_dialog_open_extensions': "All files (*.stl *.crr)) ;; STL (*.stl) ;; CrubsRunner robot (*.crr)",
            'color': (29 / 255, 144 / 255, 18 / 255, 1),  # de 0 a 1
            'edge_color': (12 / 255, 73 / 255, 10 / 255, 1),  # de 0 a 1
            'save_extension': "CrubsRunner robot (*.crr)",

            'element_name': "Robot principal",
            'appearance_translation_x': 0,
            'appearance_translation_y': 0,
            'appearance_translation_z': 0,

            'window_title': "Proprietes du robot principal",
            'color_name': "Choisir la couleur du robot",
            'edge_color_name': "Choisir la couleur des bords",
            'color_dialog_title': "Couleur du robot",
            'edge_color_dialog_title': "Couleur des bords",
            'remove_message_box_message': "Etes-vous sur de vouloir supprimer le robot principal ?\n"
                                          "Cette action est irreversible.",
            'axis_rotation_x_name': "x",
            'axis_rotation_y_name': "y",
            'axis_rotation_z_name': "z",
            'angle_rotation_min': -180,
            'angle_rotation_max': 180,

            'gb_name': "Mise en place du robot sur le plateau",
            'angle_lbl_name': "Angle : ",
            'axis_lbl_name': "Axe de rotation : ",
            'offset_lbl_name': "Hauteur : ",
            'offset_sb_min': -3000,
            'offset_sb_max': 3000,
            'invisible_coef': 1000,

            'speed_lbl': "Vitesse (mm/s) : ",
            'speed_min': 1,
            'speed_max': 1000,
            'speed_rotation_lbl': "Vitesse de rotation (degres/s) : ",
            'rotation_min':  1,
            'rotation_max': 360,
            'gb_speed_name': "Vitesses",

            'sequence_btn_name': "Creer la sequence du robot",
            'sequence_btn_default': False,
            'sequence_btn_cursor': QtCore.Qt.PointingHandCursor,

            'import_gcrubs_btn_name': "Importer le fichier sequentiel",
            'import_gcrubs_btn_default': False,
            'import_gcrubs_btn_cursor': QtCore.Qt.PointingHandCursor,
            'import_gcrubs_title': "choisir le fichier sequentiel",
            'import_gcrubs_extension': "Fichier sequentiel (*.gcrubs)",

            'sequence_dialog_title': "Sequence du robot principal",
            'sequence_text': "{comment} Sequence gcrubs generee par CrubsRunner le {date} pour le robot principal.\n",
            'sequence_save_btn_name': "Enregistrer",
            'sequence_save_btn_default': True,
            'sequence_save_btn_cursor': QtCore.Qt.PointingHandCursor,
            'sequence_cancel_btn_name': "Fermer",
            'sequence_cancel_btn_default': False,
            'sequence_cancel_btn_cursor': QtCore.Qt.PointingHandCursor,
            'save_sequence_title': "Sauvegarder le fichier genere",
            'date_format': "dd/MM/yy",

            'list_sorting_order': QtCore.Qt.AscendingOrder,
            'sequence_speed_lbl_text': "Vitesse du robot : ",

            'sequence_origin_lbl_text': "Placer le robot sur l'origine\n"
                                        "(axe z (en bleu) au niveau de\n"
                                        "l'axe de rotation).",
            'sequence_origin_lbl_text_start': "Placer le robot en position de depart.",
            'start_sequence_text': "{comment} Position de depart : x = {x} mm, y = {y} mm, angle = {angle} degres\n",
            'sequence_origin_btn_name': "Fait",
            'sequence_origin_btn_default': True,
            'sequence_origin_btn_cursor': QtCore.Qt.PointingHandCursor,
        }

        self.second_robot = {
            'type': "robot",
            'name': "Robot secondaire",
            'file': "",

            'new_message_box_type': QtWidgets.QMessageBox.Question,
            'new_message_box_title': "Question",
            'new_message_box_message': "Y a-t-il un second robot ?",
            'new_message_box_buttons': QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes,
            'file_dialog_open_title': "Choisir le robot secondaire",
            'file_dialog_open_extensions': "All files (*.stl *.crr) ;; STL (*.stl) ;; CrubsRunner robot (*.crr)",
            'color': (40 / 255, 49 / 255, 255 / 255, 1),  # de 0 a 1
            'edge_color': (11 / 255, 33 / 255, 180 / 255, 1),  # de 0 a 1
            'save_extension': "CrubsRunner robot (*.crr)",

            'element_name': "Robot secondaire",
            'appearance_translation_x': 0,
            'appearance_translation_y': 0,
            'appearance_translation_z': 0,

            'window_title': "Proprietes du robot secondaire",
            'remove_message_box_message': "Etes-vous sur de vouloir supprimer le robot secondaire ?\n"
                                          "Cette action est irreversible.",

            'sequence_dialog_title': "Sequence du robot secondaire",
            'sequence_text': "{comment} Sequence gcrubs generee par CrubsRunner le {date} pour le robot secondaire.\n\n"
        }

        self.view = {
            'start_view_position_rotation': QtGui.QQuaternion.fromEulerAngles(QtGui.QVector3D(-45, 0, 0)),
            'start_view_position_distance': 4000,
            'start_view_position_pos': QtGui.QVector3D(0, 0, 0),

            'top_view_position_elevation': 90,
            'bottom_view_position_elevation': -90,

            'moving_cursor': QtCore.Qt.DragMoveCursor,
            'rotation_view_key': QtCore.Qt.MouseButton.LeftButton,
            'moving_view1': QtCore.Qt.KeyboardModifier.ControlModifier,  # & ev.modifiers()
            'moving_view_middle_button': QtCore.Qt.MouseButton.MiddleButton,
            'moving_view_middle_button1': QtCore.Qt.KeyboardModifier.ControlModifier,  # & ev.modifiers()
            'moving_view2': QtCore.Qt.MouseButton.RightButton,

            'coord_sys_name': "Repere",
            'coord_sys_file': "coord_sys.stl",
            'coord_sys_visible': True,
            'coord_sys_x_color': (1., 0., 0., 1.),
            'coord_sys_y_color': (0., 1., 0., 1.),
            'coord_sys_z_color': (0., 0., 1., 1.),
        }

        self.grid = {
            'element_name': "Grille",
            'height': 2000,
            'width': 3000,
            'spacing_height': 100,
            'spacing_width': 100,
            'color': (255, 255, 255, 75),  # de 0 a 255
            'transparency': 75,
            'visible': True,

            'coord_sys_name': "Voir le repere",
            'coord_sys_visible': True,

            'see_name': "Voir la grille",
            'width_name': "Largeur du carreau (mm) :",
            'width_min': 1,
            'width_max': 2000,

            'height_name': "Hauteur du carreau (mm) :",
            'height_min': 1,
            'height_max': 3000,

            'color_name': "Choisir la couleur",
            'color_default': False,
            'color_cursor': QtCore.Qt.PointingHandCursor,

            'transparency_name': "Transparence : ",

            'close_name': "Fermer",
            'close_default': True,
            'close_cursor': QtCore.Qt.PointingHandCursor,

            'reset_name': "Reset",
            'reset_default': False,
            'reset_cursor': QtCore.Qt.PointingHandCursor,

            'window_name': "Proprietes de la grille",
            'window_modal': True,

            'color_dialog_name': "Choisir la couleur de la grille",

            'group_box_name': "Grille"
        }

        self.gcrubs = {
            'extension': "Sequence CrubsRunner (*.gcrubs)",
            'edit_action_name': "Editer les commandes gcrubs",
            'edit_action_status_tip': "Editer les commandes gcrubs",
            'edit_action_icon': QtGui.QIcon("icon/icon_edit_gcrubs.png"),
            'edit_window_title': "Editer les commandes gcrubs",
            'description_lbl_text': "Remplir a gauche la description de ce que fait l'action et a droite "
                                    "la sequence correspondante.\n"
                                    "Mettre entre crochets ce qui peut varier. Les variables 'dist', 'angle' et 'temps'"
                                    " sont connues et sont a utiliser\n"
                                    "(les unites sont respectivement 'millimetre', 'degre' et 'seconde').",
            'apply_btn_name': "Appliquer",
            'apply_btn_default': True,
            'apply_btn_cursor': QtCore.Qt.PointingHandCursor,
            'cancel_btn_name': "Annuler",
            'cancel_btn_default': False,
            'cancel_btn_cursor': QtCore.Qt.PointingHandCursor,
            'add_btn_name': "Ajouter une commande",
            'add_btn_default': False,
            'add_btn_cursor': QtCore.Qt.PointingHandCursor,

            'key_btn_tip': "Choisir la touche associee",
            'del_btn_tip': "Supprimer la commande",
            'btn_cursor': QtCore.Qt.PointingHandCursor,
            'del_btn_icon': QtGui.QIcon("icon/icon_del.png"),
            'key_btn_icon': QtGui.QIcon('icon/icon_key.png'),
            'sa_height': 430,
            'sa_width': 720,
            'window_modal': True,

            'key_dialog_title': "Definir le mouvement associe",
            'key_lbl_text': "Appuyer sur la touche correspondant a l'instruction\n"
                            "'{instruction}'\n"
                            "Touche : ",
            'key_close_name': "Fermer",
            'key_close_cursor': QtCore.Qt.PointingHandCursor,
            'key_close_default': True,
            'period': 100  # ms
        }

        self.run = {
            'run_action_name': "Lancer une simulation",
            'run_action_shortcut': QtGui.QKeySequence(QtCore.Qt.CTRL | QtCore.Qt.Key_R),
            'run_action_tip': "Lancer une simulation",
            'run_action_icon_stopped': QtGui.QIcon("icon/icon_run_stopped.png"),
            'run_action_icon_running': QtGui.QIcon("icon/icon_run_running.png"),

            'stop_run_action_name': "Arreter la simulation",
            'stop_run_action_shortcut': QtGui.QKeySequence(QtCore.Qt.CTRL | QtCore.Qt.Key_R | QtCore.Qt.SHIFT),
            'stop_run_action_tip': "Arreter la simulation",
            'stop_run_action_icon': QtGui.QIcon("icon/icon_stop_run.png"),

            'dialog_title': "Choix du robot a simuler",
            'dialog_modal': True,
            'main_robot_cb_name': "Robot principal",
            'main_robot_cb_checked': False,
            'second_robot_cb_name': "Robot secondaire",
            'second_robot_cb_checked': False,
            'cancel_btn_name': "Annuler",
            'cancel_btn_default': False,
            'ok_btn_name': "Valider",
            'ok_btn_default': True,

            'window_title': "Simulation",
            'cmd_lbl_main': "Commande robot principal : {cmd}",
            'cmd_lbl_second': "Commande robot secondaire : {cmd}",
            'time_lbl': "Chrono : {time} s",
            'timer_refresh': 1000,  # ms
            'accuracy_timer': None,  # None pour ne pas voir les chiffres apres la virgule
            'time_before_start': 2000  # ms
        }

        self.extensions = {
            'project': ".crp",
            'board': ".crb",
            'robot': ".crr",
            'sequence': ".gcrubs",
            '3d_file': ".stl"
        }

    def get_window(self, key: str):
        return self.window.get(key)

    def get_board(self, key: str):
        return self.board.get(key)

    def get_main_robot(self, key: str):
        return self.main_robot.get(key)

    def get_second_robot(self, key: str):
        return self.second_robot.get(key)

    def get_view(self, key: str):
        return self.view.get(key)

    def get_grid(self, key: str):
        return self.grid.get(key)

    def get_extension(self, key: str):
        if key == 'value':
            return self.extensions.values()
        else:
            return self.extensions.get(key)

    def get_gcrubs(self, key: str):
        return self.gcrubs.get(key)

    def get_run(self, key: str):
        return self.run.get(key)


class SaveData:
    def __init__(self):
        self.init_data = InitData()

        self.window = {
            'directory': "",
            'project_file': ""
        }

        self.grid = {
            'height': self.init_data.get_grid('spacing_height'),
            'width': self.init_data.get_grid('spacing_width'),
            'transparency': self.init_data.get_grid('transparency'),
            'color': self.init_data.get_grid('color'),
            'visible': self.init_data.get_grid('visible'),

            'coord_sys_visible': self.init_data.get_grid('coord_sys_visible'),
            'moving_speed': 10
        }

        self.board = {
            'file': "",
            'color': self.init_data.get_board('color'),
            'edge_color': self.init_data.get_board('edge_color')
        }

        self.main_robot = {
            'file': "",
            'color': self.init_data.get_main_robot('color'),
            'edge_color': self.init_data.get_main_robot('edge_color'),
            'angle_rotation': 0,
            'axis_rotation': 'x',
            'offset': 0,
            'speed': 200,
            'speed_rotation': 45,
            'gcrubs_file': "",
            'sequence': "",
            'start_position': (0, 0, 0)  # x, y, angle
        }

        self.second_robot = {
            'file': "",
            'color': self.init_data.get_second_robot('color'),
            'edge_color': self.init_data.get_second_robot('edge_color'),
            'angle_rotation': 0,
            'axis_rotation': 'x',
            'offset': 0,
            'speed': 200,
            'speed_rotation': 45,
            'gcrubs_file': "",
            'sequence': "",
            'start_position': (0, 0, 0)  # x, y, angle
        }

        self.gcrubs = {
            'cmd_name': {
                'Commentaire': ";;",
                'Pause': "ts;;{temps};;",
                "Se deplacer en avant": "cm;;8;;{dist};;",
                "Se deplacer en arriere": "cm;;2;;{dist};;",
                "Tourner a droite": "cm;;5;;{angle};;",
                "Tourner a gauche": "cm;;0;;{angle};;",
            },

            'cmd_key': {
                'Commentaire': None,
                'Pause': None,
                "Se deplacer en avant": QtCore.Qt.Key_Up,
                "Se deplacer en arriere": QtCore.Qt.Key_Down,
                "Tourner a droite": QtCore.Qt.Key_D,
                "Tourner a gauche": QtCore.Qt.Key_Q,
            }
        }

    def get_window(self, key: str):
        return self.window.get(key)

    def set_window(self, key: str, value):
        self.window[key] = value

    def get_board(self, key: str):
        return self.board.get(key)

    def set_board(self, key: str, value):
        self.board[key] = value

    def get_main_robot(self, key: str):
        return self.main_robot.get(key)

    def set_main_robot(self, key: str, value):
        self.main_robot[key] = value

    def get_second_robot(self, key: str):
        return self.second_robot.get(key)

    def set_second_robot(self, key: str, value):
        self.second_robot[key] = value

    def get_grid(self, key: str):
        return self.grid.get(key)

    def set_grid(self, key: str, value):
        if key == 'transparency':
            self.grid['color'] = (
                self.grid.get('color')[0], self.grid.get('color')[1], self.grid.get('color')[2], value)

        self.grid[key] = value

    def get_gcrubs(self, key: str):
        return self.gcrubs.get(key)

    def set_gcrubs(self, key: str, value):
        if value != dict():  # Si c'est pas un dico vide
            self.gcrubs[key] = value

    def save(self, to_save):
        ans = ""
        if to_save == 'window':
            ans = self.init_data.get_window('window_first_line')
            for key, value in zip(self.window.keys(), self.window.values()):
                ans += str(key) + " = '" + str(value) + "'\n"

        elif to_save == 'board':
            ans = self.init_data.get_window('board_first_line')
            for key, value in zip(self.board.keys(), self.board.values()):
                ans += str(key) + " = '" + str(value) + "'\n"

        elif to_save == 'main_robot':
            ans = self.init_data.get_window('main_robot_first_line')
            for key, value in zip(self.main_robot.keys(), self.main_robot.values()):
                ans += str(key) + " = '" + str(value) + "'\n"

        elif to_save == 'second_robot':
            ans = self.init_data.get_window('second_robot_first_line')
            for key, value in zip(self.second_robot.keys(), self.second_robot.values()):
                ans += str(key) + " = '" + str(value) + "'\n"

        elif to_save == 'grid':
            ans = self.init_data.get_window('grid_first_line')
            for key, value in zip(self.grid.keys(), self.grid.values()):
                ans += str(key) + " = '" + str(value) + "'\n"

        elif to_save == 'gcrubs':
            ans = self.init_data.get_window('gcrubs_first_line')
            for key, value in zip(self.gcrubs.keys(), self.gcrubs.values()):
                ans += str(key) + " = " + str(value) + "\n"

        return ans

    def get_len_cmd(self) -> int:
        return len(self.gcrubs.get('cmd_name'))

    def get_len(self, dictionary: str) -> int:
        if dictionary == 'window':
            return len(self.window)
        elif dictionary == 'board':
            return len(self.board)
        elif dictionary == 'main_robot':
            return len(self.main_robot)
        elif dictionary == 'second_robot':
            return len(self.second_robot)
        elif dictionary == 'grid':
            return len(self.grid)
        elif dictionary == 'gcrubs':
            return len(self.gcrubs)
        else:
            return 0
