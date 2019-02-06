# netsnake

Netsnake is simple network utility 
which redirects TCP to `prog` stdin/stdout like `netcat -e`  


## Install

```
pip install -e .
```

## Usage

```
netsnake -p 8080 /bin/cat
```