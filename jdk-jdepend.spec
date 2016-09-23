Name     : jdk-jdepend
Version  : 2.9.1
Release  : 1
URL      : https://github.com/clarkware/jdepend/archive/2.9.1.tar.gz
Source0  : https://github.com/clarkware/jdepend/archive/2.9.1.tar.gz
Source1  : http://repo1.maven.org/maven2/jdepend/jdepend/2.9.1/jdepend-2.9.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : apache-maven
BuildRequires : apache-ant
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-wagon
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn
Patch0   : 0001-Remove-timestamp-in-javadoc.patch

%description
J D E P E N D
What Is It?
-----------

JDepend traverses Java class and source file directories and
generates design quality metrics for each Java package. JDepend allows
you to automatically measure the quality of a design in terms of its
extensibility, reusability, and maintainability to effectively manage
and control package dependencies.

%prep
%setup -q -n jdepend-2.9.1
%patch0 -p1

find . -name "*.jar" -delete
find . -type d -exec chmod 755 {} \;
python3 /usr/share/java-utils/mvn_file.py jdepend:jdepend jdepend

%build
ant jar javadoc

%install
python3 /usr/share/java-utils/mvn_artifact.py %{SOURCE1} dist/jdepend-2.9.1.jar
xmvn-install  -R .xmvn-reactor -n jdepend -d %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/java/jdepend.jar
/usr/share/maven-metadata/jdepend.xml
/usr/share/maven-poms/jdepend.pom
