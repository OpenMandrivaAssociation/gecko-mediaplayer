
Summary:	GNOME MPlayer browser plugin
Name:		gecko-mediaplayer
Version:	1.0.3
Release:	%mkrel 1
License:	GPLv2+
URL:		http://kdekorte.googlepages.com/gecko-mediaplayer
Source:		http://gecko-mediaplayer.googlecode.com/files/%name-%version.tar.gz
Group:		Networking/WWW
Requires:	gnome-mplayer >= 0.5.2
Requires(post,preun):	GConf2
BuildRequires:	xulrunner-devel
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	libx11-devel
BuildRequires:	libGConf2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Gecko Media Player is a browser plugin that uses GNOME MPlayer to
play media in a browser. It should work with all browsers on
Unix-ish systems(Linux, BSD, Solaris) and use the NS4 API (Mozilla,
Firefox, Opera, etc.).

%prep
%setup -q

%build
%configure2_5x --enable-new-libxul
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mv %{buildroot}%{_docdir}/%{name} installed-docs
rm installed-docs/{INSTALL,COPYING}

# zero length docs
find installed-docs -size 0 | xargs rm

%find_lang %{name}

rm -f %{buildroot}%{_libdir}/mozilla/plugins/%{name}*.la

%clean
rm -rf %{buildroot}

%post
%post_install_gconf_schemas %{name}

%preun
%preun_uninstall_gconf_schemas %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc installed-docs/*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_libdir}/mozilla/plugins/%{name}*.so
