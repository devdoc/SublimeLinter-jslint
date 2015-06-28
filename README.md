SublimeLinter-contrib-jslint
================================

This linter plugin for [SublimeLinter][docs] provides an interface to [JSLint](http://www.jslint.com/lint.html). It will be used with files that have the “JavaScript” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that the `jslint` [npm package][jslint-npm] is installed on your system.

To install `jslint`, do the following:

1. Install [Node.js](http://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).

1. Install the `jslint` npm package by typing the following in a terminal:
   ```
   npm install -g jslint
   ```
   You may also specify the exact version of the package to be installed like this:
   ```
   npm install -g jslint@0.3.1
   ```

1. If you are using `nvm` and `zsh`, ensure that the line to load `nvm` is in `.zshenv` and not `.zshrc`.

1. If you are using `zsh` and `oh-my-zsh`, do not load the `nvm` plugin for `oh-my-zsh`.


### Linter configuration
In order for `jslint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `jslint`, you can proceed to install the SublimeLinter-contrib-jslint plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `jslint`. Among the entries you should see `SublimeLinter-contrib-jslint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

Linter Settings can be of use when you want to control the default behaviour of `jslint` globally for all files. The `args` linter setting can be used to specify options that will be passed to `jslint` on every run. For example, if you want to increase the maximum number of errors `jslint` will process from the default 50 to 100, you can add `"args": "--maxerr=100"` to the `jslint` section in SublimeLinter User settings. To list all supported options, run `jslint` without options from a command prompt. You may want to refer to the [readme](https://npmjs.org/package/jslint#readme) for the `jslint` npm package, and to the [description of JSLint options][jslint-options-20130826].

Please note that options can also be specified

- in a file called `.jslintrc` written in JSON format, specifying options as key-value pairs (refer to [description of JSLint options][jslint-options-20130826] for specifics on valid keys and values)
    * globally, by placing the file in the user's home directory
    * for directories or hierarchies of directories (please refer to SublimeLinter's [documentation for the config_file attribute][config_file] to understand where SublimeLinter will search for `.jslintrc`)
- by inline [JSLint directives](http://www.jslint.com/lint.html#options) in the JavaScript files to be linted.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbrevations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
[jslint-npm]: https://www.npmjs.org/package/jslint
[jslint-options-20130826]: https://github.com/douglascrockford/JSLint/blob/650bcde1642e53cbfbd248a6092ddebb61ce3985/jslint.js#L178
[config_file]: http://www.sublimelinter.com/en/latest/linter_attributes.html#config-file
