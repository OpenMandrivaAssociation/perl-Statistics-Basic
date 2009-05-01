%define module   Statistics-Basic
%define version    1.6005
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    A class for computing filtered vectors
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Statistics/%{module}-%{version}.tar.gz
BuildRequires: perl(Number::Format)
BuildRequires: perl(Scalar::Util)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
no description found

%prep
%setup -q -n %{module}-%{version} 

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

