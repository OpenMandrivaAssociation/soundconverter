Summary:	Sound converter application for the GNOME environment
Name:		soundconverter
Version:	1.5.3
Release:	%mkrel 1
License:	GPLv3
Group:		Sound
URL:		http://soundconverter.berlios.de/
Source0:	http://download.berlios.de/soundconverter/%{name}-%{version}.tar.gz
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
BuildRoot:	%{_tmppath}/%{name}-buildroot

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
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install \
  --add-category="Audio" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*
