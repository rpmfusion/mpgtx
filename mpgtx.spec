Name:           mpgtx
Version:        1.3.1
Release:        23%{?dist}
Summary:        An MPEG toolbox

License:        GPLv2+
URL:            http://mpgtx.sourceforge.net/
Source0:        http://dl.sf.net/mpgtx/mpgtx-1.3.1.tar.gz
Patch0:         mpgtx-1.3.1-makefile.patch

BuildRequires:  gcc-c++

%description
mpgtx allows you to split, join, demultiplex, manipulate ID3 tags and
fetch detailed information about a variety of MPEG files. 


%prep
%setup -q
%patch0 -p6 -b .makefile
for f in ChangeLog man/de/mpgtx.1 man/de/tagmp3.1 ; do
    iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f
done


%build
./configure --prefix=%{_prefix}
make


%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} manprefix=$RPM_BUILD_ROOT%{_datadir}


%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*

%changelog
* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
- Fix license
- Add BuildRequires:  gcc-c++

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.3.1-8
- Mass rebuilt for Fedora 19 Features

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.3.1-7
- Rebuilt for c++ ABI breakage

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.3.1-5
- rebuild for new F11 features

* Sun Aug 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.3.1-4
- rebuild

* Sun Oct  7 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.3.1-3
- Fix empty debuginfo package (#993).
- Convert docs to UTF-8.
- %%lang'ify German man pages.

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 1.3.1-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field
- drop Epoch

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Mon Jan 17 2005 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:1.3.1-0.lvn.1
- Updated to 1.3.1.

* Wed Dec  8 2004 Dams <anvil[AT]livna.org> - 0:1.3-0.lvn.4
- Patch0 needs -p6, not -p0.

* Thu Oct 28 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:1.3-0.lvn.3
- Fixed build patch for FC3 compilation.

* Tue Apr  8 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:1.3-0.fdr.2
- Added epoch.
- Modified source URL to allow direct downloading.

* Sat Mar 20 2003 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 1.3-0.fdr.1
- Initial Fedora RPM release.
