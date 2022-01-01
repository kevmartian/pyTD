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

from pyTD.instruments.base import Instruments
from pyTD.accounts.accounts import Accounts
from pyTD.accounts.orders import Orders
from pyTD.accounts.watchlists import Watchlists


def get_accounts(*args, **kwargs):
    """
    Function to retrieve account information from the Get Accounts endpoint

    Parameters
    ----------
    account_num: account number, optional
        Account number to retrieve. If not specified, all accounts will be returned
    api: pyTD.api.api object, optional
        A pyTD api object. If not passed, API requestor defaults to
        pyTD.api.default_api
    """
    return Accounts(*args, **kwargs).execute()


def send_order(*args, **kwargs):
    return Orders(*args, **kwargs).execute()


def get_open_orders(account_num, *args, **kwargs):
    return Accounts(account_num=account_num, resource='orders', *args, **kwargs).execute()


def get_watchlist(account_num, watchlist_id, *args, **kwargs):
    return Watchlists(account_num=account_num, watchlist_id=watchlist_id, method="GET", *args, **kwargs).execute()


def get_watchlists(account_num=None, *args, **kwargs):
    return Watchlists(account_num=account_num, method="GET", *args, **kwargs).execute()


def create_watchlist(account_num, symbols, asset_type):
    new_wl = Watchlists(account_num=account_num, method="SET", *args, **kwargs).execute()
    new_wl.set_list_from_strings(symbols, asset_type)
    return new_wl.execute()

# def get_watchlist(account_num, list_id, *args, **kwargs):
