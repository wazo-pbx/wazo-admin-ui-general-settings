# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.confd import confd


class SipGeneralSettingsService(object):

    def get(self):
        return confd.sip_general.get()

    def update(self, sip_general):
        sip_general['ordered_options'] = confd.sip_general.get()['ordered_options']
        confd.sip_general.update(sip_general)


class IaxGeneralSettingsService(object):

    def get(self):
        resource = confd.iax_general.get()
        resource['callnumberlimits'] = confd.iax_callnumberlimits.get()['items']
        return resource

    def update(self, iax_general):
        confd.iax_callnumberlimits.update({'items': iax_general['callnumberlimits']})
        iax_general['ordered_options'] = confd.iax_general.get()['ordered_options']
        confd.iax_general.update(iax_general)


class SccpGeneralSettingsService(object):

    def get(self):
        return confd.sccp_general.get()

    def update(self, sccp_general):
        confd.sccp_general.update(sccp_general)


class VoicemailGeneralSettingsService(object):

    def get(self):
        resource = confd.voicemail_general.get()
        resource['zonemessages'] = confd.voicemail_zonemessages.get()['items']
        return resource

    def update(self, voicemail_general):
        confd.voicemail_zonemessages.update({'items': voicemail_general['zonemessages']})
        confd.voicemail_general.update(voicemail_general)


class FeaturesGeneralSettingsService(object):

    def get(self):
        resource = confd.features_general.get()
        resource['featuremap'] = confd.features_featuremap.get()['options']
        resource['applicationmap'] = confd.features_applicationmap.get()['options']
        return resource

    def update(self, features_general):
        confd.features_featuremap.update({'options': features_general['featuremap']})
        confd.features_applicationmap.update({'options': features_general['applicationmap']})
        confd.features_general.update(features_general)
