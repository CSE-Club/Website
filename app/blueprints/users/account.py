from flask import Blueprint

blueprint = Blueprint('account', __name__)


@blueprint.route('/account/')
def index():
    return "Accounts!"


@blueprint.route('/account/login')
def about():
    return "Login!"
