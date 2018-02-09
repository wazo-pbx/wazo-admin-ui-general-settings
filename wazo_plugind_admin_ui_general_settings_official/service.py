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
        resource = confd.voicemail_general.get()
        resource['zonemessages'] = self.get_voicemail_zonemessages()['items']
        return resource

    def update_voicemail_general(self, voicemail_general):
        self.update_voicemail_zonemessages({'items': voicemail_general['zonemessages']})
        return confd.voicemail_general.update(voicemail_general)

    def get_voicemail_zonemessages(self):
        return confd.voicemail_zonemessages.get()

    def update_voicemail_zonemessages(self, voicemail_zonemessages):
        return confd.voicemail_zonemessages.update(voicemail_zonemessages)

    def get_features_general(self):
        resource = confd.features_general.get()
        resource['featuremap'] = self.get_features_featuremap_general()['options']
        resource['applicationmap'] = self.get_features_applicationmap_general()['options']
        return resource

    def update_features_general(self, features_general):
        self.update_features_featuremap_general({'options': features_general['featuremap']})
        self.update_features_applicationmap_general({'options': features_general['applicationmap']})
        return confd.features_general.update(features_general)

    def get_features_featuremap_general(self):
        return confd.features_featuremap.get()

    def update_features_featuremap_general(self, features_featuremap):
        return confd.features_featuremap.update(features_featuremap)

    def get_features_applicationmap_general(self):
        return confd.features_applicationmap.get()

    def update_features_applicationmap_general(self, features_applicationmap):
        return confd.features_applicationmap.update(features_applicationmap)
