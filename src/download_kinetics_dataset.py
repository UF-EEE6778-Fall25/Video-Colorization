#!/usr/bin/env python3
"""
download_kinetics_dataset.py

Reads `k400_subset.txt` (a list of .gz/.tar.gz URLs), downloads the files
to the SAME directory as the txt file, and extracts them into `data/dataset/`.

Usage:
    python src/download_kinetics_dataset.py

Assumptions:
- `k400_subset.txt` exists either in:
    1) data/kinetics-dataset/  OR
    2) current working directory OR
    3) this script's directory
- URLs point to .tar.gz (Kinetics-style) or .gz files.

"""

from pathlib import Path
import urllib.request
from urllib.error import URLError, HTTPError
from tqdm import tqdm
import tarfile
import gzip
import shutil
import sys

# ---------------------- Helpers ----------------------

def find_k400_list() -> Path | None:
    """
    Locate k400_subset.txt by checking common locations.
    Priority:
      1) data/kinetics-dataset/k400_subset.txt
      2) current working directory
      3) script directory
    """
    repo_root = Path(__file__).resolve().parents[1]
    candidates = [
        repo_root / "data" / "kinetics-dataset" / "k400_subset.txt",
        Path.cwd() / "k400_subset.txt",
        Path(__file__).resolve().parent / "k400_subset.txt",
    ]
    for p in candidates:
        if p.exists():
            return p
    return None


def iter_urls_from_file(txt_path: Path):
    """Yield cleaned URLs from a text file, skipping comments/blank lines."""
    with txt_path.open("r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            yield s


def download_with_progress(url: str, dest: Path):
    """Download a URL to dest with a progress bar."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    print(f"⬇️  Downloading: {dest.name}")
    try:
        with urllib.request.urlopen(url) as resp, open(dest, "wb") as out:
            total = int(resp.getheader("Content-Length", 0) or 0)
            chunk_size = 1024 * 256
            with tqdm(total=total, unit="B", unit_scale=True, desc=dest.name) as pbar:
                while True:
                    chunk = resp.read(chunk_size)
                    if not chunk:
                        break
                    out.write(chunk)
                    pbar.update(len(chunk))
        print(f"✅ Saved: {dest}")
    except HTTPError as e:
        print(f"❌ HTTP error for {url}: {e.code} {e.reason}")
        raise
    except URLError as e:
        print(f"❌ URL error for {url}: {e.reason}")
        raise
    except Exception as e:
        print(f"❌ Failed to download {url}: {e}")
        raise


def is_tar_gz(p: Path) -> bool:
    return p.suffixes[-2:] == [".tar", ".gz"] or p.suffix == ".tgz"


def safe_extract_tar(tar: tarfile.TarFile, path: Path):
    """Prevent path traversal when extracting tar archives."""
    path = path.resolve()
    for member in tar.getmembers():
        member_path = (path / member.name).resolve()
        if not str(member_path).startswith(str(path)):
            raise Exception("Blocked path traversal attempt in tar file")
    tar.extractall(path=path)


def extract_archive(src: Path, out_dir: Path):
    """
    Extract .tar.gz/.tgz into out_dir (preserving internal structure).
    For plain .gz (single-file gzip), decompress to out_dir/<name without .gz>.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    if is_tar_gz(src):
        print(f"📦 Extracting (tar.gz): {src.name}")
        try:
            with tarfile.open(src, "r:gz") as tf:
                safe_extract_tar(tf, out_dir)
            print(f"✅ Extracted to: {out_dir}")
        except Exception as e:
            print(f"❌ Extraction failed for {src.name}: {e}")
            raise
    elif src.suffix == ".gz":
        # Decompress a single gzip file
        target = out_dir / src.with_suffix("").name
        print(f"📦 Decompressing (gz): {src.name} → {target.name}")
        try:
            with gzip.open(src, "rb") as fin, open(target, "wb") as fout:
                shutil.copyfileobj(fin, fout)
            print(f"✅ Decompressed to: {target}")
        except Exception as e:
            print(f"❌ Decompression failed for {src.name}: {e}")
            raise
    else:
        print(f"ℹ️  Skipping (unknown archive type): {src.name}")


# ---------------------- Main ----------------------

def main():
    print("==============================================")
    print("  Kinetics (K400 subset) Fetch & Extract")
    print("==============================================\n")

    txt_path = find_k400_list()
    if not txt_path:
        print("❌ Could not find `k400_subset.txt` in expected locations:")
        print("   - data/kinetics-dataset/k400_subset.txt")
        print("   - ./k400_subset.txt (current directory)")
        print("   - src/k400_subset.txt (script directory)")
        sys.exit(1)

    txt_dir = txt_path.parent
    repo_root = Path(__file__).resolve().parents[1]
    extract_dir = repo_root / "data" / "dataset"

    print(f"📄 Using list: {txt_path}")
    print(f"📥 Downloads will be saved to: {txt_dir}")
    print(f"🗂  Extracting all archives into: {extract_dir}\n")

    urls = list(iter_urls_from_file(txt_path))
    if not urls:
        print("❌ No URLs found in k400_subset.txt.")
        sys.exit(1)

    # Download all
    for url in urls:
        filename = url.split("/")[-1]
        dest = txt_dir / filename
        download_with_progress(url, dest)

    print("\n----------------------------------------------")
    print("✅ Downloads complete. Beginning extraction...")
    print("----------------------------------------------\n")

    # Extract all downloaded .gz files found in txt_dir
    gz_files = sorted([p for p in txt_dir.iterdir() if p.is_file() and p.suffix == ".gz" or is_tar_gz(p)])
    if not gz_files:
        print("❌ No .gz/.tar.gz files found to extract.")
        sys.exit(1)

    for gz in gz_files:
        try:
            extract_archive(gz, extract_dir)
        except Exception:
            # continue to next file but keep reporting errors
            continue

    print("\n==============================================")
    print("🎉 All done!")
    print(f"   Extracted dataset folder: {extract_dir}")
    print("==============================================\n")


if __name__ == "__main__":
    main()
