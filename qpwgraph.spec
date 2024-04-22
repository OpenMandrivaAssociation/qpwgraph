%global provider org.rncbc.qpwgraph

Name:           qpwgraph
Version:        0.6.3
Release:        1
Summary:        PipeWire Graph Qt GUI Interface
License:        GPLv2+
URL:            https://gitlab.freedesktop.org/rncbc/qpwgraph
Source0:        https://gitlab.freedesktop.org/rncbc/qpwgraph/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  appstream-util
BuildRequires:  cmake
BuildRequires:	cmake(qt6)
BuildRequires:	qmake-qt6
BuildRequires:	qt6-qttools
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  vulkan-headers
Requires:       pipewire
Requires:       hicolor-icon-theme
Requires:       shared-mime-info

%description
qpwgraph is a graph manager dedicated to PipeWire, using the Qt C++ framework,
based and pretty much like the same of QjackCtl.

%prep
%autosetup -n %{name}-v%{version} -p1

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DCONFIG_ALSA_MIDI=ON
%make_build

%install
%make_install -C build


%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/%{provider}.desktop
%{_metainfodir}/%{provider}.metainfo.xml
%{_datadir}/mime/packages/%{provider}.xml
%{_mandir}/man1/qpwgraph.1.*
