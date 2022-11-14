from .model import CustomizedURL
from .db import Transaction
from flask import Blueprint, render_template, request, redirect, url_for, flash


web = Blueprint('web', __name__)


def is_existed(customized_url: str) -> bool:
    with Transaction() as session:
        return session.query(CustomizedURL) \
            .filter_by(custom_url=customized_url) \
            .first() is not None


@web.route('/', methods=['GET'])
def index():
    return render_template('main.html', base_url=request.base_url)


@web.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form.get('url')
    custom_url = request.form.get('custom_url')

    if not (original_url and custom_url):
        flash('Please enter both URL and custom URL', 'danger')
        return redirect(url_for('web.index'))

    with Transaction() as tx:
        if custom_url:
            is_existed = tx.query(CustomizedURL) \
                            .filter_by(custom_url=custom_url) \
                            .first() is not None
            if is_existed:
                flash('Custom URL already existed', 'danger')
                return redirect(url_for('web.index'))

    with Transaction() as tx:
        tx.add(CustomizedURL(original_url=original_url, custom_url=custom_url))

    flash('Your customized URL has been created', 'success')
    return redirect(url_for('web.index'))


@web.route('/<custom_url>', methods=['GET'])
def redirect_to_customized_url(custom_url):
    with Transaction() as tx:
        customized_url = tx.query(CustomizedURL) \
                .filter_by(custom_url=custom_url) \
                .first()

        if customized_url is None:
            flash('Custom URL not found', 'danger')
            return redirect(url_for('web.index'))

        return redirect(customized_url.original_url)
