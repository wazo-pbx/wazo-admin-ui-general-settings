# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_babel import lazy_gettext as l_
from wtforms.fields import (
    FieldList,
    FormField,
    SelectField,
    StringField,
    SubmitField
)
from wtforms.validators import InputRequired

from wazo_admin_ui.helpers.form import BaseForm


class OptionsForm(BaseForm):

    def to_dict(self):
        return super().to_dict(empty_string=True)

    option_key = StringField(validators=[InputRequired()])
    option_value = StringField()


class GeneralSettingsOptionsForm(BaseForm):
    options = FieldList(FormField(OptionsForm))
    submit = SubmitField(l_('Submit'))


class SipGeneralSettingsForm(GeneralSettingsOptionsForm):
    pass


class IaxGeneralSettingsForm(GeneralSettingsOptionsForm):
    pass


class SccpGeneralSettingsForm(GeneralSettingsOptionsForm):
    pass


class VoicemailZonemessages(BaseForm):
    name = StringField(l_('Name'))
    timezone = SelectField('Timezone',
                           validators=[InputRequired()],
                           choices=[
                               ('America/St_Johns', 'America/St_Johns'),
                               ('America/Halifax', 'America/Halifax'),
                               ('America/New_York', 'America/New_York'),
                               ('America/Chicago', 'America/Chicago'),
                               ('America/Denver', 'America/Denver'),
                               ('America/Los_Angeles', 'America/Los_Angeles'),
                               ('America/Anchorage', 'America/Anchorage'),
                               ('Europe/Paris', 'Europe/Paris')
                           ])
    message = StringField(l_('Message'))


class VoicemailGeneralSettingsForm(GeneralSettingsOptionsForm):
    zonemessages = FieldList(FormField(VoicemailZonemessages))
