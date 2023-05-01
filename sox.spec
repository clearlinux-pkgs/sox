#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sox
Version  : 14.4.2
Release  : 16
URL      : https://sourceforge.net/projects/sox/files/sox/14.4.2/sox-14.4.2.tar.bz2
Source0  : https://sourceforge.net/projects/sox/files/sox/14.4.2/sox-14.4.2.tar.bz2
Summary  : Audio file format and effects library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: sox-bin = %{version}-%{release}
Requires: sox-lib = %{version}-%{release}
Requires: sox-license = %{version}-%{release}
Requires: sox-man = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-cmake
BuildRequires : file-dev
BuildRequires : libsndfile-dev
BuildRequires : pkgconfig(flac)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(opusfile)
BuildRequires : pkgconfig(vorbis)
Patch1: CVE-2017-11332.patch
Patch2: CVE-2017-11358.patch
Patch3: CVE-2017-11359.patch
Patch4: CVE-2017-15370.patch
Patch5: CVE-2017-15371.patch
Patch6: CVE-2017-15372.patch
Patch7: CVE-2017-15642.patch
Patch8: CVE-2017-18189.patch
Patch9: CVE-2019-8354.patch
Patch10: CVE-2019-8355.patch
Patch11: CVE-2019-8356.patch
Patch12: CVE-2019-8357.patch
Patch13: CVE-2019-13590.patch

%description
SoX: Sound eXchange
===================
SoX (Sound eXchange) is the Swiss Army knife of sound processing tools: it
can convert sound files between many different file formats & audio devices,
and can apply many sound effects & transformations, as well as doing basic
analysis and providing input to more capable analysis and plotting tools.

%package bin
Summary: bin components for the sox package.
Group: Binaries
Requires: sox-license = %{version}-%{release}

%description bin
bin components for the sox package.


%package dev
Summary: dev components for the sox package.
Group: Development
Requires: sox-lib = %{version}-%{release}
Requires: sox-bin = %{version}-%{release}
Provides: sox-devel = %{version}-%{release}
Requires: sox = %{version}-%{release}

%description dev
dev components for the sox package.


%package lib
Summary: lib components for the sox package.
Group: Libraries
Requires: sox-license = %{version}-%{release}

%description lib
lib components for the sox package.


%package license
Summary: license components for the sox package.
Group: Default

%description license
license components for the sox package.


%package man
Summary: man components for the sox package.
Group: Default

%description man
man components for the sox package.


%prep
%setup -q -n sox-14.4.2
cd %{_builddir}/sox-14.4.2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664907175
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
%configure --disable-static --with-png \
--with-pulseaudio \
--with-oggvorbis \
--with-flac
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1664907175
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sox
cp %{_builddir}/sox-%{version}/COPYING %{buildroot}/usr/share/package-licenses/sox/80e5c5a14b56473afb672af36c556e8416cf93a0 || :
cp %{_builddir}/sox-%{version}/LICENSE.GPL %{buildroot}/usr/share/package-licenses/sox/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/sox-%{version}/LICENSE.LGPL %{buildroot}/usr/share/package-licenses/sox/caeb68c46fa36651acf592771d09de7937926bb3 || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/play
/usr/bin/rec
/usr/bin/sox
/usr/bin/soxi

%files dev
%defattr(-,root,root,-)
/usr/include/sox.h
/usr/lib64/libsox.so
/usr/lib64/pkgconfig/sox.pc
/usr/share/man/man3/libsox.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsox.so.3
/usr/lib64/libsox.so.3.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sox/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/sox/80e5c5a14b56473afb672af36c556e8416cf93a0
/usr/share/package-licenses/sox/caeb68c46fa36651acf592771d09de7937926bb3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/play.1
/usr/share/man/man1/rec.1
/usr/share/man/man1/sox.1
/usr/share/man/man1/soxi.1
/usr/share/man/man7/soxeffect.7
/usr/share/man/man7/soxformat.7
