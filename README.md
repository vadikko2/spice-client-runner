# SPICE client runner for MacOS

The script listens set directory and
run [remote-viewer](https://gist.github.com/tomdaley92/789688fc68e77477d468f7b9e59af51c)
for all just downloaded files with set suffix.

```
optional arguments:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     Working directory. By default "~/Downloads"
  -s SUFFIX, --suffix SUFFIX
                        SPICE file suffix. By default ".vv"
```

#### For enable to launchd do:
- Fix `.plist` file
- `launchctl bootstrap gui/<UID> <PATH_TO FILE>`. For get UID do `id -u`
- check service by `launchctl list | grep spice`. this will return a line like this: `<pid> <status> spice.client`.

#### For disable do:
- `launchctl bootout gui/<UID> <PATH_TO_FILE>`  