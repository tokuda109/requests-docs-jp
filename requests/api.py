# -*- coding: utf-8 -*-

"""
requests.api
~~~~~~~~~~~~

This module implements the Requests API.

:copyright: (c) 2012 by Kenneth Reitz.
:license: Apache2, see LICENSE for more details.
"""

from . import sessions


def request(method, url, **kwargs):
    """
    .. Constructs and sends a :class:`Request <Request>`.

    :class:`Request <Request>` を生成し、送信します。

    .. :param method: method for the new :class:`Request` object.
    .. :param url: URL for the new :class:`Request` object.
    .. :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
    .. :param data: (optional) Dictionary or list of tuples ``[(key, value)]`` (will be form-encoded), bytes, or file-like object to send in the body of the :class:`Request`.
    .. :param json: (optional) json data to send in the body of the :class:`Request`.
    .. :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
    .. :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
    .. :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
    ..     ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
    ..     or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
    ..     defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
    ..     to add for the file.
    .. :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
    .. :param timeout: (optional) How many seconds to wait for the server to send data
    ..     before giving up, as a float, or a :ref:`(connect timeout, read
    ..     timeout) <timeouts>` tuple.
    .. :type timeout: float or tuple
    .. :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
    .. :type allow_redirects: bool
    .. :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
    .. :param verify: (optional) Either a boolean, in which case it controls whether we verify
    ..         the server's TLS certificate, or a string, in which case it must be a path
    ..         to a CA bundle to use. Defaults to ``True``.
    .. :param stream: (optional) if ``False``, the response content will be immediately downloaded.
    .. :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
    .. :return: :class:`Response <Response>` object
    .. :rtype: requests.Response

    :param method: 新しく作成した :class:`Request` オブジェクトの HTTP メソッド。
    :param url: 新しく作成した :class:`Request` オブジェクトのURL。
    :param params: (任意) :class:`Request` のクエリ文字列として送信されるディクショナリ、もしくはバイトデータ。
    :param data: (任意) :class:`Request` のボディとして送信するディクショナリ、
        もしくは(フォームエンコードされた) ``[(key, value)]`` 形式のタプルの一覧、バイトデータ、ファイル形式のオブジェクト。
    :param json: (任意) :class:`Request` のボディとして送信する JSON データ。
    :param headers: (任意) :class:`Request` と一緒に送信するための HTTP ヘッダーのディクショナリ。
    :param cookies: (任意) :class:`Request` と一緒に送信するためのディクショナリか CookieJar オブジェクト。
    :param files: (任意) マルチパートのエンコーディングアップロードのための ``'name': file-like-objects`` (もしくは、``{'name': file-tuple}``) のディクショナリ。
        ``file-tuple`` は、``('filename', fileobj)`` 形式、``('filename', fileobj, 'content_type')`` 形式、``('filename', fileobj, 'content_type', custom_headers)`` 形式にできます。
        ``'content-type'`` は指定されたファイルのコンテントタイプを定義する文字列で、``custom_headers`` はファイルに追加するヘッダーを含むディクショナリ形式のオブジェクトです。
    :param auth: (任意) Basic / Digest / 独自の HTTP 認証を有効にするためのタプル。
    :param timeout: (任意) サーバーからのデータ返却をどれくらい待つかを float か :ref:`(connect timeout, read timeout) <timeouts>` のタプルで指定します。
    :type timeout: float or tuple
    :param allow_redirects: (任意) ブーリアン。GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD のリダイレクトを有効/無効にします。デフォルトは ``True`` です。
    :type allow_redirects: bool
    :param proxies: (任意) プロキシへの URL にプロトコルをマッピングするためのディクショナリ。
    :param verify: (任意) ブーリアンの場合、サーバーの TLS 証明書を検証するか文字列を検証するかを制御します。
            この場合、使う認証局のバンドルへのパスでなければいけません。デフォルトは ``True`` 。
    :param stream: (任意) ``False`` の場合、レスポンスの内容はすぐにダウンロードが開始されます。
    :param cert: (任意) 文字列の場合は、SSL 証明書(.pem)へのパス。タプルの場合は、('cert', 'key') のペア。
    :return: :class:`Response <Response>` オブジェクト。
    :rtype: requests.Response

    .. Usage

    使い方::

      >>> import requests
      >>> req = requests.request('GET', 'http://httpbin.org/get')
      <Response [200]>
    """

    # By using the 'with' statement we are sure the session is closed, thus we
    # avoid leaving sockets open which can trigger a ResourceWarning in some
    # cases, and look like a memory leak in others.
    with sessions.Session() as session:
        return session.request(method=method, url=url, **kwargs)


