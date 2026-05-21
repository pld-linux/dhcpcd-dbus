Summary:	DBus bindings for dhcpcd
Name:		dhcpcd-dbus
Version:	0.6.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://roy.marples.name/downloads/dhcpcd/%{name}-%{version}.tar.bz2
# Source0-md5:	3e0762be2f2336dceebaa319f388c8dd
URL:		http://roy.marples.name/projects/dhcpcd-dbus/wiki
BuildRequires:	dbus-devel >= 1.1.0
BuildRequires:	pkgconfig
Requires:	dhcpcd >= 5.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dhcpcd-dbus receives interface configuration events from the dhcpcd
control socket and emits them to the DBus listeners. It also has
methods to release, rebind, stop, query and configure dhcpcd on an
interface.

dhcpcd-dbus also listens to wpa_supplicant for wireless interfaces via
its control socket.

%prep
%setup -q

%build
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/dhcpcd-dbus.conf
%attr(755,root,root) %{_libexecdir}/dhcpcd-dbus
%{_datadir}/dbus-1/system-services/name.marples.roy.dhcpcd.service
