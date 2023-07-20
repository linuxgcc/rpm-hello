Name:           hello
Version:        2.12
Release:        1
Summary:        The "Hello World" program from GNU

License:        GPLv3+
URL:            http://ftp.gnu.org/gnu/hello
Source0:        http://ftp.gnu.org/gnu/hello/%{name}-%{version}.tar.gz

BuildRequires:  help2man
Requires:       glibc

%description
The "Hello World" program, done with all bells and whistles of a proper FOSS 
project, including configuration, build, internationalization, help files, etc.


%package help
Summary: help package for %{name}

%description help
This is the help package for %{name}. It includes some doc
files and man, info files.


%prep
%autosetup

%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%license COPYING
%{_bindir}/hello

%files help
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_mandir}/man1/*
%{_infodir}/hello.*
%{_infodir}/dir
%{_usr}/share/locale/*/LC_MESSAGES/*



%changelog
* Thu Jul 20 2023 root
- first build hello word
- 
