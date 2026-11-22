"""news-image-20261121 entry: writes the Saturday 21 November 2026 front page.

The image is drawn ahead of time from frontpage.html and kept in the
repository as entry.png. At run time this program has no network, so it
only checks that picture against the competition limits and copies it,
byte for byte, into the output folder.
"""
import os
import struct
import sys
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
MAX_BYTES = 1024 * 1024          # 1 MiB cap from the rules
MAX_SIDE = 1024                  # at most 1024 x 1024 pixels
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(msg: str) -> None:
    sys.stderr.write("entry check failed: " + msg + "\n")
    sys.exit(1)


def check_png(data: bytes) -> tuple[int, int]:
    """Walk every chunk, verify each CRC, and return (width, height)."""
    if not data.startswith(PNG_MAGIC):
        fail("not a PNG (bad signature)")
    pos = len(PNG_MAGIC)
    width = height = None
    seen_end = False
    while pos < len(data):
        if pos + 8 > len(data):
            fail("truncated chunk header")
        length, ctype = struct.unpack(">I4s", data[pos:pos + 8])
        body = data[pos + 8:pos + 8 + length]
        crc_at = pos + 8 + length
        if crc_at + 4 > len(data):
            fail("truncated chunk " + ctype.decode("latin-1"))
        (crc,) = struct.unpack(">I", data[crc_at:crc_at + 4])
        if zlib.crc32(ctype + body) & 0xFFFFFFFF != crc:
            fail("bad CRC in chunk " + ctype.decode("latin-1"))
        if ctype == b"IHDR":
            width, height = struct.unpack(">II", body[:8])
        pos = crc_at + 4
        if ctype == b"IEND":
            seen_end = True
            break
    if width is None or not seen_end:
        fail("missing IHDR or IEND")
    return width, height


def main() -> int:
    try:
        with open(SOURCE, "rb") as fh:
            data = fh.read()
    except OSError as exc:
        fail("cannot read entry.png: " + str(exc))
    if len(data) > MAX_BYTES:
        fail(f"{len(data)} bytes is over the 1 MiB cap")
    width, height = check_png(data)
    if width > MAX_SIDE or height > MAX_SIDE or (width, height) != (1024, 1024):
        fail(f"image is {width}x{height}, expected 1024x1024")
    os.makedirs(OUT_DIR, exist_ok=True)
    target = os.path.join(OUT_DIR, "entry.png")
    with open(target, "wb") as fh:
        fh.write(data)
    with open(target, "rb") as fh:
        if fh.read() != data:
            fail("written file does not match the source bytes")
    print(f"wrote {target}: {width}x{height}, {len(data)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
