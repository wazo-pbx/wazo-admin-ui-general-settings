# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.plugin import create_blueprint

general_settings = create_blueprint('general_settings', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']

        core.register_blueprint(general_settings)
