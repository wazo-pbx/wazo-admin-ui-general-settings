# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_menu.classy import register_flaskview

from wazo_admin_ui.helpers.plugin import create_blueprint

from .service import (
    SipGeneralSettingsService,
    IaxGeneralSettingsService,
    SccpGeneralSettingsService,
    VoicemailGeneralSettingsService,
    FeaturesGeneralSettingsService
)
from .view import (
    SipGeneralSettingsView,
    IaxGeneralSettingsView,
    SccpGeneralSettingsView,
    VoicemailGeneralSettingsView,
    FeaturesGeneralSettingsView
)

general_settings = create_blueprint('general_settings', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']

        SipGeneralSettingsView.service = SipGeneralSettingsService()
        SipGeneralSettingsView.register(general_settings, route_base='/sip_general_settings')
        register_flaskview(general_settings, SipGeneralSettingsView)

        IaxGeneralSettingsView.service = IaxGeneralSettingsService()
        IaxGeneralSettingsView.register(general_settings, route_base='/iax_general_settings')
        register_flaskview(general_settings, IaxGeneralSettingsView)

        SccpGeneralSettingsView.service = SccpGeneralSettingsService()
        SccpGeneralSettingsView.register(general_settings, route_base='/sccp_general_settings')
        register_flaskview(general_settings, SccpGeneralSettingsView)

        VoicemailGeneralSettingsView.service = VoicemailGeneralSettingsService()
        VoicemailGeneralSettingsView.register(general_settings, route_base='/voicemail_general_settings')
        register_flaskview(general_settings, VoicemailGeneralSettingsView)

        FeaturesGeneralSettingsView.service = FeaturesGeneralSettingsService()
        FeaturesGeneralSettingsView.register(general_settings, route_base='/features_general_settings')
        register_flaskview(general_settings, FeaturesGeneralSettingsView)

        core.register_blueprint(general_settings)
