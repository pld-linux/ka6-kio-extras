# TODO: libappimage >= 0.1.10, https://github.com/AppImage/libappimage
#
# Conditional build:
%bcond_with	tests		# test suite

%define		ka_ver		%{version}
%define		kf_ver		6.0.0
%define		qt_ver		6.5.0
%define		kaname		kio-extras
Summary:	Additional components to increase the functionality of KIO
Summary(pl.UTF-8):	Dodatkowe komponenty rozszerzające funkcjonalność KIO
Name:		ka6-%{kaname}
Version:	25.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{ka_ver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	7b29a691fe8b595587dc239f492e24f9
URL:		https://kde.org/
BuildRequires:	Imath-devel >= 3.1.12
BuildRequires:	OpenEXR-devel >= 3.0.5
BuildRequires:	Qt6Core-devel >= %{qt_ver}
BuildRequires:	Qt6DBus-devel >= %{qt_ver}
BuildRequires:	Qt6Gui-devel >= %{qt_ver}
BuildRequires:	Qt6Network-devel >= %{qt_ver}
BuildRequires:	Qt6Qt5Compat-devel >= %{qt_ver}
BuildRequires:	Qt6Sql-devel >= %{qt_ver}
BuildRequires:	Qt6Svg-devel >= %{qt_ver}
%{?with_tests:BuildRequires:	Qt6Test-devel >= %{qt_ver}}
BuildRequires:	Qt6Widgets-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.20
BuildRequires:	gperf
BuildRequires:	gettext-tools
BuildRequires:	ka6-libkexiv2-devel
BuildRequires:	kdsoap-qt6-devel >= 2.2.0
BuildRequires:	kdsoap-ws-discovery-client-qt6-devel >= 0.3.0
BuildRequires:	kf6-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf6-karchive-devel >= %{kf_ver}
BuildRequires:	kf6-kcmutils-devel >= %{kf_ver}
BuildRequires:	kf6-kconfig-devel >= %{kf_ver}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kf_ver}
BuildRequires:	kf6-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf6-kdbusaddons-devel >= %{kf_ver}
BuildRequires:	kf6-kdnssd-devel >= %{kf_ver}
BuildRequires:	kf6-kdoctools-devel >= %{kf_ver}
BuildRequires:	kf6-kguiaddons-devel >= %{kf_ver}
BuildRequires:	kf6-ki18n-devel >= %{kf_ver}
BuildRequires:	kf6-kio-devel >= %{kf_ver}
BuildRequires:	kf6-knotifications-devel >= %{kf_ver}
BuildRequires:	kf6-kservice-devel >= %{kf_ver}
BuildRequires:	kf6-ktextwidgets-devel >= %{kf_ver}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kf_ver}
BuildRequires:	kf6-solid-devel >= %{kf_ver}
BuildRequires:	kf6-syntax-highlighting-devel >= %{kf_ver}
BuildRequires:	kp6-plasma-activities-devel
BuildRequires:	kp6-plasma-activities-stats-devel
BuildRequires:	libimobiledevice-devel >= 1.3.0
BuildRequires:	libmtp-devel >= 1.1.2
BuildRequires:	libplist-devel >= 2.0
BuildRequires:	libproxy-devel
BuildRequires:	libssh-devel >= 0.8.3
BuildRequires:	libsmbclient-devel
BuildRequires:	libtirpc-devel >= 1.3.3
BuildRequires:	ninja
BuildRequires:	phonon-qt6-devel >= 4.6.60
BuildRequires:	pkgconfig
BuildRequires:	qcoro-qt6-devel >= 0.10.0
BuildRequires:	qt6-build >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	shared-mime-info
BuildRequires:	taglib-devel >= 1.11
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires:	Qt6Core >= %{qt_ver}
Requires:	Qt6DBus >= %{qt_ver}
Requires:	Qt6Gui >= %{qt_ver}
Requires:	Qt6Network >= %{qt_ver}
Requires:	Qt6Qt5Compat >= %{qt_ver}
Requires:	Qt6Sql >= %{qt_ver}
Requires:	Qt6Svg >= %{qt_ver}
Requires:	Qt6Widgets >= %{qt_ver}
Requires:	kf6-karchive >= %{kf_ver}
Requires:	kf6-kcmutils >= %{kf_ver}
Requires:	kf6-kconfig >= %{kf_ver}
Requires:	kf6-kcoreaddons >= %{kf_ver}
Requires:	kf6-kdbusaddons >= %{kf_ver}
Requires:	kf6-kdnssd >= %{kf_ver}
Requires:	kf6-ki18n >= %{kf_ver}
Requires:	kf6-kio >= %{kf_ver}
Requires:	kf6-knotifications >= %{kf_ver}
Requires:	kf6-kservice >= %{kf_ver}
Requires:	kf6-ktextwidgets >= %{kf_ver}
Requires:	kf6-kwidgetsaddons >= %{kf_ver}
Requires:	kf6-solid-devel >= %{kf_ver}
Requires:	kf6-syntax-highlighting >= %{kf_ver}
Requires:	libimobiledevice >= 1.3.0
Requires:	libmtp >= 1.1.2
Requires:	libssh >= 0.8.3
Requires:	libtirpc-devel >= 1.3.3
Requires:	phonon-qt6 >= 4.6.60
Requires:	taglib >= 1.11
Provides:	kf5-kio-apps = %{version}-%{release}
Obsoletes:	kf5-kio-apps < 6
Obsoletes:	ka5-kio-extras < 6
Conflicts:	kf5-kio < 5.116.0-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional components to increase the functionality of KIO.

