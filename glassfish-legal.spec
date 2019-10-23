%{?scl:%scl_package glassfish-legal}
%{!?scl:%global pkg_name %{name}}

Name:          %{?scl_prefix}glassfish-legal
Version:       1.1
Release:       12.1%{?dist}
Summary:       Legal License for glassfish code
License:       CDDL or GPLv2 with exceptions
URL:           http://glassfish.java.net/
# svn export https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/ glassfish-legal-1.1
# tar czf glassfish-legal-1.1-src-svn.tar.gz glassfish-legal-1.1
Source0:       %{pkg_name}-%{version}-src-svn.tar.gz

BuildRequires: %{?scl_prefix}glassfish-master-pom
BuildRequires: %{?scl_prefix}maven-local
BuildRequires: %{?scl_prefix}maven-remote-resources-plugin

Requires:      %{?scl_prefix}glassfish-master-pom
BuildArch:     noarch

%description
An archive which contains license files for glassfish code.

%prep
%setup -q -n %{pkg_name}-%{version}

sed -i 's/\r//' src/main/resources/META-INF/LICENSE.txt
cp -p src/main/resources/META-INF/LICENSE.txt .

%mvn_file :legal %{pkg_name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%changelog
* Tue Sep  3 2019 Java Maintainers <java-maint@redhat.com> - 1.1-12.1
- Automated package import and SCL-ization

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-12
- Mass rebuild for javapackages-tools 201901

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 03 2015 gil cattaneo <puntogil@libero.it> 1.1-6
- introduce license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.1-4
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 gil cattaneo <puntogil@libero.it> 1.1-2
- switch to XMvn
- minor changes to adapt to current guideline

* Wed Jan 16 2013 gil cattaneo <puntogil@libero.it> 1.1-1
- initial rpm
