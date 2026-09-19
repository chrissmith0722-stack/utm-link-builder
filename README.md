# utm-link-builder

Build campaign URLs with UTM parameters from the command line.

## Requirements

- Python 3.9+

## Usage

```bash
python utm_link_builder.py \
  --url "https://example.com/product" \
  --source twitter \
  --medium social \
  --campaign launch-week \
  --content thread-1 \
  --term indie-tools
```

Prints a single absolute URL with encoded query params.

Required: `--url`, `--source`, `--medium`, `--campaign`  
Optional: `--content`, `--term`

Existing query strings on the base URL are preserved.

## License

MIT
