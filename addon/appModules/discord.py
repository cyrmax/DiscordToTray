# -*- coding: utf-8 -*-


# Discord to tray
# A small addon which helps you to minimize Discord window to tray instead of closing it with alt+F4.
# Copyright (c) 2023 <Kirill Belousov cyrmax@internet.ru>
# Released under GNU GPLv3 License

import addonHandler
import appModuleHandler
import winUser
from api import getForegroundObject
from keyboardHandler import KeyboardInputGesture
from scriptHandler import script


addonHandler.initTranslation()


class AppModule(appModuleHandler.AppModule):
    # Translators: Script category for Discord to tray in input gestures dialog.
    scriptCategory = _("Discord to tray")

    @script(
        description=_(
            # Translators: Script description.
            "Minimizes Discord window to tray"
        ),
        gesture="KB:alt+F4",
    )
    def script_minimizeToTray(self, gesture: KeyboardInputGesture):
        # 0x0010 stands for WM_CLOSE WinAPI constant which is missing in NVDA winUser module.
        winUser.sendMessage(getForegroundObject().windowHandle, 0x0010, None, None)
        # After minimizing Discord to tray NVDA focus hangs in unknown state.
        # To avoid this we send alt+tab to switch focus to next visible window.
        gst = KeyboardInputGesture.fromName("alt+tab")
        gst.send()
