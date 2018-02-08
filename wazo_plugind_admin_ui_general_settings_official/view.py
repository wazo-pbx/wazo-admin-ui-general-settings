# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_babel import gettext as _
from flask_babel import lazy_gettext as l_
from flask import (
    redirect,
    render_template,
    url_for,
    flash
)
from flask_classful import route
from flask_menu.classy import classy_menu_item
from requests.exceptions import HTTPError

from wazo_admin_ui.helpers.classful import BaseView, flash_basic_form_errors

from .form import (
    SipGeneralSettingsForm,
    IaxGeneralSettingsForm,
    SccpGeneralSettingsForm,
    VoicemailGeneralSettingsForm,
    FeaturesGeneralSettingsForm
)


class BaseGeneralSettingsView(BaseView):
    settings = None

    def index(self, form=None):
        try:
            resource = getattr(self.service, 'get_{}'.format(self.settings))()
        except HTTPError as error:
            self._flash_http_error(error)
            return redirect(url_for('admin.Admin:get'))

        form = form or self._map_resources_to_form(resource)
        form = self._populate_form(form)

        return render_template(self._get_template(self.settings),
                               form=form)

    @route('/put', methods=['POST'])
    def put(self):
        form = self.form()
        if not form.csrf_token.validate(form):
            flash_basic_form_errors(form)
            return self.index(form)

        resources = self._map_form_to_resources(form)
        try:
            update_func = getattr(self.service, 'update_{}'.format(self.settings))
            update_func(resources)
        except HTTPError as error:
            form = self._fill_form_error(form, error)
            self._flash_http_error(error)
            return self.index(form)

        flash(_('%(resource)s: Resource has been updated', resource=self.resource), 'success')
        return self._redirect_for('index')

    def _map_resources_to_form(self, resource):
        resource['options'] = self._build_options(resource['options'])
        form = self.form(data=resource)
        return form

    def _build_options(self, options):
        return [{'option_key': option_key, 'option_value': option_value} for option_key, option_value in
                options.items()]

    def _map_form_to_resources(self, form, form_id=None):
        data = form.to_dict()
        data['options'] = self._map_options_to_resource(data['options'])
        return data

    def _map_options_to_resource(self, options):
        return {option['option_key']: option['option_value'] for option in options}


class SipGeneralSettingsView(BaseGeneralSettingsView):
    form = SipGeneralSettingsForm
    resource = 'sip_general_settings'
    settings = 'sip_general'

    @classy_menu_item('.advanced.sip_general_settings', l_('SIP General Settings'), order=4, icon="asterisk")
    def index(self, form=None):
        return super().index(form)


class IaxGeneralSettingsView(BaseGeneralSettingsView):
    form = IaxGeneralSettingsForm
    resource = 'iax_general_settings'
    settings = 'iax_general'

    @classy_menu_item('.advanced.iax_general_settings', l_('IAX General Settings'), order=5, icon="asterisk")
    def index(self, form=None):
        return super().index(form)


class SccpGeneralSettingsView(BaseGeneralSettingsView):
    form = SccpGeneralSettingsForm
    resource = 'sccp_general_settings'
    settings = 'sccp_general'

    @classy_menu_item('.advanced.sccp_general_settings', l_('SCCP General Settings'), order=6, icon="asterisk")
    def index(self, form=None):
        return super().index(form)


class VoicemailGeneralSettingsView(BaseGeneralSettingsView):
    form = VoicemailGeneralSettingsForm
    resource = 'voicemail_general_settings'
    settings = 'voicemail_general'

    @classy_menu_item('.advanced.voicemail_general_settings', l_('Voicemail General Settings'), order=7,
                      icon="asterisk")
    def index(self, form=None):
        return super().index(form)


class FeaturesGeneralSettingsView(BaseGeneralSettingsView):
    form = FeaturesGeneralSettingsForm
    resource = 'features_general_settings'
    settings = 'features_general'

    @classy_menu_item('.advanced.features_general_settings', l_('Features General Settings'), order=8, icon="asterisk")
    def index(self, form=None):
        return super().index(form)

    def _map_resources_to_form(self, resource):
        resource['options'] = self._build_options(resource['options'])
        resource['featuremap'] = self._build_options(resource['featuremap'])
        form = self.form(data=resource)
        return form

    def _map_form_to_resources(self, form, form_id=None):
        data = form.to_dict()
        data['options'] = self._map_options_to_resource(data['options'])
        data['featuremap'] = self._map_options_to_resource(data['featuremap'])
        return data
