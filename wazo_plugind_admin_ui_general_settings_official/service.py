# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.confd import confd


class GeneralSettingsService(object):

    def get_sip_general(self):
        return confd.sip_general.get()

    def update_sip_general(self, sip_general):
        sip_general['ordered_options'] = self.get_sip_general()['ordered_options']
        return confd.sip_general.update(sip_general)