%description -l pl.UTF-8
Dodatkowe komponenty rozszerzające funkcjonalność KIO.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kf6-karchive-devel >= %{kf_ver}
Requires:	kf6-kio-devel >= %{kf_ver}
Obsoletes:	ka5-kio-extras-devel < 6

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_desktop_database_post

%postun
/sbin/ldconfig
%update_desktop_database_postun

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%doc DESIGN
%attr(755,root,root) %{_libexecdir}/kf6/smbnotifier
%attr(755,root,root) %{_libexecdir}/wpad-detector-helper
%attr(755,root,root) %{_libdir}/libkioarchive6.so.*.*
%ghost %{_libdir}/libkioarchive6.so.6
%attr(755,root,root) %{_libdir}/qt6/plugins/kcm_trash.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kfileaudiopreview.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/filenamesearchmodule.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/smbwatcher.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/wpad-detector.so
%dir %{_libdir}/qt6/plugins/kf6/kfileitemaction
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfileitemaction/forgetfileitemaction.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfileitemaction/kactivitymanagerd_fileitem_linking_plugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/activities.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/afc.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/archive.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/filter.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/fish.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/info.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/man.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/mtp.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/nfs.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/recentlyused.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/sftp.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/smb.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/thumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/kio_filenamesearch.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kiod/kmtpd.so
%dir %{_libdir}/qt6/plugins/kf6/thumbcreator
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/audiothumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/comicbookthumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/cursorthumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/directorythumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/djvuthumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/ebookthumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/exrthumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/imagethumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/jpegthumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/kraorathumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/opendocumentthumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/svgthumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/textthumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/windowsexethumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/windowsimagethumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_netpref.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_proxy.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_webshortcuts.so
%{_datadir}/config.kcfg/jpegcreatorsettings5.kcfg
%{_datadir}/dbus-1/services/org.kde.kmtpd5.service
%dir %{_datadir}/kio_filenamesearch
%{_datadir}/kio_filenamesearch/kio-filenamesearch-grep
%dir %{_datadir}/kio_info
%{_datadir}/kio_info/kde-info2html
%{_datadir}/kio_info/kde-info2html.conf
%dir %{_datadir}/konqueror
%dir %{_datadir}/konqueror/dirtree
%dir %{_datadir}/konqueror/dirtree/remote
%{_datadir}/konqueror/dirtree/remote/mtp-network.desktop
%{_datadir}/konqueror/dirtree/remote/smb-network.desktop
%{_datadir}/mime/packages/org.kde.kio.smb.xml
%{_datadir}/remoteview/afc-network.desktop
%{_datadir}/remoteview/mtp-network.desktop
%{_datadir}/remoteview/smb-network.desktop
%{_datadir}/solid/actions/solid_afc.desktop
%{_datadir}/solid/actions/solid_mtp.desktop
%{_datadir}/qlogging-categories6/kio-extras.categories
%{_datadir}/qlogging-categories6/kio-extras.renamecategories
%{_desktopdir}/kcm_netpref.desktop
%{_desktopdir}/kcm_proxy.desktop
%{_desktopdir}/kcm_trash.desktop
%{_desktopdir}/kcm_webshortcuts.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/KioArchive6
%{_libdir}/cmake/KioArchive6
