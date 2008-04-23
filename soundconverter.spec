Summary:	Sound converter application for the GNOME environment
Name:		soundconverter
Version:	1.0.2
Release:	%mkrel 1
License:	GPLv3
Group:		Sound
URL:		http://soundconverter.berlios.de/
Source:		http://download.berlios.de/soundconverter/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
#BuildRequires:	ImageMagick
BuildRequires:	pygtk2.0-devel
BuildRequires:	gnome-python
BuildRequires:	desktop-file-utils
#needed to build translations, for now
BuildRequires:	perl(XML::Parser)
Requires:	gstreamer0.10-gnomevfs
Requires:	gnome-python-gnomevfs
Requires:	gstreamer0.10-python
Requires:	pygtk2.0-libglade
Requires:	gnome-python-gconf 
Requires:	gnome-python
#configure	fails if noarch
#BuildArch:	noarch
#Suggests: gstreamer0.10-lame

%description
SoundConverter is a simple sound converter application for the GNOME
environment. It reads and writes WAV, FLAC, MP3 and Ogg Vorbis. The user
interface is raw, but should be simple enough to get the job done. 

NOTE: To create MP3 files, you will have to install gstreamer0.10-lame
yourself.

%prep
%setup -q
perl -pi -e "s|pixmapsdir = \\\$\(datadir\)/pixmaps|pixmapsdir = \\\$\(datadir\)/icons|" data/Makefile.in
sed -i -e 's|Name=No name||' data/soundconverter.desktop*

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

perl -pi -e "s/guillaume.bedot wanadoo.fr/littletux zarb.org/" %{buildroot}%{_bindir}/soundconverter

desktop-file-install \
  --add-category="Audio" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%clean
rm -rf %{buildroot}

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*
