from flask import Blueprint

blueprint = Blueprint('account', __name__)


@blueprint.route('%s/' % __name__)
def index():
    return "Accounts!"


@blueprint.route('%s/login' % __name__)
def about():
    return "Login!"
