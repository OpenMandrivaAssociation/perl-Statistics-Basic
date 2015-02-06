%define upstream_name    Statistics-Basic
%define upstream_version 1.6607

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.6607
Release:	3
Epoch:		1

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	A collection of very basic statistics modules
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Statistics/Statistics-Basic-1.6607.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Number::Format)
BuildRequires:	perl(Scalar::Util)
BuildArch:	noarch

%description
A collection of very basic statistics modules

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Statistics

%changelog
* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1:1.660.200-1mdv2011.0
+ Revision: 596648
- update to 1.6602

* Mon Sep 14 2009 Jérôme Quelin <jquelin@mandriva.org> 1:1.660.100-1mdv2011.0
+ Revision: 439432
- update to 1.6601
- update to 1.6600

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.6500

* Tue Jun 30 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.660.0-1mdv2010.0
+ Revision: 390840
- update to new version 1.6600

* Sat May 30 2009 Jérôme Quelin <jquelin@mandriva.org> 1:1.650.0-1mdv2010.0
+ Revision: 381275
- adding epoch: tag to make sure %%perl_convert_version gets picked
- really use %%perl_convert_version

* Sat May 30 2009 Jérôme Quelin <jquelin@mandriva.org> 1.6500-1mdv2010.0
+ Revision: 381271
- update to 1.6500
- using %%perl_convert_version
- fixed license, summary and description fields

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.6007-2mdv2010.0
+ Revision: 375901
- rebuild

* Sun May 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.6007-1mdv2010.0
+ Revision: 371340
- update to new version 1.6007

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.6005-1mdv2010.0
+ Revision: 370179
- update to new version 1.6005

* Mon Mar 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.6004-1mdv2009.1
+ Revision: 355662
- import perl-Statistics-Basic


* Mon Mar 16 2009 cpan2dist 1.6004-1mdv
- initial mdv release, generated with cpan2dist


