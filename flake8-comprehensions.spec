#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC7125C934883BE5 (me@adamj.eu)
#
Name     : flake8-comprehensions
Version  : 3.2.3
Release  : 20
URL      : https://files.pythonhosted.org/packages/9a/f9/60063957dd096966b5323b0c7a3aa33e4ae81f0ef675d80bc8655c6347c7/flake8-comprehensions-3.2.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/9a/f9/60063957dd096966b5323b0c7a3aa33e4ae81f0ef675d80bc8655c6347c7/flake8-comprehensions-3.2.3.tar.gz
Source1  : https://files.pythonhosted.org/packages/9a/f9/60063957dd096966b5323b0c7a3aa33e4ae81f0ef675d80bc8655c6347c7/flake8-comprehensions-3.2.3.tar.gz.asc
Summary  : A flake8 plugin to help you write better list/set/dict comprehensions.
Group    : Development/Tools
License  : ISC
Requires: flake8-comprehensions-python = %{version}-%{release}
Requires: flake8-comprehensions-python3 = %{version}-%{release}
Requires: flake8
BuildRequires : buildreq-distutils3
BuildRequires : flake8

%description
flake8-comprehensions
        =====================

%package python
Summary: python components for the flake8-comprehensions package.
Group: Default
Requires: flake8-comprehensions-python3 = %{version}-%{release}

%description python
python components for the flake8-comprehensions package.


%package python3
Summary: python3 components for the flake8-comprehensions package.
Group: Default
Requires: python3-core
Provides: pypi(flake8_comprehensions)
Requires: pypi(flake8)

%description python3
python3 components for the flake8-comprehensions package.


%prep
%setup -q -n flake8-comprehensions-3.2.3
cd %{_builddir}/flake8-comprehensions-3.2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591625838
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
