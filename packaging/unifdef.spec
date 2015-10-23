Summary: Removes ifdefs from C files.
Name: unifdef
Version: 2.3
Release: %{?release_prefix:%{release_prefix}.}1.44.%{?dist}%{!?dist:tizen}
VCS:     external/unifdef#submit/trunk/20121022.015811-0-g24c5f44c59bb826a7240b862bd518e0c5fa7ba54
License: BSD
Group: Development/Tools
URL: http://dotat.at/prog/unifdef/
Source: http://dotat.at/prog/unifdef/%name-%version.tar.gz
BuildRoot: %_tmppath/%name-%version-%release

%description
Unifdef is useful for removing ifdef'ed lines from a file while otherwise
leaving the file alone.  Unifdef acts on #ifdef, #ifndef, #else, and #en­
dif lines, and it knows only enough about C to know when one of these is
inactive because it is inside a comment, or a single or double quote.

%track
prog %name = {
	url = http://dotat.at/prog/unifdef/
	version = %version
	regex = %name-(__VER__)\.tar\.gz
}

%prep
%setup
make clean

%build
make %?_smp_mflags CC=%__cc CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR="$RPM_BUILD_ROOT" prefix=%_prefix

%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/unifdef
%_bindir/unifdefall
%_mandir/man1/unifdef.1*
%_mandir/man1/unifdefall.1*

%changelog
* Mon Sep 16 2013 UkJung Kim <ujkim@samsung.com> - submit/trunk/20121022.015811 
- PROJECT: external/unifdef
- COMMIT_ID: 24c5f44c59bb826a7240b862bd518e0c5fa7ba54
- PATCHSET_REVISION: 24c5f44c59bb826a7240b862bd518e0c5fa7ba54
- CHANGE_OWNER: \"UkJung Kim\" <ujkim@samsung.com>
- PATCHSET_UPLOADER: \"UkJung Kim\" <ujkim@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/103654
- PATCHSET_REVISION: 24c5f44c59bb826a7240b862bd518e0c5fa7ba54
- TAGGER: UkJung Kim <ujkim@samsung.com>
- Gerrit patchset approval info:
- UkJung Kim <ujkim@samsung.com> Verified : 1
- Newton Lee <newton.lee@samsung.com> Code Review : 2
- CHANGE_SUBJECT: Initial commit
- [Version] 2.3
- [Project] GT-I8800
- [Title] Initial commit
- [BinType] PDA
- [Customer] Open
- [Issue#] N/A
- [Problem] N/A
- [Cause] N/A
- [Solution]
- [Team] SCM
- [Developer] UkJung Kim <ujkim@samsung.com>
- [Request] N/A
- [Horizontal expansion] N/A
- [SCMRequest] N/A
