# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.confd import confd


class GeneralSettingsService(object):

    def get_sip_general(self):
        return confd.sip_general.get()

    def update_sip_general(self, sip_general):
        sip_general['ordered_options'] = self.get_sip_general()['ordered_options']
        return confd.sip_general.update(sip_general)

    def get_iax_general(self):
        return confd.iax_general.get()

    def update_iax_general(self, iax_general):
        iax_general['ordered_options'] = self.get_iax_general()['ordered_options']
        return confd.iax_general.update(iax_general)

    def get_sccp_general(self):
        return confd.sccp_general.get()

    def update_sccp_general(self, sccp_general):
        return confd.sccp_general.update(sccp_general)

    def get_voicemail_general(self):
        return confd.voicemail_general.get()

    def update_voicemail_general(self, voicemail_general):
        return confd.voicemail_general.update(voicemail_general)
