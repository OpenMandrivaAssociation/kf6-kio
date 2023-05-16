%define libname %mklibname KF6KIO
%define devname %mklibname KF6KIO -d
%define git 20230513

Name: kf6-kio
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kio/-/archive/master/kio-master.tar.bz2#/kio-%{git}.tar.bz2
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
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
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
Requires: %{libname} = %{EVRD}

%description
Network transparent access to files and data

%package -n %{libname}
Summary: Network transparent access to files and data
Group: System/Libraries
Requires: %{name} = %{EVRD}

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
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html --with-man

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kio.*
%{_datadir}/kservices6/searchproviders
%{_sysconfdir}/xdg/accept-languages.codes
%{_sysconfdir}/xdg/kshorturifilterrc
%{_bindir}/kcookiejar5
%{_bindir}/ktelnetservice6
%{_bindir}/ktrash6
%{_qtdir}/plugins/kcm_trash.so
%dir %{_qtdir}/plugins/kf6/kded
%{_qtdir}/plugins/kf6/kded/kcookiejar.so
%{_qtdir}/plugins/kf6/kded/proxyscout.so
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
%dir %{_qtdir}/plugins/plasma
%dir %{_qtdir}/plugins/plasma/kcms
%dir %{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_cookies.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_netpref.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_proxy.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_smb.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_webshortcuts.so
%{_datadir}/applications/kcm_trash.desktop
%{_datadir}/applications/ktelnetservice6.desktop
%{_datadir}/dbus-1/interfaces/kf5_org.kde.KCookieServer.xml
%{_datadir}/dbus-1/interfaces/kf5_org.kde.KDirNotify.xml
%{_datadir}/dbus-1/interfaces/kf5_org.kde.KPasswdServer.xml
%{_datadir}/dbus-1/interfaces/kf5_org.kde.kio.FileUndoManager.xml
%{_datadir}/dbus-1/services/org.kde.kcookiejar5.service
%{_datadir}/dbus-1/services/org.kde.kiod5.service
%{_datadir}/dbus-1/services/org.kde.kioexecd.service
%{_datadir}/dbus-1/services/org.kde.kpasswdserver.service
%{_datadir}/dbus-1/services/org.kde.kssld5.service
%{_datadir}/kconf_update/filepicker.upd
%{_datadir}/kf6/kcookiejar/domain_info
%{_datadir}/knotifications6/proxyscout.notifyrc
%{_mandir}/man8/kcookiejar5.8*

%files -n %{devname}
%{_includedir}/KF6/KIO
%{_includedir}/KF6/KIOCore
%{_includedir}/KF6/KIOFileWidgets
%{_includedir}/KF6/KIOGui
%{_includedir}/KF6/KIOWidgets
%{_libdir}/cmake/KF6KIO
%{_qtdir}/mkspecs/modules/qt_KIOCore.pri
%{_qtdir}/mkspecs/modules/qt_KIOFileWidgets.pri
%{_qtdir}/mkspecs/modules/qt_KIOGui.pri
%{_qtdir}/mkspecs/modules/qt_KIOWidgets.pri
%{_qtdir}/doc/KF6KIO.*
%{_datadir}/kdevappwizard/templates/kioworker.tar.bz2

%files -n %{libname}
%{_libdir}/libKF6KIOCore.so*
%{_libdir}/libKF6KIOFileWidgets.so*
%{_libdir}/libKF6KIOGui.so*
%{_libdir}/libKF6KIOWidgets.so*
%{_libdir}/libexec/kf6/kio_http_cache_cleaner
%{_libdir}/libexec/kf6/kiod5
%{_libdir}/libexec/kf6/kioexec
%{_libdir}/libexec/kf6/kioworker
%{_libdir}/libexec/kf6/kpac_dhcp_helper

%files -n %{libname}-designer
%{_qtdir}/plugins/designer/kio6widgets.so
