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


class Watchlists(AccountsAndTrading):
    """
    Class for retrieving and posting data via the Watchlists endpoint.

    Parameters
    ----------
    account_num: account number, optional
        Account number used for the watchlist
    api: pyTD.api.api object, optional
        A pyTD api object. If not passed, API requestor defaults to
        pyTD.api.default_api
    updated_list: list(WatchlistItem), optional
        list of watchlistitems, if adding a list
    """

    def __init__(self, **kwargs):
        self.method = kwargs.pop("method")
        self.account_num = kwargs.pop("account_num", None)
        self.watchlist_id = kwargs.pop("watchlist_id", None)
        self.updated_list = kwargs.pop("updated_list", None)

        self.opt = kwargs
        api = kwargs.get("api")
        super(AccountsAndTrading, self).__init__(api)

    @property
    def params(self):
        # if this doesn't work, try sending json instead or as data param
        p = {
            "name": self.watchlist_id,
            "watchlistItems": self.updated_list,
            }
        # clear out keys with empty values
        pars = {k: v for k, v in p.items() if v is not None}
        return pars

    def set_list_from_strings(self, new_symbols, asset_type):
        new_list = []
        for symbol in new_symbols:
            w = WatchlistItem(instrument=(symbol, asset_type))
            new_list.append(w.get_dict())
        self.updated_list = new_list

    @property
    def resource(self):
        return "watchlists"

    @property
    def url(self):
        if self.method == "POST":
            return "%s%s/%s/%s" % (self._BASE_URL, self.endpoint, self.account_num, self.resource)
        else:
            if self.watchlist_id:
                return "%s%s/%s/%s/%s" % (self._BASE_URL, self.endpoint, self.account_num, self.resource, self.watchlist_id)
            elif self.account_num:
                return "%s%s/%s/%s" % (self._BASE_URL, self.endpoint, self.account_num, self.resource)
            else:
                return "%s%s/%s" % (self._BASE_URL, self.endpoint, self.resource)


    @auth_check
    def execute(self):
        # TODO: add in this URL accordingly
        if self.method == "GET":
            return self.get(url=self.url)
        # if self.method == "POST":
        #     return self.post(url=self.url.format(self.account_num))
        if self.method == "PUT":
            return self.put(url=self.url)
        if self.method == "DELETE":
            return self.delete(url=self.url)


class WatchlistItem:
    """
    Class for storing a watchlist item.

    Parameters
    ----------
    quantity: int, optional
        quantity of shares, defaults to 0
    average_price: float, optional
        average price of purchase, defaults to 0
    commission: float, optional
        price of commission, defaults to 0
    purchased_date: datetime object, optional
        date of purchase, defaults to DateParam\"
    instrument: tuple
        tuple of symbol and asset type. see below for types (symbol, asset type)
        assetType": "'EQUITY' or 'OPTION' or 'MUTUAL_FUND' or 'FIXED_INCOME' or 'INDEX'"
    """

    def __init__(self, **kwargs):
        self.quantity = kwargs.pop("quantity", 0)
        self.average_price = kwargs.pop("average_price", 0)
        self.commission = kwargs.pop("commission", 0)
        self.purchased_date = kwargs.pop("purchased_date", "DateParam\"")
        self.instrument = kwargs.pop("instrument")

    @property
    def quantity(self):
        return self.quantity

    @property
    def average_price(self):
        return self.average_price

    @property
    def commission(self):
        return self.commission

    @property
    def purchased_date(self):
        return self.purchased_date

    @property
    def instrument(self):
        return self.instrument

    def get_dict(self):
        return {
            "quantity": self.quantity,
            "averagePrice": self.average_price,
            "commission": self.commission,
            "purchasedDate": self.purchased_date,
            "instrument": {
                "symbol": self.instrument[0],
                "assetType": self.instrument[1]
            }
        }
