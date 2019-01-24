
Summary:	GNOME MPlayer browser plugin
Name:		gecko-mediaplayer
Version:	1.0.9
Release:	1
License:	GPLv2+
URL:		http://kdekorte.googlepages.com/gecko-mediaplayer
Source:		http://gecko-mediaplayer.googlecode.com/files/%name-%version.tar.gz
Patch0:		gecko-mediaplayer-1.0.8-no-xpcom.patch
Patch1:		gecko-mediaplayer-1.0.9-np-loadds.patch
Patch2:		gecko-mediaplayer-1.0.9-libxul.patch
Group:		Networking/WWW
Requires:	gnome-mplayer >= 0.5.2
#BuildRequires:	xulrunner-devel
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(gmlib)
BuildRequires:  pkgconfig(nspr)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Gecko Media Player is a browser plugin that uses GNOME MPlayer to
play media in a browser. It should work with all browsers on
Unix-ish systems(Linux, BSD, Solaris) and use the NS4 API (Mozilla,
Firefox, Opera, etc.).

%prep
%setup -q
%autopatch -p1

%build
autoreconf -fi

export CPPFLAGS="-DNPAPI_USE_CONSTCHARS"
%configure2_5x
%make_build

%install
%make_install

mv %{buildroot}%{_docdir}/%{name} installed-docs
rm installed-docs/{INSTALL,COPYING}

# zero length docs
find installed-docs -size 0 | xargs rm

%find_lang %{name}

rm -f %{buildroot}%{_libdir}/mozilla/plugins/%{name}*.la

%files -f %{name}.lang
%doc installed-docs/*
%{_libdir}/mozilla/plugins/%{name}*.so
