Summary:	Sound converter application for the GNOME environment
Name:		soundconverter
Version:	2.0.1
Release:	1
License:	GPLv3
Group:		Sound
URL:		http://soundconverter.berlios.de/
Source0:	http://launchpad.net/soundconverter/trunk/2.0.1/+download/%{name}-%{version}.tar.xz
BuildRequires:	pygtk2.0-devel
BuildRequires:	gnome-python
BuildRequires:	desktop-file-utils
BuildRequires:	perl(XML::Parser)
BuildRequires:	intltool
Requires:	gstreamer0.10-gnomevfs
Requires:	gnome-python-gnomevfs
Requires:	gstreamer0.10-python
Requires:	pygtk2.0-libglade
Requires:	gnome-python-gconf 
Requires:	gnome-python
#Suggests: gstreamer0.10-lame
BuildArch:	noarch

%description
SoundConverter is a simple sound converter application for the GNOME
environment. It reads and writes WAV, FLAC, MP3 and Ogg Vorbis. The user
interface is raw, but should be simple enough to get the job done. 

NOTE: To create MP3 files, you will have to install gstreamer0.10-lame
yourself.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

desktop-file-install \
  --add-category="Audio" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog README TODO
%{_bindir}/%{name}
%{_libdir}/%{name}/python/%{name}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*
