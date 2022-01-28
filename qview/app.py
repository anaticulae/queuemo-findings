# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask
import flask_bootstrap

import qview.config
from qview.api.findings import *  # pylint:disable=W0401
from qview.view.findings import findings_
from qview.view.welcome import welcome_


def create_application() -> flask.Flask:
    """Setup flask application

    1. Set template and static folder
    2. Configure application
    3. Setup global env
    4. Register blueprint for routing the user requests
    """
    # Flask determines template- and static-folder automatically.
    appi = flask.Flask(__name__)
    appi.secret_key = qview.config.SECRET_KEY

    appi.config.setdefault('BOOTSTRAP_SERVE_LOCAL', True)
    flask_bootstrap.Bootstrap(app=appi)

    # views
    appi.register_blueprint(welcome_)
    appi.register_blueprint(findings_)

    # data
    appi.register_blueprint(api_findings, url_prefix=qview.config.API_PREFIX)

    return appi
