Summary: Removes ifdefs from C files.
Name: unifdef
Version: 2.3
Release: 1
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
* Wed May 12 2010 Bernhard Rosenkraenzer <bero@arklinux.org> 2.3-1ark
- 2.3
- Allow crosscompiling

* Sun Jan 27 2008 Bernhard Rosenkraenzer <bero@arklinux.org> 1.0-3ark
- Rebuild to get a package into the x86_64 tree

* Sat Jul 15 2006 Bernhard Rosenkraenzer <bero@arklinux.org> 1.0-2ark
- Compile it instead of allowing make install to use the binary in the
  tarball

* Tue May 23 2006 Bernhard Rosenkraenzer <bero@arklinux.org> 1.0-1ark
- initial package