def get(url, params=None, **kwargs):
    r"""
    .. Sends a GET request.

    GET リクエストを送信します。

    .. :param url: URL for the new :class:`Request` object.
    .. :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
    .. :param \*\*kwargs: Optional arguments that ``request`` takes.
    .. :return: :class:`Response <Response>` object
    .. :rtype: requests.Response

    :param url: 新しく作成した :class:`Request` オブジェクトのURL。
    :param params: (任意) :class:`Request` のクエリ文字列で送信されるディクショナリ、もしくはバイトデータ。
    :param \*\*kwargs: ``request`` が受け取る任意の引数。
    :return: :class:`Response <Response>` オブジェクト。
    :rtype: requests.Response
    """

    kwargs.setdefault('allow_redirects', True)
    return request('get', url, params=params, **kwargs)


def options(url, **kwargs):
    r"""Sends an OPTIONS request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    kwargs.setdefault('allow_redirects', True)
    return request('options', url, **kwargs)


def head(url, **kwargs):
    r"""
    .. Sends a HEAD request.

    HEAD リクエストを送信します。

    .. :param url: URL for the new :class:`Request` object.
    .. :param \*\*kwargs: Optional arguments that ``request`` takes.
    .. :return: :class:`Response <Response>` object
    .. :rtype: requests.Response

    :param url: 新しく作成した :class:`Request` オブジェクトのURL。
    :param \*\*kwargs: ``request`` が受け取る任意の引数。
    :return: :class:`Response <Response>` オブジェクト。
    :rtype: requests.Response
    """

    kwargs.setdefault('allow_redirects', False)
    return request('head', url, **kwargs)


def post(url, data=None, json=None, **kwargs):
    r"""
    .. Sends a POST request.

    POST リクエストを送信します。

    .. :param url: URL for the new :class:`Request` object.
    .. :param data: (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in the body of the :class:`Request`.
    .. :param json: (optional) json data to send in the body of the :class:`Request`.
    .. :param \*\*kwargs: Optional arguments that ``request`` takes.
    .. :return: :class:`Response <Response>` object
    .. :rtype: requests.Response

    :param url: 新しく作成した :class:`Request` オブジェクトのURL。
    :param data: (任意) :class:`Request` のボティで送信する(フォームエンコードされた)ディクショナリ、バイトデータ、ファイル形式のオブジェクト。
    :param json: (任意) :class:`Request` のボティで送信する JSON データ。
    :param \*\*kwargs: ``request`` が受け取る任意の引数。
    :return: :class:`Response <Response>` オブジェクト。
    :rtype: requests.Response
    """

    return request('post', url, data=data, json=json, **kwargs)


def put(url, data=None, **kwargs):
    r"""
    .. Sends a PUT request.

    PUT リクエストを送信します。

    .. :param url: URL for the new :class:`Request` object.
    .. :param data: (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in the body of the :class:`Request`.
    .. :param json: (optional) json data to send in the body of the :class:`Request`.
    .. :param \*\*kwargs: Optional arguments that ``request`` takes.
    .. :return: :class:`Response <Response>` object
    .. :rtype: requests.Response

    :param url: 新しく作成した :class:`Request` オブジェクトのURL。
    :param data: (任意) :class:`Request` のボティで送信する(フォームエンコードされた)ディクショナリ、バイトデータ、ファイル形式のオブジェクト。
    :param json: (任意) :class:`Request` のボティで送信する JSON データ。
    :param \*\*kwargs: ``request`` が受け取る任意の引数。
    :return: :class:`Response <Response>` オブジェクト。
    :rtype: requests.Response
    """

    return request('put', url, data=data, **kwargs)


def patch(url, data=None, **kwargs):
    r"""
    .. Sends a PATCH request.

    PATCH リクエストを送信します。

    .. :param url: URL for the new :class:`Request` object.
    .. :param data: (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in the body of the :class:`Request`.
    .. :param json: (optional) json data to send in the body of the :class:`Request`.
    .. :param \*\*kwargs: Optional arguments that ``request`` takes.
    .. :return: :class:`Response <Response>` object
    .. :rtype: requests.Response

    :param url: 新しく作成した :class:`Request` オブジェクトのURL。
    :param data: (任意) :class:`Request` のボティで送信する(フォームエンコードされた)ディクショナリ、バイトデータ、ファイル形式のオブジェクト。
    :param json: (任意) :class:`Request` のボティで送信する JSON データ。
    :param \*\*kwargs: ``request`` が受け取る任意の引数。
    :return: :class:`Response <Response>` オブジェクト。
    :rtype: requests.Response
    """

    return request('patch', url, data=data, **kwargs)


def delete(url, **kwargs):
    r"""
    .. Sends a DELETE request.

    DELETE リクエストを送信します。

    .. :param url: URL for the new :class:`Request` object.
    .. :param \*\*kwargs: Optional arguments that ``request`` takes.
    .. :return: :class:`Response <Response>` object
    .. :rtype: requests.Response

    :param url: 新しく作成した :class:`Request` オブジェクトのURL。
    :param \*\*kwargs: ``request`` が受け取る任意の引数。
    :return: :class:`Response <Response>` オブジェクト。
    :rtype: requests.Response
    """

    return request('delete', url, **kwargs)
