#
# spec file for package hello
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           hello
Version:        2.10
Release:        1
Summary:        The "Hello World" program from GNU
License:        WTFPL
Group:          toys
URL:            https://www.gnu.org/software/hello/
Source0:        https://ftp.gnu.org/gnu/hello/hello-%{version}.tar.gz

%description
The "Hello World" program, done with all bells and whistles of a proper FOSS
project, including configuration, build, internationalization, help files, etc.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
/usr/bin/hello
/usr/share/info/*
/usr/share/man/man1/hello.1.gz
%lang(bg) /usr/share/locale/bg/LC_MESSAGES/hello.mo
%lang(ca) /usr/share/locale/ca/LC_MESSAGES/hello.mo
%lang(da) /usr/share/locale/da/LC_MESSAGES/hello.mo
%lang(de) /usr/share/locale/de/LC_MESSAGES/hello.mo
%lang(el) /usr/share/locale/el/LC_MESSAGES/hello.mo
%lang(eo) /usr/share/locale/eo/LC_MESSAGES/hello.mo
%lang(es) /usr/share/locale/es/LC_MESSAGES/hello.mo
%lang(et) /usr/share/locale/et/LC_MESSAGES/hello.mo
%lang(eu) /usr/share/locale/eu/LC_MESSAGES/hello.mo
%lang(fa) /usr/share/locale/fa/LC_MESSAGES/hello.mo
%lang(fi) /usr/share/locale/fi/LC_MESSAGES/hello.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/hello.mo
%lang(ga) /usr/share/locale/ga/LC_MESSAGES/hello.mo
%lang(gl) /usr/share/locale/gl/LC_MESSAGES/hello.mo
%lang(he) /usr/share/locale/he/LC_MESSAGES/hello.mo
%lang(hr) /usr/share/locale/hr/LC_MESSAGES/hello.mo
%lang(hu) /usr/share/locale/hu/LC_MESSAGES/hello.mo
%lang(id) /usr/share/locale/id/LC_MESSAGES/hello.mo
%lang(it) /usr/share/locale/it/LC_MESSAGES/hello.mo
%lang(ja) /usr/share/locale/ja/LC_MESSAGES/hello.mo
%lang(ka) /usr/share/locale/ka/LC_MESSAGES/hello.mo
%lang(ko) /usr/share/locale/ko/LC_MESSAGES/hello.mo
%lang(lv) /usr/share/locale/lv/LC_MESSAGES/hello.mo
%lang(ms) /usr/share/locale/ms/LC_MESSAGES/hello.mo
%lang(nb) /usr/share/locale/nb/LC_MESSAGES/hello.mo
%lang(nl) /usr/share/locale/nl/LC_MESSAGES/hello.mo
%lang(nn) /usr/share/locale/nn/LC_MESSAGES/hello.mo
%lang(pl) /usr/share/locale/pl/LC_MESSAGES/hello.mo
%lang(pt) /usr/share/locale/pt/LC_MESSAGES/hello.mo
%lang(pt_BR) /usr/share/locale/pt_BR/LC_MESSAGES/hello.mo
%lang(ro) /usr/share/locale/ro/LC_MESSAGES/hello.mo
%lang(ru) /usr/share/locale/ru/LC_MESSAGES/hello.mo
%lang(sk) /usr/share/locale/sk/LC_MESSAGES/hello.mo
%lang(sl) /usr/share/locale/sl/LC_MESSAGES/hello.mo
%lang(sr) /usr/share/locale/sr/LC_MESSAGES/hello.mo
%lang(sv) /usr/share/locale/sv/LC_MESSAGES/hello.mo
%lang(th) /usr/share/locale/th/LC_MESSAGES/hello.mo
%lang(tr) /usr/share/locale/tr/LC_MESSAGES/hello.mo
%lang(uk) /usr/share/locale/uk/LC_MESSAGES/hello.mo
%lang(vi) /usr/share/locale/vi/LC_MESSAGES/hello.mo
%lang(zh_CN) /usr/share/locale/zh_CN/LC_MESSAGES/hello.mo
%lang(zh_TW) /usr/share/locale/zh_TW/LC_MESSAGES/hello.mo


%changelog
* Thu Jul 07 2011 The Coon of Ty <Ty@coon.org> - 2.10-1
- Initial version of the package
