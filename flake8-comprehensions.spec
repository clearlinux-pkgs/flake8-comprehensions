#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC7125C934883BE5 (me@adamj.eu)
#
Name     : flake8-comprehensions
Version  : 3.1.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/ac/56/3f3ab0cdf263e36bcaa6c549e16aeae266ac1944ed8f7b469189620dda60/flake8-comprehensions-3.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ac/56/3f3ab0cdf263e36bcaa6c549e16aeae266ac1944ed8f7b469189620dda60/flake8-comprehensions-3.1.0.tar.gz
Source1 : https://files.pythonhosted.org/packages/ac/56/3f3ab0cdf263e36bcaa6c549e16aeae266ac1944ed8f7b469189620dda60/flake8-comprehensions-3.1.0.tar.gz.asc
Summary  : A flake8 plugin to help you write better list/set/dict comprehensions.
Group    : Development/Tools
License  : ISC
Requires: flake8-comprehensions-license = %{version}-%{release}
Requires: flake8-comprehensions-python = %{version}-%{release}
Requires: flake8-comprehensions-python3 = %{version}-%{release}
Requires: flake8
BuildRequires : buildreq-distutils3
BuildRequires : flake8

%description
=====================
flake8-comprehensions
=====================
.. image:: https://img.shields.io/pypi/v/flake8-comprehensions.svg
:target: https://pypi.org/project/flake8-comprehensions/

%package license
Summary: license components for the flake8-comprehensions package.
Group: Default

%description license
license components for the flake8-comprehensions package.


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

%description python3
python3 components for the flake8-comprehensions package.


%prep
%setup -q -n flake8-comprehensions-3.1.0
cd %{_builddir}/flake8-comprehensions-3.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573828346
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/flake8-comprehensions
cp %{_builddir}/flake8-comprehensions-3.1.0/LICENSE %{buildroot}/usr/share/package-licenses/flake8-comprehensions/3b98f67b904745157b7acca53f96f7aa7bd2d01c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/flake8-comprehensions/3b98f67b904745157b7acca53f96f7aa7bd2d01c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
