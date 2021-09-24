[personal] OBS version: https://build.opensuse.org/package/show/home:sbradnick/runit
20210924: this is a test.

```
#
# [20210730] Initial attempt at runit.
#
```

```
git clone -b wsl https://github.com/sbradnick/runit.git
cd SPEC
```

Build with:
```
rpmbuild --target x86_64 -bb runit.spec
````

Install with:
```
sudo zypper in ~/rpmbuild/RPMS/x86_64/<something>.rpm
```

Verify with:
```
rpm -ql runit
zypper info runit
```

Info on variables:
```
$ rpm --eval %{_sysconfdir}
/etc

$ rpm --eval %{buildroot}
/home/scott/rpmbuild/BUILDROOT/%{NAME}-%{VERSION}-%{RELEASE}.x86_64
```
