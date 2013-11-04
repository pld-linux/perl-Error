#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Error - error/exception handling in an OO-ish way
Summary(pl.UTF-8):	Error - obiektowa obsługa błędów/wyjątków
Name:		perl-Error
Version:	0.17021
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/Error/Error-%{version}.tar.gz
Source0:	http://www.cpan.org/modules/by-module/Error/SHLOMIF/Error-%{version}.tar.gz
# Source0-md5:	fd98e0041b2acbfb19c6b492243709d2
URL:		http://search.cpan.org/dist/Error/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Test-Pod >= 1.14
BuildRequires:	perl-Test-Pod-Coverage >= 1.04
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Error Perl module provides two interfaces. Firstly Error provides
a procedural interface to exception handling. Secondly Error is a base
class for errors/exceptions that can either be thrown, for subsequent
catch, or can simply be recorded.

%description -l pl.UTF-8
Moduł Perla Error udostępnia dwa interfejsy. Po pierwsze, interfejs
proceduralny do obsługi wyjątków. Po drugie, klasę bazową dla
błędów/wyjątków, które mogą być albo przerzucone dla późniejszego
przejęcia, albo po prostu zarejestrowane.

%prep
%setup -q -n Error-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Error.pm
%dir %{perl_vendorlib}/Error
%{perl_vendorlib}/Error/Simple.pm
%{_mandir}/man3/Error*.3pm*
