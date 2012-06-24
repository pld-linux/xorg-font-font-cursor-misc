Summary:	cursor font
Summary(pl.UTF-8):	Font cursor
Name:		xorg-font-font-cursor-misc
Version:	1.0.0
Release:	1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-cursor-misc-%{version}.tar.bz2
# Source0-md5:	305fa22cdfefb8f80babd711051a534b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cursor font needed by X server.

%description -l pl.UTF-8
Font cursor wymagany przez serwer X.

%prep
%setup -q -n font-cursor-misc-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-fontdir=%{_fontsdir}/misc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_fontsdir}/misc/cursor.pcf.gz
