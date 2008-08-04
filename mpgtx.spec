Name:           mpgtx
Version:        1.3.1
Release:        4%{?dist}
Summary:        An MPEG toolbox

Group:          Applications/Multimedia
License:        GPL
URL:            http://mpgtx.sourceforge.net/
Source0:        http://dl.sf.net/mpgtx/mpgtx-1.3.1.tar.gz
Patch0:         mpgtx-1.3.1-makefile.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


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
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} manprefix=$RPM_BUILD_ROOT%{_datadir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/*
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*

%changelog
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
