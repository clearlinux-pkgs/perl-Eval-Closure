#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Eval-Closure
Version  : 0.14
Release  : 32
URL      : https://cpan.metacpan.org/authors/id/D/DO/DOY/Eval-Closure-0.14.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DO/DOY/Eval-Closure-0.14.tar.gz
Summary  : 'safely and cleanly create closures via string eval'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl Artistic-2.0 GPL-1.0
Requires: perl-Eval-Closure-license = %{version}-%{release}
Requires: perl-Eval-Closure-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Requires)
BuildRequires : perl(Try::Tiny)

%description
This archive contains the distribution Eval-Closure,
version 0.14:
safely and cleanly create closures via string eval

%package dev
Summary: dev components for the perl-Eval-Closure package.
Group: Development
Provides: perl-Eval-Closure-devel = %{version}-%{release}
Requires: perl-Eval-Closure = %{version}-%{release}

%description dev
dev components for the perl-Eval-Closure package.


%package license
Summary: license components for the perl-Eval-Closure package.
Group: Default

%description license
license components for the perl-Eval-Closure package.


%package perl
Summary: perl components for the perl-Eval-Closure package.
Group: Default
Requires: perl-Eval-Closure = %{version}-%{release}

%description perl
perl components for the perl-Eval-Closure package.


%prep
%setup -q -n Eval-Closure-0.14
cd %{_builddir}/Eval-Closure-0.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Eval-Closure
cp %{_builddir}/Eval-Closure-0.14/LICENSE %{buildroot}/usr/share/package-licenses/perl-Eval-Closure/7be6ac2a9daa3606494d27e6f00b73fe78480849
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Eval::Closure.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Eval-Closure/7be6ac2a9daa3606494d27e6f00b73fe78480849

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
