%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6KIO
%define devname %mklibname KF6KIO -d
#define git 20240217

Name: kf6-kio
Version: 6.6.0
Release: %{?git:0.%{git}.}2
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kio/-/archive/master/kio-master.tar.bz2#/kio-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/frameworks/%{major}/kio-%{version}.tar.xz
%endif
Summary: Network transparent access to files and data
URL: https://invent.kde.org/frameworks/kio
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6KDED)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: %mklibname -d KF6IconWidgets
BuildRequires: pkgconfig(mount)
BuildRequires: pkgconfig(libacl)
BuildRequires: pkgconfig(libattr)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(krb5)
# Just to avoid pulling in the KF5 version
BuildRequires: plasma6-xdg-desktop-portal-kde
Obsoletes: kcookiejar < %{EVRD}
Requires: %{libname} = %{EVRD}

%patchlist

%description
Network transparent access to files and data

%package -n %{libname}
Summary: Network transparent access to files and data
Group: System/Libraries
Requires: %{name} = %{EVRD}
Recommends: switcheroo-control

%description -n %{libname}
Network transparent access to files and data

%package -n %{libname}-designer
Summary: Qt Designer support for %{name} widgets
Group: System/Libraries
Requires: %{libname} = %{EVRD}
Supplements: qt6-qttools-designer

%description -n %{libname}-designer
Qt Designer support for %{name} widgets

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Network transparent access to files and data

%prep
%autosetup -p1 -n kio-%{?git:master}%{!?git:%{version}}
# Disabling PCH on aarch64 is a workaround for an apparent clang 16.0.3 bug
# at compile time:
#	error: is pie differs in PCH file vs. current file
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
%ifarch %{aarch64}
	-DENABLE_PCH:BOOL=OFF \
%endif
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html --with-man

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kio.*
%{_datadir}/kf6/searchproviders
%{_bindir}/ktelnetservice6
%{_bindir}/ktrash6
%dir %{_qtdir}/plugins/kf6/kded
%{_qtdir}/plugins/kf6/kded/remotenotifier.so
%dir %{_qtdir}/plugins/kf6/kio
%{_qtdir}/plugins/kf6/kio/kio_file.so
%{_qtdir}/plugins/kf6/kio/kio_ftp.so
%{_qtdir}/plugins/kf6/kio/kio_ghelp.so
%{_qtdir}/plugins/kf6/kio/kio_help.so
%{_qtdir}/plugins/kf6/kio/kio_http.so
%{_qtdir}/plugins/kf6/kio/kio_remote.so
%{_qtdir}/plugins/kf6/kio/kio_trash.so
%dir %{_qtdir}/plugins/kf6/kiod
%{_qtdir}/plugins/kf6/kiod/kioexecd.so
%{_qtdir}/plugins/kf6/kiod/kpasswdserver.so
%{_qtdir}/plugins/kf6/kiod/kssld.so
%dir %{_qtdir}/plugins/kf6/urifilters
%{_qtdir}/plugins/kf6/urifilters/fixhosturifilter.so
%{_qtdir}/plugins/kf6/urifilters/kshorturifilter.so
%{_qtdir}/plugins/kf6/urifilters/kuriikwsfilter.so
%{_qtdir}/plugins/kf6/urifilters/kurisearchfilter.so
%{_qtdir}/plugins/kf6/urifilters/localdomainurifilter.so
%{_datadir}/applications/ktelnetservice6.desktop
%{_datadir}/dbus-1/services/org.kde.kiod6.service
%{_datadir}/dbus-1/services/org.kde.kioexecd6.service
%{_datadir}/dbus-1/services/org.kde.kpasswdserver6.service
%{_datadir}/dbus-1/services/org.kde.kssld6.service
%{_datadir}/applications/org.kde.kiod6.desktop

%files -n %{devname}
%{_includedir}/KF6/KIO
%{_includedir}/KF6/KIOCore
%{_includedir}/KF6/KIOFileWidgets
%{_includedir}/KF6/KIOGui
%{_includedir}/KF6/KIOWidgets
%{_libdir}/cmake/KF6KIO
%{_qtdir}/doc/KF6KIO.*
%{_datadir}/kdevappwizard/templates/kioworker6.tar.bz2

%files -n %{libname}
%{_libdir}/libKF6KIOCore.so*
%{_libdir}/libKF6KIOFileWidgets.so*
%{_libdir}/libKF6KIOGui.so*
%{_libdir}/libKF6KIOWidgets.so*
%{_libdir}/libkuriikwsfiltereng_private.so
%{_libdir}/libexec/kf6/kiod6
%{_libdir}/libexec/kf6/kioexec
%{_libdir}/libexec/kf6/kioworker

%files -n %{libname}-designer
%{_qtdir}/plugins/designer/kio6widgets.so
