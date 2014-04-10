%define __spec_install_post %{nil}
%define debug_package %{nil}
%define __os_install_post %{_dbpath}/brp-compress

Summary: company webapp apache data
Name: webapp
Version: 1.0.0
Release: 1
License: GPL+
Group: Development/Tools
SOURCE0 : %{name}-%{version}.tar.gz
URL: https://github.com/brada-vmware/webapp

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q

%build
# Empty section.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

# in builddir
cp -a * %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%/var/www/html/*

%changelog
* Wed Apr 09 2014 Brad Anderson <brada@vmware.com> 1.0.0-1
- First Build
