%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-mrpt-msgs
Version:        0.4.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS mrpt_msgs package

License:        BSD
URL:            https://wiki.ros.org/mrpt_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-geometry-msgs
Requires:       ros-humble-rosidl-default-runtime
Requires:       ros-humble-sensor-msgs
Requires:       ros-humble-std-msgs
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-geometry-msgs
BuildRequires:  ros-humble-ros-environment
BuildRequires:  ros-humble-rosidl-default-generators
BuildRequires:  ros-humble-sensor-msgs
BuildRequires:  ros-humble-std-msgs
BuildRequires:  ros-humble-ros-workspace
BuildRequires:  ros-humble-rosidl-typesupport-fastrtps-c
BuildRequires:  ros-humble-rosidl-typesupport-fastrtps-cpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Provides:       ros-humble-rosidl-interface-packages(member)

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-cppcheck
BuildRequires:  ros-humble-ament-cpplint
BuildRequires:  ros-humble-ament-lint-auto
BuildRequires:  ros-humble-ament-lint-cmake
BuildRequires:  ros-humble-ament-lint-common
%endif

%if 0%{?with_weak_deps}
Supplements:    ros-humble-rosidl-interface-packages(all)
%endif

%description
ROS messages for MRPT classes and objects

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Wed May 18 2022 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.4.2-1
- Autogenerated by Bloom

* Fri May 13 2022 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.4.0-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.3.4-2
- Autogenerated by Bloom

* Sat Apr 02 2022 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.3.4-1
- Autogenerated by Bloom

* Wed Mar 30 2022 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.3.3-1
- Autogenerated by Bloom

* Wed Mar 30 2022 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.3.2-1
- Autogenerated by Bloom

* Sat Mar 05 2022 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.3.1-1
- Autogenerated by Bloom

