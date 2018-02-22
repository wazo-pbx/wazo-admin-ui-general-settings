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
        resource = {
            'general': confd.iax_general.get(),
            'callnumberlimits': confd.iax_callnumberlimits.get()['items']
        }
        return resource

    def update(self, resource):
        confd.iax_callnumberlimits.update({'items': resource['callnumberlimits']})
        resource['general']['ordered_options'] = confd.iax_general.get()['ordered_options']
        confd.iax_general.update(resource['general'])


class SccpGeneralSettingsService(object):

    def get(self):
        return confd.sccp_general.get()

    def update(self, sccp_general):
        confd.sccp_general.update(sccp_general)


class VoicemailGeneralSettingsService(object):

    def get(self):
        resource = {
            'general': confd.voicemail_general.get(),
            'zonemessages': confd.voicemail_zonemessages.get()['items']
        }
        return resource

    def update(self, resource):
        confd.voicemail_zonemessages.update({'items': resource['zonemessages']})
        confd.voicemail_general.update(resource['general'])


class FeaturesGeneralSettingsService(object):

    def get(self):
        resource = {
            'general': confd.features_general.get(),
            'featuremap': confd.features_featuremap.get(),
            'applicationmap': confd.features_applicationmap.get()
        }
        return resource

    def update(self, resource):
        confd.features_featuremap.update(resource['featuremap'])
        confd.features_applicationmap.update(resource['applicationmap'])
        confd.features_general.update(resource['general'])


class ConfBridgeGeneralSettingsService(object):

    def get(self):
        resource = {
            'wazo_default_user': confd.confbridge_wazo_default_user.get(),
            'wazo_default_bridge': confd.confbridge_wazo_default_bridge.get()
        }
        return resource

    def update(self, resource):
        confd.confbridge_wazo_default_user.update(resource['wazo_default_user'])
        confd.confbridge_wazo_default_bridge.update(resource['wazo_default_bridge'])
