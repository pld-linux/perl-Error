%include	/usr/lib/rpm/macros.perl
Summary:	Error - error/exception handling in an OO-ish way
Summary(pl):	Error - obiektowa obs�uga b��d�w/wyj�tk�w
Name:		perl-Error
Version:	0.15
Release:	4
# same as perl
License:	GPL v1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Error/Error-%{version}.tar.gz
# Source0-md5:	81b4847fb893f18a4e85186bca5f4380
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Error Perl module provides two interfaces. Firstly Error provides
a procedural interface to exception handling. Secondly Error is a base
class for errors/exceptions that can either be thrown, for subsequent
catch, or can simply be recorded.

%description -l pl
Modu� Perla Error udost�pnia dwa interfejsy. Po pierwsze, interfejs
proceduralny do obs�ugi wyj�tk�w. Po drugie, klas� bazow� dla
b��d�w/wyj�tk�w, kt�re mog� by� albo przerzucone dla po�niejszego
przej�cia, albo po prostu zarejestrowane.

- obiektowa obs�uga b��d�w/wyj�tk�w.

%prep
%setup -q -n Error-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Error.pm
%{_mandir}/man3/*
