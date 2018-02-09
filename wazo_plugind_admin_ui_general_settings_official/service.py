# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.confd import confd


class GeneralSettingsService(object):

    def get_sip_general(self):
        return confd.sip_general.get()

    def update_sip_general(self, sip_general):
        sip_general['ordered_options'] = self.get_sip_general()['ordered_options']
        confd.sip_general.update(sip_general)

    def get_iax_general(self):
        resource = confd.iax_general.get()
        resource['callnumberlimits'] = self.get_iax_callnumberlimits_general()['items']
        return resource

    def update_iax_general(self, iax_general):
        self.update_iax_callnumberlimits_general({'items': iax_general['callnumberlimits']})
        iax_general['ordered_options'] = self.get_iax_general()['ordered_options']
        confd.iax_general.update(iax_general)

    def get_iax_callnumberlimits_general(self):
        return confd.iax_callnumberlimits.get()

    def update_iax_callnumberlimits_general(self, iax_callnumberlimits):
        confd.iax_callnumberlimits.update(iax_callnumberlimits)

    def get_sccp_general(self):
        return confd.sccp_general.get()

    def update_sccp_general(self, sccp_general):
        confd.sccp_general.update(sccp_general)

    def get_voicemail_general(self):
        resource = confd.voicemail_general.get()
        resource['zonemessages'] = self.get_voicemail_zonemessages()['items']
        return resource

    def update_voicemail_general(self, voicemail_general):
        self.update_voicemail_zonemessages({'items': voicemail_general['zonemessages']})
        confd.voicemail_general.update(voicemail_general)

    def get_voicemail_zonemessages(self):
        return confd.voicemail_zonemessages.get()

    def update_voicemail_zonemessages(self, voicemail_zonemessages):
        confd.voicemail_zonemessages.update(voicemail_zonemessages)

    def get_features_general(self):
        resource = confd.features_general.get()
        resource['featuremap'] = self.get_features_featuremap_general()['options']
        resource['applicationmap'] = self.get_features_applicationmap_general()['options']
        return resource

    def update_features_general(self, features_general):
        self.update_features_featuremap_general({'options': features_general['featuremap']})
        self.update_features_applicationmap_general({'options': features_general['applicationmap']})
        confd.features_general.update(features_general)

    def get_features_featuremap_general(self):
        return confd.features_featuremap.get()

    def update_features_featuremap_general(self, features_featuremap):
        confd.features_featuremap.update(features_featuremap)

    def get_features_applicationmap_general(self):
        return confd.features_applicationmap.get()

    def update_features_applicationmap_general(self, features_applicationmap):
        confd.features_applicationmap.update(features_applicationmap)
