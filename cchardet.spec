#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cchardet
Version  : 2.1.7
Release  : 16
URL      : https://files.pythonhosted.org/packages/a8/5d/090c9f0312b7988a9433246c9cf0b566b1ae1374368cfb8ac897218a4f65/cchardet-2.1.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/a8/5d/090c9f0312b7988a9433246c9cf0b566b1ae1374368cfb8ac897218a4f65/cchardet-2.1.7.tar.gz
Summary  : cChardet is high speed universal character encoding detector.
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 MPL-1.1
Requires: cchardet-bin = %{version}-%{release}
Requires: cchardet-license = %{version}-%{release}
Requires: cchardet-python = %{version}-%{release}
Requires: cchardet-python3 = %{version}-%{release}
Requires: requests
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : requests

%description
========
        
        cChardet is high speed universal character encoding detector. - binding to `uchardet`_.

%package bin
Summary: bin components for the cchardet package.
Group: Binaries
Requires: cchardet-license = %{version}-%{release}

%description bin
bin components for the cchardet package.


%package license
Summary: license components for the cchardet package.
Group: Default

%description license
license components for the cchardet package.


%package python
Summary: python components for the cchardet package.
Group: Default
Requires: cchardet-python3 = %{version}-%{release}

%description python
python components for the cchardet package.


%package python3
Summary: python3 components for the cchardet package.
Group: Default
Requires: python3-core
Provides: pypi(cchardet)

%description python3
python3 components for the cchardet package.


%prep
%setup -q -n cchardet-2.1.7
cd %{_builddir}/cchardet-2.1.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635709513
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cchardet
cp %{_builddir}/cchardet-2.1.7/COPYING %{buildroot}/usr/share/package-licenses/cchardet/b43296a79ba94d20f8bf64837d7680856776337c
cp %{_builddir}/cchardet-2.1.7/src/ext/uchardet/COPYING %{buildroot}/usr/share/package-licenses/cchardet/b43296a79ba94d20f8bf64837d7680856776337c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cchardetect

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cchardet/b43296a79ba94d20f8bf64837d7680856776337c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
