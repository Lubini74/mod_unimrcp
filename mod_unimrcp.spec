######################################################################################################################
#
# Initial Version Copyright (C) 2023 atip Team, All Rights Reserved.
#
######################################################################################################################
# Module build settings
%define _unpackaged_files_terminate_build 0  
%define _build_id_links none
%define nonparsedversion 1.10.10
%define version %(echo '%{nonparsedversion}' | sed 's/-//g')
%define release 1

######################################################################################################################
#
%define _prefix   /usr
%define prefix    %{_prefix}

######################################################################################################################
# Layout of packages FHS (Redhat/SUSE), FS (Standard FreeSWITCH layout using /usr/local), OPT (/opt based layout)
%define packagelayout	FHS

%define	PREFIX		%{_prefix}
%define MODINSTDIR	%{_libdir}/freeswitch/mod


Name:         	mod_unimrcp
Summary:      	mod_unimrcp FreeSwitch plugin
License:      	MPL1.1
Group:        	Productivity/Telephony/Servers
Version:	%{version}
Release:	%{release}%{?dist}
URL:          	http://www.atip.de/
Packager:     	Ken Rice
Vendor:       	http://www.atip.de/

######################################################################################################################
#
#					Source files and where to get them
#
######################################################################################################################
Source0:        http://files.atip.de/%{name}-%{nonparsedversion}.tar.gz
Prefix:        	%{prefix}

######################################################################################################################
#
#					Where the packages are going to be built
#
######################################################################################################################
BuildRoot:    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
mod_unimrcp Plugin for FreeSwitch 


######################################################################################################################
#
#				Unpack and prepare Source archives, copy stuff around etc ..
#
######################################################################################################################

%prep
%setup -q

######################################################################################################################
#
#						Start the Build process
#
######################################################################################################################
%build
./bootstrap.sh
PKG_CONFIG_PATH=/usr/share/freeswitch/pkgconfig:/opt/unimrcp/lib/pkgconfig ./configure

######################################################################################################################
#
#				Install it and create some required dirs and links
#
######################################################################################################################
%install
%{__make} DESTDIR=%{buildroot} install
%{__rm} -f %{buildroot}/usr/lib64/freeswitch/mod/mod_unimrcp.la


######################################################################################################################
#
#			Add a freeswitch user with group daemon that will own the whole enchilada
#
######################################################################################################################
%pre

%post

%preun

%postun

%clean

%files
######################################################################################################################
#
#			What to install where ... first set default permissions
#
######################################################################################################################
%{MODINSTDIR}/mod_unimrcp.so*

######################################################################################################################
#
#						Changelog
#
######################################################################################################################
%changelog
* Wed May 17 2023 - Lubos (ATIP GmbH)
- Initial packet for mod_unimrcp

