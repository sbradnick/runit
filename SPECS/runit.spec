#
# spec file for package runit
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           runit
Version:        2.1.2
Release:        0
Summary:        A UNIX init scheme with service supervision.
License:        BSD-2-Clause
URL:            http://smarden.org/runit
Source:         http://smarden.org/runit/runit-%{version}.tar.gz
Source1:        README.SUSE-WSL
# Source?:        runit.init
# Source?:        README.SuSE
# Source?:        runit-rpmlintrc
Patch0:         runit-2.0.0_etc_service.patch
Patch1:         compile_warnings.patch
BuildRequires:  glibc-devel-static
%define _sbindir /usr/sbin
%define _bindir /usr/bin
%define pkg_name runit

%description
runit is a cross-platform Unix init scheme with service supervision; a
replacement for sysvinit and other init schemes. It runs on GNU/Linux, *BSD,
Mac OS X, and Solaris, and can easily be adapted to other Unix operating
systems. runit implements a simple three-stage concept:
Stage 1 performs the system's one-time initialization tasks.
Stage 2 starts the system's uptime services (via the runsvdir program).
Stage 3 handles the tasks necessary to shutdown and halt or reboot.

%prep
%setup -n admin/%{pkg_name}-%{version}
%patch0
%patch1 -p2
sed -i -e 's|-O2|%{optflags}|g' src/conf-cc
sed -i -e 's| -s||g' src/conf-ld
%{__cp} %{S:1} .

%build
sh package/compile

%install
for i in $(< package/commands) ; do
    %{__install} -D -m 0755 command/$i %{buildroot}%{_sbindir}/$i
done
%{__install} -d -m 0755 %{buildroot}%{_bindir}
mv %{buildroot}%{_sbindir}/runsv* %{buildroot}%{_bindir}/
mv %{buildroot}%{_sbindir}/sv* %{buildroot}%{_bindir}/
for i in man/*8 ; do
    %{__install} -D -m 0644 $i %{buildroot}%{_mandir}/man8/${i##man/}
done
%{__install} -d -m 0755 %{buildroot}{/etc/service,/etc/sv}
%{__install} -D -m 0750 etc/2 %{buildroot}%{_sbindir}/runsvdir-start

%files
%defattr(-,root,root,-)
%{_sbindir}/*
%{_bindir}/*
%{_mandir}/man8/*.8*
%doc doc/* etc/ README.SUSE-WSL
%doc package/CHANGES package/COPYING package/README package/THANKS package/TODO
%dir %{_sysconfdir}/sv
%dir %{_sysconfdir}/service

%changelog
* Fri Jul 30 2021 Scott Bradnick <sbradnick@suse.com>
- Initial version.
- Added 'README.txt' w/ usage info.
