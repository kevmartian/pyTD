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


from pyTD.auth import auth_check
from pyTD.accounts.base import AccountsAndTrading
from pyTD.utils.exceptions import ResourceNotFound


class Accounts(AccountsAndTrading):
    """
    Class for retrieving data from the Get Account endpoint. Defaults to
    retrieve all account balances

    Parameters
    ----------
    account_num: account number, optional
        Account number to retrieve. If not specified, all accounts will be returned
    api: pyTD.api.api object, optional
        A pyTD api object. If not passed, API requestor defaults to
        pyTD.api.default_api
    """

    def __init__(self, **kwargs):
        self.account_num = kwargs.pop("account_num", "")
        # TODO: Make this work on a specific account
        self.opt = kwargs
        api = kwargs.get("api")
        super(Accounts, self).__init__(api)

    """
    @property
    def params(self):
        p = {
            "periodType": self.period_type,
            "period": self.period,
            "frequencyType": self.frequency_type,
            "frequency": self.frequency,
            "startDate": self.start,
            "endDate": self.end,
            "needExtendedHoursData": self.need_extended
            }
        return p
    """

    @property
    def resource(self):
        return ''

    @property
    def url(self):
        return "%s%s/{}/%s" % (self._BASE_URL, self.endpoint, self.resource)

    @auth_check
    def execute(self):
        return self.get(url=self.url.format(self.account_num))
