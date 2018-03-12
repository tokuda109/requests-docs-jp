.. Release Process and Rules
   =========================

リリースプロセスとルール
============================

.. versionadded:: v2.6.2

.. Starting with the version to be released after ``v2.6.2``, the following rules
   will govern and describe how the Requests core team produces a new release.

``v2.6.2`` 以降にリリースされるバージョンから開始されたこととして、
Requests のコアチームが新しいリリースをどのように進めていくかを定め、説明することになりました。

.. Major Releases
   --------------

メジャーリリース
------------------------

.. A major release will include breaking changes. When it is versioned, it will
   be versioned as ``vX.0.0``. For example, if the previous release was
   ``v10.2.7`` the next version will be ``v11.0.0``.

メジャーリリースには、互換性を壊す変更が含まれることがあります。
バージョンが変更されると、``vX.0.0`` のようなバージョンになります。
例えば、1つ前のリリースが ``v10.2.7`` の場合、次のバージョンは ``v11.0.0`` になります。

.. Breaking changes are changes that break backwards compatibility with prior
   versions. If the project were to change the ``text`` attribute on a
   ``Response`` object to a method, that would only happen in a Major release.

互換性を壊す変更は、以前のバージョンとの後方互換性を損なう変更になります。
プロジェクトが ``Response`` オブジェクトのテキスト属性をメソッドに変更するような変更は、メジャーリリースでのみ行われます。

.. Major releases may also include miscellaneous bug fixes and upgrades to
   vendored packages. The core developers of Requests are committed to providing
   a good user experience. This means we're also committed to preserving
   backwards compatibility as much as possible. Major releases will be infrequent
   and will need strong justifications before they are considered.

メジャーリリースには諸々のバグ修正やベンダーパッケージのアップグレードなども含まれます。
Requests のコア開発者は、優れたユーザーエクスペリエンスを提供することに重きを置いています。
つまり、可能な限り後方互換性を維持することにも取り組んでいることを意味しています。
メジャーリリースはまれであり、後方互換性が考慮される以前に強い正当性が必要となります。

.. Minor Releases
   --------------

マイナーリリース
-------------------------

.. A minor release will not include breaking changes but may include
   miscellaneous bug fixes and upgrades to vendored packages. If the previous
   version of Requests released was ``v10.2.7`` a minor release would be
   versioned as ``v10.3.0``.

マイナーリリースには互換性を壊す変更は含まれませんが、諸々のバグ修正やベンダーパッケージのアップグレードなどが含まれます。
Requests の1つ前にリリースされたバージョンが ``v10.2.7`` だった場合、マイナーリリースは ``v10.3.0`` になります。

.. Minor releases will be backwards compatible with releases that have the same
   major version number. In other words, all versions that would start with
   ``v10.`` should be compatible with each other.

マイナーリリースは、メジャーバージョンの番号が同じリリースと後方互換性があります。
言い換えると、``v10.`` で始まる全てのバージョンは、それぞれ互換性があるはずです。

.. Hotfix Releases
   ---------------

ホットフィックスリリース
---------------------------

.. A hotfix release will only include bug fixes that were missed when the project
   released the previous version. If the previous version of Requests released
   ``v10.2.7`` the hotfix release would be versioned as ``v10.2.8``.

ホットフィックスリリースには、以前のバージョンをリリースした時に見逃したバグ修正のみ含まれます。
Requests の1つ前にリリースされたバージョンが ``v10.2.7`` だった場合、ホットフィックスリリースは ``v10.2.8`` になります。

.. Hotfixes will **not** include upgrades to vendored dependencies after
   ``v2.6.2``

修正されたものには ``v2.6.2`` 以降の依存しているベンダーパッケージのアップグレードは含まれていません。

.. Reasoning
   ---------

プロセスとルールを定める理由
------------------------------------

.. In the 2.5 and 2.6 release series, the Requests core team upgraded vendored
   dependencies and caused a great deal of headaches for both users and the core
   team. To reduce this pain, we're forming a concrete set of procedures so
   expectations will be properly set.

バージョン 2.5 と 2.6 のリリースでは、Requests のコアチームはベンダーの依存を変更し、
ユーザーとコアチームの両方に迷惑をかけました。
このようなことが極力起こらないようにするために、期待されていることを具体的な一連の流れとして設定することにしました。
