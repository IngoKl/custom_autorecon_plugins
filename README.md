# Custom AutoRecon Plugins

This is a small collection of my (public) plugins for Tib3rius' fantastic [AutoRecon](https://github.com/Tib3rius/AutoRecon/).

* `rustscan.py` -> QuickRustScanScan
* `ssh_custom.py` -> SSHAudit

## Additional Requirements

In addition to `AutoRecon` and all its requirements, you will need:

```
rustscan
ssh-audit
```

## Usage

`AutoRecon` has a beautiful and simple-to-use plugin system. On my `Kali` box, I keep my plugins in `/opt/custom_autorecon_plugins`.
To run the tool using my plugins in addition to the regular ones, I use:

`sudo autorecon IP --add-plugins-dir /opt/custom_autorecon_plugins`

## Credit

The `ssh-audit` plugin has been inspired by [blockomat2100](https://github.com/blockomat2100/autorecon-plugins)'s plugin collection.