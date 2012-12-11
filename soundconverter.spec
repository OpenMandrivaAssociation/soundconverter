Summary:	Sound converter application for the GNOME environment
Name:		soundconverter
Version:	2.0.3
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


%changelog
* Fri Jul 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.0.3-1
+ Revision: 808314
- version update 2.0.3

* Sun Feb 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.0.1-1
+ Revision: 771301
- version update 2.0.1

* Mon Oct 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5.4-1
+ Revision: 704056
- update t- new version 1.5.4

* Mon Aug 30 2010 Jani Välimaa <wally@mandriva.org> 1.5.3-1mdv2011.0
+ Revision: 574422
- new version 1.5.3
- clean .spec
  - drop support for old mdv versions
  - drop unneeded parts

* Mon Jul 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.4-1mdv2010.0
+ Revision: 401044
- update to new version 1.4.4

* Mon Jun 01 2009 Guillaume Bedot <littletux@mandriva.org> 1.4.3-1mdv2010.0
+ Revision: 381895
- New release

* Tue Jan 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.2-1mdv2009.1
+ Revision: 334210
- update to new version 1.4.2

* Fri Oct 10 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.1-1mdv2009.1
+ Revision: 291530
- add missing buildrequire on intltool
- update to new version 1.4.1
- update to new version 1.4.0

* Sun Aug 03 2008 Funda Wang <fwang@mandriva.org> 1.3.2-1mdv2009.0
+ Revision: 262057
- New version 1.3.2

* Tue Jun 24 2008 Funda Wang <fwang@mandriva.org> 1.3.1-3mdv2009.0
+ Revision: 228516
- rebuild for noarch package

* Tue Jun 24 2008 Funda Wang <fwang@mandriva.org> 1.3.1-2mdv2009.0
+ Revision: 228497
- Should be noarch package
- New version 1.3.1

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon May 12 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.0-1mdv2009.0
+ Revision: 206306
- new version

* Wed Apr 23 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-1mdv2009.0
+ Revision: 196874
- new version

* Mon Apr 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.1-1mdv2009.0
+ Revision: 196251
- new version

* Fri Mar 07 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.9-1mdv2008.1
+ Revision: 181128
- new version

* Thu Jan 10 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.8-1mdv2008.1
+ Revision: 147674
- spec file clean
- fix mixture of tabs and spaces
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 02 2007 Funda Wang <fwang@mandriva.org> 0.9.7-1mdv2008.0
+ Revision: 58185
- BR gnome-python
- drop old menu
- New version 0.9.7
- patches are not needed

* Wed Apr 18 2007 Guillaume Bedot <littletux@mandriva.org> 0.9.4-1mdv2008.0
+ Revision: 14700
- fix buildrequires
- New release 0.9.4

