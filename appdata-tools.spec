Summary:	Tools for AppData files
Name:		appdata-tools
Version:	0.1.7
Release:	1
License:	GPLv2+
Group:		File tools
Url:		http://people.freedesktop.org/~hughsient/appdata/
Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxslt)

%description
appdata-tools contains a command line program designed to validate AppData
application descriptions for standards compliance and to the style guide.

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/appdata-validate
%{_mandir}/man1/appdata-validate.1.*
%dir %{_datadir}/appdata/schema
%{_datadir}/appdata/schema/appdata.xsd
%{_datadir}/appdata/schema/appdata.rnc
%{_datadir}/appdata/schema/schema-locating-rules.xml
%{_datadir}/aclocal/appdata-xml.m4
%{_datadir}/emacs/site-lisp/site-start.d/appdata-rng-init.el

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

