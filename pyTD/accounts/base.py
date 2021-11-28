# MIT License

# Copyright (c) 2018 Addison Lynch

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging

from pyTD.auth import auth_check
from pyTD.resource import Resource

logger = logging.getLogger(__name__)


class AccountsAndTrading(Resource):
    """
    Base class for retrieving accounts and orders information. This includes the
    following endpoint groups:
        - Orders
        - Saved Orders
        - Accounts

    Parameters
    ----------
    api: pyTD.api.api object, optional
        A pyTD api object. If not passed, API requestor defaults to
        pyTD.api.default_api
    """
    def __init__(self, api=None):
        super(AccountsAndTrading, self).__init__(api)

    @property
    def endpoint(self):
        return "accounts"

    @property
    def resource(self):
        return ''

    @property
    def url(self):
        return "%s%s/%s" % (self._BASE_URL, self.endpoint, self.resource)

    @auth_check
    def execute(self):
        out = self.get()
        return out
