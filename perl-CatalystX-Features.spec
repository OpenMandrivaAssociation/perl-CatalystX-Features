%define upstream_name    CatalystX-Features
%define upstream_version 0.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Root Controller for Test
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CatalystX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Catalyst)
BuildRequires: perl(Catalyst::Action::RenderView)
BuildRequires: perl(Catalyst::Plugin::ConfigLoader)
BuildRequires: perl(Catalyst::Plugin::Static::Simple)
BuildRequires: perl(Class::Inspector)
BuildRequires: perl(Config::General)
BuildRequires: perl(FindBin)
BuildRequires: perl(Moose)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The idea behind this module is to make it easier to spread your code
outside of the main application directory, in the spirit of Eclipse
features and Ruby on Rails plugins.

It's mainly useful if you're working on a large application with distinct
isolated features that are not tightly coupled with the main app and could
be pulled off or eventually reused somewhere else.

It also comes handy in a large project, with many developers working on
specific application parts. And, say, you wish to split the functionality
in diretories, or just want to keep them out of the application core files.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


