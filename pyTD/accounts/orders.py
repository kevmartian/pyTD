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


class Orders(AccountsAndTrading):
    """
    Class for retrieving and posting data via the Orders endpoint.

    Parameters
    ----------
    account_num: account number, required
        Account number used for the order
    api: pyTD.api.api object, optional
        A pyTD api object. If not passed, API requestor defaults to
        pyTD.api.default_api
    """

    def __init__(self, **kwargs):
        self.method = kwargs.pop("method")
        self.account_num = kwargs.pop("account_num", "")
        self.duration = kwargs.pop("duration", "GOOD_TILL_CANCEL")
        self.order_type = kwargs.pop("order_type", "LIMIT")
        self.quantity = kwargs.pop("quantity", '') # appears this should not be string
        self.order_strategy_type = kwargs.pop("order_strategy_type", "SINGLE")
        self.session = kwargs.pop("session", "SEAMLESS")
        self.price = kwargs.pop("price", '')
        self.instruction = kwargs.pop("instruction", '')
        self.symbol = kwargs.pop("symbol", '')
        self.asset_type = kwargs.pop("asset_type", '')
        self.complex_order_strategy_type = kwargs.pop("complex_ord_strat_type", "NONE")
        self.exist_order_num = kwargs.pop("exist_order_num", "")

        self.opt = kwargs
        api = kwargs.get("api")
        super(AccountsAndTrading, self).__init__(api)


    @property
    def params(self):
        # if this doesn't work, try sending json instead or as data param
        p = {
            "complexOrderStrategyType": self.complex_order_strategy_type,
            "orderType": self.order_type,
            "session": self.session,
            "price": str(self.price),
            "duration": self.duration,
            "orderStrategyType": self.order_strategy_type,
            "orderLegCollection": [
                {
                    "instruction": self.instruction,
                    "quantity": self.quantity,
                    "instrument": {
                        "symbol": self.symbol,
                        "assetType": self.asset_type
                    }
                }
            ]
            }
        # clear out keys with empty values
        pars = {k: v for k, v in p.items() if v is not None}
        return pars

    @property
    def resource(self):
        return self.exist_order_num

    @property
    def url(self):
        if self.resource:
            return "%s%s/{}/orders/%s" % (self._BASE_URL, self.endpoint, self.resource)
        else:
            return "%s%s/{}/orders" % (self._BASE_URL, self.endpoint)

    @auth_check
    def execute(self):
        # TODO: add in this URL accordingly
        if self.method == "GET":
            return self.get(url=self.url.format(self.account_num))
        if self.method == "POST":
            return self.post(url=self.url.format(self.account_num))
        if self.method == "PUT":
            return self.put(url=self.url.format(self.account_num))
        if self.method == "DELETE":
            return self.delete(url=self.url.format(self.account_num))
