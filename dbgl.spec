#
# spec file for package dbgl
#
# Copyright (c) 2020 UnitedRPMs.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://goo.gl/zqFJft
#

%global debug_package %{nil}

Name:           dbgl
Summary:        DOSBox Game Launcher
URL:            http://home.quicknet.nl/qn/prive/blankendaalr/dbgl/
Version:        0.92
%global         uversion  %(foo=%{version}; echo ${foo//./})
Release:        1%{?dist}
License:        GPLv2
BuildRequires:  libappstream-glib

Requires:       dosbox >= 0.70
Requires:       eclipse-swt
Recommends:     hsqldb1
Requires:       java >= 1:1.8.0
Requires:       java-headless >= 1:1.8.0
Requires:       jpackage-utils
Requires:       SDL_net
Requires:       SDL_sound
Source0:        http://members.quicknet.nl/blankendaalr/dbgl/download/%{name}%{uversion}.tar.gz
Source1:        dbgl.desktop
Source2:        dbgl.appdata.xml
Source3:        dbgl	

%description
DBGL is a Java front-end for DOSBox, based largely upon the proven
interface of D-Fend.
The front-end is by no means finished. It is a work in progress
and lacking many features, but the core is working, and I think
the product is somewhat usable as it is. Please bear in mind that
the interface is still quite rough around the edges.

%prep
%setup -qc


%build
# Nothing here

%install

  install -dm755 %{buildroot}/usr/share/java/%{name}
  install -m755 dbgl %{buildroot}/usr/share/java/%{name}
  install -m644 dbgl.jar \
    dbgl.png \
    %{buildroot}/usr/share/java/%{name}

  for dir in captures db dosroot export lib profiles templates xsl; do
    mv "$dir" %{buildroot}/usr/share/java/%{name}/
  done

  install -dm755 %{buildroot}/usr/bin
  install -m755 %{S:3} %{buildroot}/usr/bin/dbgl

  install -dm755 %{buildroot}/usr/share/icons/hicolor/256x256/apps
  install -m644 dbgl.png %{buildroot}/usr/share/icons/hicolor/256x256/apps

  install -dm755 %{buildroot}/usr/share/applications
  install -m644 %{S:1} %{buildroot}/usr/share/applications

  install -D -p -m 0644 %{S:2} \
    %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%check
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%{_bindir}/%{name}
%{_javadir}/%{name}/
%{_datadir}/icons/hicolor/256x256/apps/dbgl.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml

%changelog

* Sat Dec 26 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.92-1
- Updated to 0.92

* Sun Feb 09 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.91-1
- Updated to 0.91

* Wed Dec 25 2019 Sérgio Basto <sergio@serjux.com> - 0.90-1
- Update to 0.90

* Sun Nov 05 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.82-1
- Updated to 0.82

* Thu Mar 09 2017 Sérgio Basto <sergio@serjux.com> - 0.81-1
- Update to 0.81

* Fri Dec 23 2016 Sérgio Basto <sergio@serjux.com> - 0.80-3
- set jar classpath with (unbundle) system libraries (instead use symbol links)
- gnatenkobrain review:
  - btw, you can remove / between %{buildroot} and others.
  - probably you meant %{ix86}
  - to %check please

* Mon Dec 19 2016 Sérgio Basto <sergio@serjux.com> - 0.80-2
- Bump release
- Use external .desktop file easier to send to upstream
- Add Packaging:AppData

* Fri Jun 17 2016 Oleg Kishinskiy <legunt@yandex.ru> - 0.80-1
- Update for new vertion

* Fri Mar 20 2015 Oleg Kishinskiy <legunt@yandex.ru> - 0.79-3
- add ant for BuildRequires

* Fri Mar 20 2015 Oleg Kishinskiy <legunt@yandex.ru> - 0.79-2
- FIX change category

* Fri Mar 20 2015 Oleg Kishinskiy <legunt@yandex.ru> - 0.79-1
- update for new vertion
- change category

* Tue Dec 23 2014 Oleg Kishinskiy <legunt@yandex.ru> - 0.78-3
- fix spec to install from source

* Wed Dec 10 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.78-2
- spec cleanup

* Wed Dec 10 2014 Oleg Kishinskiy <legunt@yandex.ru> - 0.78-1
- Update for new vertion

* Mon Jul 29 2013 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.76-2
- Initial build rpm 
