%define upstream_name    Statistics-Basic
%define upstream_version 1.6601

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Epoch:      1

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    A collection of very basic statistics modules
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Statistics/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Number::Format)
BuildRequires: perl(Scalar::Util)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
A collection of very basic statistics modules

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/Statistics

