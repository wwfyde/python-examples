#!/usr/bin/env just --justfile
export PATH := join(justfile_directory(), ".env", "bin") + ":" + env_var('PATH')

upgrade:
    uv lock --upgrade

[arg("bar", long="bar")]
foo bar:
    echo bar
