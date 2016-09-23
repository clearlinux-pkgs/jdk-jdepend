PKG_NAME := jdk-jdepend
URL := https://github.com/clarkware/jdepend/archive/2.9.1.tar.gz
ARCHIVES := http://repo1.maven.org/maven2/jdepend/jdepend/2.9.1/jdepend-2.9.1.pom %{buildroot}

include ../common/Makefile.common
