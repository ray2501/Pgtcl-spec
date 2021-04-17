#
# spec file for package PgTcl
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           PgTcl
BuildRequires:  autoconf
BuildRequires:  postgresql-devel
BuildRequires:  tcl-devel >= 8.6
Summary:        Tcl Client Library for PostgreSQL
License:        MIT
Group:          Productivity/Databases/Clients
Version:        2.7.7
Release:        0
Url:            https://github.com/flightaware/Pgtcl
Source0:        Pgtcl-%version.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the libpgtcl client library as a loadable Tcl
package. It is needed to access PostgreSQL databases from Tcl scripts.

%prep
%setup -q -n Pgtcl-%version

%build
autoconf
CFLAGS=-DUSE_INTERP_ERRORLINE
%configure \
        --libdir=%tcl_archdir \
	--with-tcl=%_libdir \
	--with-postgres-include=%_includedir/pgsql \
	--with-postgres-lib=%_libdir
make %{?_smp_mflags}

%install
make install-binaries install-libraries PKG_HEADERS= DESTDIR=%buildroot

%files
%defattr(-,root,root,-)
%doc ChangeLog README.md README.async TODO
%doc doc/PGTCL-NOTES doc/libpgtcl.pdf doc/html
%tcl_archdir

%changelog
