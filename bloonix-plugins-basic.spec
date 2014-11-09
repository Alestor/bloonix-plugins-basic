Summary: Basic Bloonix plugins.
Name: bloonix-plugins-basic
Version: 0.21
Release: 1%{dist}
License: Commercial
Group: Utilities/System
Distribution: RHEL and CentOS

Packager: Jonny Schulz <js@bloonix.de>
Vendor: Bloonix

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Source0: http://download.bloonix.de/sources/%{name}-%{version}.tar.gz
Requires: bloonix-core
Requires: curl
Requires: perl(Getopt::Long)
Requires: perl(Time::HiRes)
Requires: perl(Authen::SASL)
Requires: perl(MIME::Base64)
AutoReqProv: no

%description
bloonix-plugins-basic provides base plugins.

%define blxdir /usr/lib/bloonix
%define docdir %{_docdir}/%{name}-%{version}

%prep
%setup -q -n %{name}-%{version}

%build
%{__perl} Configure.PL --prefix /usr
%{__make}

%install
rm -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
mkdir -p ${RPM_BUILD_ROOT}%{docdir}
install -c -m 0444 LICENSE ${RPM_BUILD_ROOT}%{docdir}/
install -c -m 0444 ChangeLog ${RPM_BUILD_ROOT}%{docdir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%dir %{blxdir}
%dir %{blxdir}/plugins
%{blxdir}/plugins/check-*
%{blxdir}/etc/plugins/plugin-*

%dir %attr(0755, root, root) %{docdir}
%doc %attr(0444, root, root) %{docdir}/ChangeLog
%doc %attr(0444, root, root) %{docdir}/LICENSE

%changelog
* Sat Nov 08 2014 Jonny Schulz <js@bloonix.de> - 0.21-1
- Fixed arguments warn-count and warning of check-logfile.
- Fixed the search order for warnings and criticals of check-logfile.
- Improved argument examples for check-logfile.
- Fixed a typo in check-logfile description.
* Mon Nov 03 2014 Jonny Schulz <js@bloonix.de> - 0.20-1
- Updated the license information.
* Tue Aug 26 2014 Jonny Schulz <js@bloonix.de> - 0.19-1
- An mtr result is added if the extern checks fails.
- Limit the maximum packages for check-ping to 10.
- Licence added and old releases deleted.
* Tue May 27 2014 Jonny Schulz <js@bloonix.de> - 0.18-1
- Implement SSL to check-ftp.
* Sat Apr 12 2014 Jonny Schulz <js@bloonix.de> - 0.16-1
- Added the new check check-filestat.
* Sat Mar 23 2014 Jonny Schulz <js@bloonix.de> - 0.14-1
- Complete rewrite of all plugins.
- The statistics of all plugins is now printed in JSON format.
* Sun Sep 16 2012 Jonny Schulz <js@bloonix.de> - 0.12-1
- kill -9 is now send to the curl process if eval{}
  returns an error.
- check-imap is a complete rewrite. Now it's possible to
  check mail account with check-smtp and check-imap in
  conjunction. check-smtp sends the mail and check-imap
  collects it.
- Plugin check-smtp accept now --subject as option.
- Now it's not possible any more to set the path and
  filename for the plugin check-logfile and paramater -d.
- Added CONFIG_PATH to check-dbconnect.
- Improved check-dbconnect and added parameter -f.
- Moved $time calculation in check-http to an earlier place.
- Added new plugin check-dns.
- Added plugin-plain for plain data.
- Kicked YAML::Syck from check-logfile.
* Tue Jan 03 2012 Jonny Schulz <js@bloonix.de> - 0.10-1
- Fixed a little bug with the error handling of argument --error
  and added the curl parameter --max-time for a better timeout
  handling.
- check-logfile now parses a logfile if the logfile was rotated.
  By default the old logfile with extension .1 will be parsed.
- Updated the plugin-* files.
- Now it's possible to request host:port with check-http.
- Fixed check-http: the request must not end with a slash.
* Fri Jul 01 2011 Jonny Schulz <js@bloonix.de> - 0.7-1
- Kicked unused option o_stat.
* Tue Jun 21 2011 Jonny Schulz <js@bloonix.de> - 0.6-1
- Added content length in output for check-http.
* Mon Dec 27 2010 Jonny Schulz <js@bloonix.de> - 0.4-1
- Renamed all plugin files from *.plugin to plugin-*.
* Thu Nov 25 2010 Jonny Schulz <js@bloonix.de> - 0.3-1
- Fixed argument handling for warning and critical
  in check-logfile and now it's possible to set
  a path + filename for the data file.
* Wed Nov 17 2010 Jonny Schulz <js@bloonix.de> - 0.2-1
- Fixed header and content regex and removes //sm
- Fixed output line for check-http (HTTPS) and
  check-smtp (SMTPS).
- Kicked option --stat from all plugins, because
  statistics will be printed by default on stdout.
* Mon Aug 02 2010 Jonny Schulz <js@bloonix.de> - 0.1-1
- Initial release.