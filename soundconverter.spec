%define name	soundconverter
%define version	0.9.0
%define pre alpha1
%define fversion %version-%pre
%define release %mkrel 0.%pre.1

Name: 	 	%{name}
Summary: 	Sound converter application for the GNOME environment
Version: 	%{version}
Release: 	%{release}

Source:		http://download.berlios.de/soundconverter/%{name}-%{fversion}.tar.bz2
Patch: soundconverter-0.9.0-alpha1-missing.patch
URL:		http://soundconverter.berlios.de/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
#BuildRequires:  ImageMagick
BuildRequires:  pygtk2.0-devel
BuildRequires:  desktop-file-utils
Requires:	gstreamer0.10-gnomevfs gnome-python-gnomevfs
Requires:	gstreamer0.10-python
Requires:	pygtk2.0-libglade
Requires:	gnome-python-gconf 
Requires:	gnome-python
BuildArch:	noarch
#Suggests: gstreamer0.10-lame

%description
SoundConverter is a simple sound converter application for the GNOME
environment. It reads and writes WAV, FLAC, MP3 and Ogg Vorbis. The user
interface is raw, but should be simple enough to get the job done. 

NOTE: To create MP3 files, you will have to install gstreamer0.10-lame
yourself.

%prep
%setup -q -n %name-%fversion
%patch -p1 -b .missing

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

perl -pi -e "s/guillaume.bedot wanadoo.fr/littletux zarb.org/" %buildroot%_bindir/soundconverter

#man page
#mkdir -p %buildroot/%_mandir/man1
#cp *.1 %buildroot/%_mandir/man1/
#bzip2 %buildroot/%_mandir/man1/*.1


#menu
mkdir -p %buildroot%{_menudir}
cat << EOF > %buildroot%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="sound_section.png" needs="x11" title="Sound Converter" longtitle="Change sound file formats" section="Multimedia/Sound" xdg="true"
EOF
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Multimedia" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


%find_lang %{name}

%clean
rm -rf %buildroot

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog README TODO
%{_bindir}/%name
%{_datadir}/%name
%{_mandir}/man1/*
%{_menudir}/%name
%{_datadir}/applications/%{name}.desktop
