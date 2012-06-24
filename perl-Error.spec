%include	/usr/lib/rpm/macros.perl
Summary:	Error perl module
Summary(pl):	Modu� perla Error
Name:		perl-Error
Version:	0.13
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Error/Error-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Error perl - Error/exception handling in an OO-ish way.

%description -l pl
Modu� perla Error - obiektowa obs�uga b��d�w/wyj�tk�w.

%prep
%setup -q -n Error-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Error.pm
%{_mandir}/man3/*
