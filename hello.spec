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
License:        GPLv3+
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          development
URL:      https://www.gnu.org/software/hello/
Source0:  https://ftp.gnu.org/gnu/hello/hello-%{version}.tar.gz
#BuildRequires:  
#BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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

%post
%postun

%files
%defattr(-,root,root)
/usr/bin/hello
/usr/lib/debug/usr/bin/hello-2.10-1.x86_64.debug
/usr/share/info/hello.info.gz
/usr/share/locale/bg/LC_MESSAGES/hello.mo
/usr/share/locale/ca/LC_MESSAGES/hello.mo
/usr/share/locale/da/LC_MESSAGES/hello.mo
/usr/share/locale/de/LC_MESSAGES/hello.mo
/usr/share/locale/el/LC_MESSAGES/hello.mo
/usr/share/locale/eo/LC_MESSAGES/hello.mo
/usr/share/locale/es/LC_MESSAGES/hello.mo
/usr/share/locale/et/LC_MESSAGES/hello.mo
/usr/share/locale/eu/LC_MESSAGES/hello.mo
/usr/share/locale/fa/LC_MESSAGES/hello.mo
/usr/share/locale/fi/LC_MESSAGES/hello.mo
/usr/share/locale/fr/LC_MESSAGES/hello.mo
/usr/share/locale/ga/LC_MESSAGES/hello.mo
/usr/share/locale/gl/LC_MESSAGES/hello.mo
/usr/share/locale/he/LC_MESSAGES/hello.mo
/usr/share/locale/hr/LC_MESSAGES/hello.mo
/usr/share/locale/hu/LC_MESSAGES/hello.mo
/usr/share/locale/id/LC_MESSAGES/hello.mo
/usr/share/locale/it/LC_MESSAGES/hello.mo
/usr/share/locale/ja/LC_MESSAGES/hello.mo
/usr/share/locale/ka/LC_MESSAGES/hello.mo
/usr/share/locale/ko/LC_MESSAGES/hello.mo
/usr/share/locale/lv/LC_MESSAGES/hello.mo
/usr/share/locale/ms/LC_MESSAGES/hello.mo
/usr/share/locale/nb/LC_MESSAGES/hello.mo
/usr/share/locale/nl/LC_MESSAGES/hello.mo
/usr/share/locale/nn/LC_MESSAGES/hello.mo
/usr/share/locale/pl/LC_MESSAGES/hello.mo
/usr/share/locale/pt/LC_MESSAGES/hello.mo
/usr/share/locale/pt_BR/LC_MESSAGES/hello.mo
/usr/share/locale/ro/LC_MESSAGES/hello.mo
/usr/share/locale/ru/LC_MESSAGES/hello.mo
/usr/share/locale/sk/LC_MESSAGES/hello.mo
/usr/share/locale/sl/LC_MESSAGES/hello.mo
/usr/share/locale/sr/LC_MESSAGES/hello.mo
/usr/share/locale/sv/LC_MESSAGES/hello.mo
/usr/share/locale/th/LC_MESSAGES/hello.mo
/usr/share/locale/tr/LC_MESSAGES/hello.mo
/usr/share/locale/uk/LC_MESSAGES/hello.mo
/usr/share/locale/vi/LC_MESSAGES/hello.mo
/usr/share/locale/zh_CN/LC_MESSAGES/hello.mo
/usr/share/locale/zh_TW/LC_MESSAGES/hello.mo
/usr/share/man/man1/hello.1.gz

%changelog
* Thu Jul 07 2011 The Coon of Ty <Ty@coon.org> - 2.10-1
- Initial version of the package
